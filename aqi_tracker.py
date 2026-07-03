#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Taiwan Air Quality Tracker - Core Script
Fetches AQI reports from the Taiwan Ministry of Environment (MOENV) Open Data Platform,
saves it in JSON format, updates README.md, and hosts a dashboard to visualize it.
"""

import os
import ssl
import json
import argparse
import datetime
import urllib.request
import urllib.error
import http.server
import socketserver
import webbrowser
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

# Constants
DEFAULT_CONFIG_FILE = "config.json"
API_URL = "https://data.moenv.gov.tw/api/v2/aqx_p_432"
# Default API key (from public tutorials, subject to rate limits, but works for testing)
DEFAULT_API_KEY = "e75b1660-e564-4107-aad5-a8be1f905dd9"

DEFAULT_CONFIG = {
    "moenv_api_key": DEFAULT_API_KEY,
    "output_dir": "data",
    "server_port": 8800
}

def setup_config():
    """Create default config file if it does not exist."""
    if not os.path.exists(DEFAULT_CONFIG_FILE):
        print(f"[*] Creating default configuration file: {DEFAULT_CONFIG_FILE}")
        with open(DEFAULT_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4, ensure_ascii=False)
        print("[!] Please edit 'config.json' and fill in your Ministry of Environment API key (moenv_api_key) if needed.")
        print("[!] You can obtain a free API key at: https://data.moenv.gov.tw/")
        return DEFAULT_CONFIG
    
    try:
        with open(DEFAULT_CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
            # Migration check: if cwa_api_key is there, migrate/add moenv_api_key
            updated = False
            if "cwa_api_key" in config and "moenv_api_key" not in config:
                config["moenv_api_key"] = DEFAULT_API_KEY
                updated = True
            if updated:
                with open(DEFAULT_CONFIG_FILE, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=4, ensure_ascii=False)
            return config
    except Exception as e:
        print(f"[!] Error reading config file: {e}")
        return DEFAULT_CONFIG

def get_api_key(config):
    """Retrieve API key from config or environment variable."""
    api_key = os.environ.get("MOENV_API_KEY")
    if api_key:
        return api_key
    
    config_key = config.get("moenv_api_key")
    if config_key and config_key != "YOUR_MOENV_API_KEY_HERE":
        return config_key
        
    return DEFAULT_API_KEY

def fetch_aqi_data(api_key):
    """Fetch JSON data from MOENV Open Data API."""
    query_url = f"{API_URL}?api_key={api_key}&format=json"
    
    print(f"[*] Fetching Taiwan Air Quality data from MOENV Open Data Platform...")
    
    req = urllib.request.Request(
        query_url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) TaiwanAqiTracker/1.0'}
    )
    
    try:
        # Avoid SSL cert verification issues
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(req, timeout=30, context=context) as response:
            if response.status == 200:
                raw_data = response.read().decode('utf-8')
                return json.loads(raw_data)
                
            print(f"[!] API request failed with status code: {response.status}")
            return None
    except urllib.error.HTTPError as e:
        print(f"[!] HTTP Error {e.code}: {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"[!] Connection Error: {e.reason}")
        return None
    except Exception as e:
        print(f"[!] Unexpected error during fetch: {e}")
        return None

def parse_aqi(raw_data):
    """Parses MOENV AQI JSON list into a clean format."""
    # The MOENV API returns a list directly or a dict with records
    parsed_list = []
    
    if isinstance(raw_data, list):
        records = raw_data
    elif isinstance(raw_data, dict) and "records" in raw_data:
        records = raw_data["records"]
    else:
        print("[!] Warning: API response format unexpected.")
        return []
        
    for item in records:
        # Validate critical fields
        site_name = item.get("sitename", "").strip()
        county = item.get("county", "").strip()
        if not site_name or not county:
            continue
            
        # Parse AQI value to int if possible, else None
        aqi_str = item.get("aqi", "")
        aqi_val = None
        if aqi_str and aqi_str.isdigit():
            aqi_val = int(aqi_str)
            
        parsed_list.append({
            "site_id": item.get("siteid", ""),
            "site_name": site_name,
            "county": county,
            "aqi": aqi_val,
            "status": item.get("status", "未知").strip(),
            "pollutant": item.get("pollutant", "").strip(),
            "pm2_5": item.get("pm2.5", "").strip(),
            "pm2_5_avg": item.get("pm2.5_avg", "").strip(),
            "pm10": item.get("pm10", "").strip(),
            "pm10_avg": item.get("pm10_avg", "").strip(),
            "o3": item.get("o3", "").strip(),
            "o3_8hr": item.get("o3_8hr", "").strip(),
            "co": item.get("co", "").strip(),
            "co_8hr": item.get("co_8hr", "").strip(),
            "so2": item.get("so2", "").strip(),
            "so2_avg": item.get("so2_avg", "").strip(),
            "no2": item.get("no2", "").strip(),
            "no": item.get("no", "").strip(),
            "nox": item.get("nox", "").strip(),
            "wind_speed": item.get("wind_speed", "").strip(),
            "wind_direc": item.get("wind_direc", "").strip(),
            "longitude": item.get("longitude", "").strip(),
            "latitude": item.get("latitude", "").strip(),
            "publish_time": item.get("publishtime", "").strip()
        })
        
    return parsed_list

def get_aqi_color_emoji(aqi):
    if aqi is None:
        return "⚪"
    if aqi <= 50:
        return "🟢"
    elif aqi <= 100:
        return "🟡"
    elif aqi <= 150:
        return "🟠"
    elif aqi <= 200:
        return "🔴"
    elif aqi <= 300:
        return "🟣"
    else:
        return "🟤"

def get_aqi_health_status(aqi):
    if aqi is None:
        return "無資料"
    if aqi <= 50:
        return "良好"
    elif aqi <= 100:
        return "普通"
    elif aqi <= 150:
        return "對敏感族群不健康"
    elif aqi <= 200:
        return "對所有族群不健康"
    elif aqi <= 300:
        return "非常不健康"
    else:
        return "危害"

def update_readme(aqi_list, data_dir):
    """Update README.md with the latest AQI information."""
    readme_path = SCRIPT_DIR / "README.md"
    if not readme_path.exists():
        print("[!] README.md not found. Skipping README update.")
        return
        
    tz_taiwan = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_taiwan)
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Filter out stations without AQI data
    valid_aqi_list = [item for item in aqi_list if item["aqi"] is not None]
    
    # Sort by AQI descending
    valid_aqi_list.sort(key=lambda x: x["aqi"], reverse=True)
    
    # Calculate stats
    total_stations = len(valid_aqi_list)
    avg_aqi = sum(x["aqi"] for x in valid_aqi_list) / total_stations if total_stations > 0 else 0
    
    # Cleanest and most polluted
    cleanest = valid_aqi_list[-1] if valid_aqi_list else None
    polluted = valid_aqi_list[0] if valid_aqi_list else None
    
    # Generate Markdown content
    md_content = []
    md_content.append(f"**⏰ Last Updated (Taipei Time)**: `{formatted_time}`\n")
    
    if valid_aqi_list:
        md_content.append("### 🚨 Current Air Quality Summary")
        md_content.append(f"- **Total Active Stations**: {total_stations}")
        md_content.append(f"- **National Average AQI**: `{avg_aqi:.1f}` ({get_aqi_health_status(avg_aqi)})")
        if cleanest:
            md_content.append(f"- **🟢 Cleanest Location**: {cleanest['county']}{cleanest['site_name']} (AQI: `{cleanest['aqi']}`)")
        if polluted:
            md_content.append(f"- **🔴 Most Polluted Location**: {polluted['county']}{polluted['site_name']} (AQI: `{polluted['aqi']}`, Main Pollutant: `{polluted['pollutant'] or 'None'}`)")
        
        md_content.append("\n### 🗺️ Top 10 Cleanest Stations")
        md_content.append("| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |")
        md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
        for item in reversed(valid_aqi_list[-10:]):
            emoji = get_aqi_color_emoji(item['aqi'])
            md_content.append(f"| {item['site_name']} | {item['county']} | `{item['aqi']}` | {emoji} {item['status']} | {item['pm2_5']} | {item['pm10']} |")
            
        md_content.append("\n### 🚨 Top 10 Most Polluted Stations")
        md_content.append("| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |")
        md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
        for item in valid_aqi_list[:10]:
            emoji = get_aqi_color_emoji(item['aqi'])
            md_content.append(f"| {item['site_name']} | {item['county']} | `{item['aqi']}` | {emoji} {item['status']} | {item['pollutant'] or 'None'} | {item['pm2_5']} |")
    else:
        md_content.append("*No AQI records available.*")
        
    md_block = "\n".join(md_content)
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_text = f.read()
            
        start_marker = "<!-- AQI_START -->"
        end_marker = "<!-- AQI_END -->"
        
        # We reuse the same markers or rename them in README.md. Let's make sure it handles both.
        if start_marker in readme_text and end_marker in readme_text:
            parts = readme_text.split(start_marker)
            before = parts[0]
            after = parts[1].split(end_marker)[1]
            
            new_readme = f"{before}{start_marker}\n\n{md_block}\n\n{end_marker}{after}"
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_readme)
            print("[+] README.md has been automatically updated with the latest AQI info.")
        else:
            print("[!] Warning: AQI start/end markers not found in README.md. Skipping README update.")
    except Exception as e:
        print(f"[!] Failed to update README.md: {e}")

def update_statistics(aqi_list, data_dir):
    """Update statistics tracking average AQI by county and state distributions."""
    stats_file = data_dir / "stats.json"
    
    # Filter out stations without AQI data
    valid_aqi_list = [item for item in aqi_list if item["aqi"] is not None]
    
    county_map = {}
    good_count = 0
    moderate_count = 0
    unhealthy_sens_count = 0
    unhealthy_all_count = 0
    very_unhealthy_count = 0
    hazardous_count = 0
    
    for item in valid_aqi_list:
        aqi = item["aqi"]
        county = item["county"]
        
        if county not in county_map:
            county_map[county] = []
        county_map[county].append(aqi)
        
        if aqi <= 50:
            good_count += 1
        elif aqi <= 100:
            moderate_count += 1
        elif aqi <= 150:
            unhealthy_sens_count += 1
        elif aqi <= 200:
            unhealthy_all_count += 1
        elif aqi <= 300:
            very_unhealthy_count += 1
        else:
            hazardous_count += 1
            
    county_averages = []
    for county, aqis in county_map.items():
        avg = sum(aqis) / len(aqis) if aqis else 0
        county_averages.append({
            "county": county,
            "average_aqi": round(avg, 1),
            "station_count": len(aqis),
            "max_aqi": max(aqis) if aqis else None,
            "min_aqi": min(aqis) if aqis else None
        })
        
    # Sort county averages by average AQI descending
    county_averages.sort(key=lambda x: x["average_aqi"], reverse=True)
    
    tz_taiwan = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_taiwan)
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    stats_data = {
        "updated_at": formatted_time,
        "summary": {
            "total_stations": len(valid_aqi_list),
            "good_count": good_count,
            "moderate_count": moderate_count,
            "unhealthy_sensitive_count": unhealthy_sens_count,
            "unhealthy_all_count": unhealthy_all_count,
            "very_unhealthy_count": very_unhealthy_count,
            "hazardous_count": hazardous_count
        },
        "county_averages": county_averages
    }
    
    try:
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats_data, f, indent=2, ensure_ascii=False)
        print(f"[+] Saved statistics to {stats_file}")
    except Exception as e:
        print(f"[!] Failed to save stats JSON: {e}")
        
    # Generate Markdown Tables for README STATS section
    md_lines = []
    md_lines.append("### 📊 National AQI Level Distribution")
    md_lines.append("| AQI Level | Range | Color | Station Count | Percentage |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    total = len(valid_aqi_list)
    if total > 0:
        md_lines.append(f"| 良好 (Good) | 0 - 50 | 🟢 Green | {good_count} | {(good_count/total)*100:.1f}% |")
        md_lines.append(f"| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | {moderate_count} | {(moderate_count/total)*100:.1f}% |")
        md_lines.append(f"| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | {unhealthy_sens_count} | {(unhealthy_sens_count/total)*100:.1f}% |")
        md_lines.append(f"| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | {unhealthy_all_count} | {(unhealthy_all_count/total)*100:.1f}% |")
        md_lines.append(f"| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | {very_unhealthy_count} | {(very_unhealthy_count/total)*100:.1f}% |")
        md_lines.append(f"| 危害 (Hazardous) | 301+ | 🟤 Maroon | {hazardous_count} | {(hazardous_count/total)*100:.1f}% |")
    else:
        md_lines.append("| No stations reporting | | | | |")
        
    md_lines.append("\n### 🏢 Average AQI by County / City")
    md_lines.append("| County | Station Count | Average AQI | Range (Min - Max) | Status |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    
    for c in county_averages:
        emoji = get_aqi_color_emoji(c["average_aqi"])
        status = get_aqi_health_status(c["average_aqi"])
        md_lines.append(f"| {c['county']} | {c['station_count']} | `{c['average_aqi']}` | `{c['min_aqi']} - {c['max_aqi']}` | {emoji} {status} |")
        
    md_block = "\n".join(md_lines)
    
    readme_path = SCRIPT_DIR / "README.md"
    if readme_path.exists():
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                readme_text = f.read()
                
            start_marker = "<!-- STATS_START -->"
            end_marker = "<!-- STATS_END -->"
            
            if start_marker in readme_text and end_marker in readme_text:
                parts = readme_text.split(start_marker)
                before = parts[0]
                after = parts[1].split(end_marker)[1]
                
                new_readme = f"{before}{start_marker}\n\n{md_block}\n\n{end_marker}{after}"
                
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(new_readme)
                print("[+] README.md has been automatically updated with AQI statistics.")
            else:
                print("[!] Warning: STATS markers not found in README.md. Skipping stats update.")
        except Exception as e:
            print(f"[!] Failed to update README stats: {e}")

def update_county_files(aqi_list, data_dir):
    """Update individual county JSON files with AQI histories of stations in each county."""
    counties_dir = data_dir / "counties"
    counties_dir.mkdir(parents=True, exist_ok=True)
    
    tz_taiwan = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_taiwan)
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    county_data_map = {}
    
    for item in aqi_list:
        county_name = item["county"]
        if not county_name:
            continue
            
        if county_name not in county_data_map:
            county_file = counties_dir / f"{county_name}.json"
            existing_data = {"county": county_name, "updated_at": formatted_time, "stations": []}
            if county_file.exists():
                try:
                    with open(county_file, 'r', encoding='utf-8') as f:
                        loaded = json.load(f)
                        if isinstance(loaded, dict) and "stations" in loaded:
                            existing_data = loaded
                except Exception:
                    pass
            county_data_map[county_name] = existing_data

        stations_list = county_data_map[county_name]["stations"]
        # Remove existing station entry if present to update it
        stations_list = [s for s in stations_list if s["site_name"] != item["site_name"]]
        
        stations_list.append(item)
        county_data_map[county_name]["stations"] = stations_list
        
    for county_name, data in county_data_map.items():
        data["stations"].sort(key=lambda x: x["aqi"] if x["aqi"] is not None else 999)
        data["updated_at"] = formatted_time
        
        county_file = counties_dir / f"{county_name}.json"
        try:
            with open(county_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[!] Failed to save county file for {county_name}: {e}")
            
    print(f"[+] Updated {len(county_data_map)} individual county AQI files in: {counties_dir}")

def save_aqi_json(aqi_list, output_dir):
    """Save AQI data list to aqi.json file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / "aqi.json"
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(aqi_list, f, indent=2, ensure_ascii=False)
        print(f"[+] AQI JSON updated: {file_path} (Total: {len(aqi_list)} records)")
        return file_path
    except Exception as e:
        print(f"[!] Failed to save AQI JSON: {e}")
        return None

