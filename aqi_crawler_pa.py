#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Taiwan Air Quality Tracker - PythonAnywhere Dedicated Crawler
Fetches AQI reports from the MOENV API, parses, saves to data/aqi.json,
and updates README.md. Designed to be run periodically via cron/scheduled tasks.
"""

import os
import ssl
import json
import datetime
import urllib.request
import urllib.error
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = SCRIPT_DIR / "config.json"
DEFAULT_API_KEY = "e75b1660-e564-4107-aad5-a8be1f905dd9"

def get_config():
    if not CONFIG_PATH.exists():
        default_config = {
            "moenv_api_key": DEFAULT_API_KEY,
            "output_dir": "data",
            "server_port": 8800
        }
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4, ensure_ascii=False)
        print(f"[!] config.json not found. Created template at: {CONFIG_PATH}")
        return default_config

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error reading config.json: {e}")
        return None

def fetch_aqi_data(api_key):
    query_url = f"https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key={api_key}&format=json"
    
    print(f"[*] Fetching Taiwan Air Quality data from MOENV Open Data Platform...")
    
    req = urllib.request.Request(
        query_url, 
        headers={'User-Agent': 'PythonAnywhereAqiClient/1.0'}
    )
    
    try:
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
    parsed_list = []
    
    if isinstance(raw_data, list):
        records = raw_data
    elif isinstance(raw_data, dict) and "records" in raw_data:
        records = raw_data["records"]
    else:
        print("[!] Warning: API response format unexpected.")
        return []
        
    for item in records:
        site_name = item.get("sitename", "").strip()
        county = item.get("county", "").strip()
        if not site_name or not county:
            continue
            
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
    readme_path = SCRIPT_DIR / "README.md"
    if not readme_path.exists():
        print("[!] README.md not found. Skipping README update.")
        return
        
    tz_taiwan = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_taiwan)
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    valid_aqi_list = [item for item in aqi_list if item["aqi"] is not None]
    valid_aqi_list.sort(key=lambda x: x["aqi"], reverse=True)
    
    total_stations = len(valid_aqi_list)
    avg_aqi = sum(x["aqi"] for x in valid_aqi_list) / total_stations if total_stations > 0 else 0
    cleanest = valid_aqi_list[-1] if valid_aqi_list else None
    polluted = valid_aqi_list[0] if valid_aqi_list else None
    
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
        
        if start_marker in readme_text and end_marker in readme_text:
            parts = readme_text.split(start_marker)
            before = parts[0]
            after = parts[1].split(end_marker)[1]
            
            new_readme = f"{before}{start_marker}\n\n{md_block}\n\n{end_marker}{after}"
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_readme)
            print("[+] README.md has been automatically updated with the latest AQI info.")
    except Exception as e:
        print(f"[!] Failed to update README.md: {e}")

def update_statistics(aqi_list, data_dir):
    stats_file = data_dir / "stats.json"
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
    except Exception as e:
        print(f"[!] Failed to save stats JSON: {e}")
        
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
                print("[+] README.md has been automatically updated with yearly statistics.")
        except Exception as e:
            print(f"[!] Failed to update README stats: {e}")

def update_county_files(aqi_list, data_dir):
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

def main():
    config = get_config()
    if not config:
        print("[!] Crawler aborted due to missing configuration.")
        return
        
    api_key = config.get("moenv_api_key", DEFAULT_API_KEY)
    output_dir = SCRIPT_DIR / config.get("output_dir", "data")
    
    raw_data = fetch_aqi_data(api_key)
    if not raw_data:
        print("[!] Error: No AQI data retrieved. Exiting.")
        return
        
    aqi_list = parse_aqi(raw_data)
    if not aqi_list:
        print("[!] Error: AQI list empty. Exiting.")
        return
        
    aqi_list.sort(key=lambda x: (x["county"], x["site_name"]))
    
    # Save files
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_dir / "aqi.json", "w", encoding="utf-8") as f:
        json.dump(aqi_list, f, indent=2, ensure_ascii=False)
        
    update_readme(aqi_list, output_dir)
    update_statistics(aqi_list, output_dir)
    update_county_files(aqi_list, output_dir)
    
    print("[+] Headless AQI crawler run completed successfully.")

if __name__ == "__main__":
    main()