def run_fetch_pipeline(config):
    """Main pipeline to fetch, parse, and save AQI data."""
    api_key = get_api_key(config)
    output_dir = SCRIPT_DIR / config.get("output_dir", "data")
    
    raw_data = fetch_aqi_data(api_key)
    if not raw_data:
        print("[!] Error: No AQI data could be retrieved. Aborting update.")
        return False
        
    aqi_list = parse_aqi(raw_data)
    if not aqi_list:
        print("[!] Error: Parsing AQI data failed or empty results. Aborting update.")
        return False
        
    # Sort alphabetically by county, then site name
    aqi_list.sort(key=lambda x: (x["county"], x["site_name"]))
    
    # Save main JSON file
    save_aqi_json(aqi_list, output_dir)
    
    # Update README.md
    update_readme(aqi_list, output_dir)
    
    # Update statistics
    update_statistics(aqi_list, output_dir)
    
    # Update county files
    update_county_files(aqi_list, output_dir)
    
    print("[+] Air Quality data pipeline completed successfully!")
    return True

def serve_dashboard(port, output_dir):
    """Start a local web server to display the air quality dashboard."""
    class DashboardHTTPHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()
            
    socketserver.TCPServer.allow_reuse_address = True
    
    current_port = port
    max_attempts = 20
    httpd = None
    
    for attempt in range(max_attempts):
        try:
            httpd = socketserver.TCPServer(("", current_port), DashboardHTTPHandler)
            break
        except OSError as e:
            if "already in use" in str(e) or getattr(e, 'errno', None) in (98, 10048):
                print(f"[!] Port {current_port} is already in use. Trying port {current_port + 1}...")
                current_port += 1
            else:
                print(f"[!] Socket error: {e}")
                return
                
    if not httpd:
        print(f"[!] Failed to find an open port after {max_attempts} attempts.")
        return
        
    try:
        with httpd:
            print(f"[+] Air Quality Dashboard is live!")
            print(f"[*] Opening browser to http://localhost:{current_port}/index.html ...")
            webbrowser.open(f"http://localhost:{current_port}/index.html")
            print("[*] Press Ctrl+C to stop the server.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")
    except Exception as e:
        print(f"[!] Failed to run dashboard server: {e}")

def main():
    parser = argparse.ArgumentParser(description="Taiwan Air Quality Tracker CLI")
    parser.add_argument("--fetch", action="store_true", help="Fetch latest AQI data from MOENV API")
    parser.add_argument("--serve", action="store_true", help="Start the dashboard local web server")
    parser.add_argument("--port", type=int, default=None, help="Dashboard port (default from config or 8800)")
    parser.add_argument("--setup", action="store_true", help="Initialize or fix config.json")
    
    args = parser.parse_args()
    
    # Initialize configuration
    config = setup_config()
    
    if args.setup:
        print("[+] Setup complete. Please configure config.json before running.")
        return
        
    action_taken = False
    
    if args.fetch:
        action_taken = True
        run_fetch_pipeline(config)
        
    if args.serve:
        action_taken = True
        port = args.port or config.get("server_port", 8800)
        serve_dashboard(port, None)
        
    if not action_taken:
        # Default behavior: run fetch, then exit.
        print("[*] No action specified. Running AQI data fetch pipeline...")
        success = run_fetch_pipeline(config)
        if success:
            print("\n[*] Tip: Run 'python aqi_tracker.py --serve' to view the visual dashboard!")
            print("[*] Tip: Edit config.json to supply your MOENV Open Data API key.")

if __name__ == "__main__":
    main()
