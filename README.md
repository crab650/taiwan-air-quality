# Taiwan Air Quality Tracker 🍃

This project automatically crawls and visualizes Taiwan Air Quality Index (AQI) data from the **Ministry of Environment (MOENV) Open Data Platform**. It structures raw monitoring data into a clean, unified JSON payload, calculates statistics by county, updates the project readme table, and serves a premium glassmorphism Single Page Application (SPA) web dashboard for easy browsing.

The tracker is designed for automated data version control using **GitHub and PythonAnywhere scheduled tasks**. By committing data updates directly to `data/aqi.json`, your GitHub commit history serves as a long-term historical database.

---

## 📂 Project Directory Structure

*   `aqi_tracker.py` - Core Python CLI (handles fetching, parsing, updating README, and hosts local HTTP server).
*   `aqi_crawler_pa.py` - Lightweight headless Python crawler designed for periodic runs on **PythonAnywhere**.
*   `config.json` - Shared configurations (containing API Key, output directory, and local server port settings).
*   `index.html` - Web dashboard main SPA structure.
*   `style.css` - Glassmorphism stylesheet featuring a premium dark theme and responsive layout.
*   `app.js` - Dashboard application logic (JSON parsing, live filtering, and rendering chemical pollutants and wind compass).
*   `run_tracker.bat` - Windows launcher script providing a quick interactive console menu.
*   `run_pa_test.bat` - Windows launcher to test the PythonAnywhere crawler locally.
*   `git_sync.sh` - Linux Shell automation script to crawl and push updates to GitHub.
*   `data/` - Created data directory:
    *   `aqi.json` - Unified data package containing current air quality status across all stations in Taiwan.
    *   `stats.json` - Overall statistics and averages by county.
    *   `counties/` - Folder containing separate JSON files for each of Taiwan's 22 counties.

---

## 📊 Live Air Quality Report

<!-- AQI_START -->

**⏰ Last Updated (Taipei Time)**: `2026-07-12 06:09:10`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `35.2` (良好)
- **🟢 Cleanest Location**: 臺中市大里 (AQI: `0`)
- **🔴 Most Polluted Location**: 屏東縣屏東（枋山） (AQI: `109`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 大里 | 臺中市 | `0` | 🟢  |  |  |
| 基隆 | 基隆市 | `13` | 🟢 良好 | 4 | 12 |
| 汐止 | 新北市 | `14` | 🟢 良好 | 5 | 12 |
| 古亭 | 臺北市 | `15` | 🟢 良好 | 0 | 17 |
| 埔里 | 南投縣 | `15` | 🟢 良好 | 0 | 15 |
| 士林 | 臺北市 | `16` | 🟢 良好 | 1 | 13 |
| 土城 | 新北市 | `17` | 🟢 良好 | 2 | 17 |
| 新莊 | 新北市 | `18` | 🟢 良好 | 5 | 20 |
| 新店 | 新北市 | `20` | 🟢 良好 | 2 | 20 |
| 桃園 | 桃園市 | `21` | 🟢 良好 | 4 | 9 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 屏東（枋山） | 屏東縣 | `109` | 🟠 對敏感族群不健康 | 懸浮微粒 | 16 |
| 林園 | 高雄市 | `83` | 🟡 普通 | 懸浮微粒 | 17 |
| 金門 | 金門縣 | `64` | 🟡 普通 | 細懸浮微粒 | 12 |
| 前金 | 高雄市 | `59` | 🟡 普通 | 懸浮微粒 | 5 |
| 馬祖 | 連江縣 | `55` | 🟡 普通 | 細懸浮微粒 | 18 |
| 前鎮 | 高雄市 | `55` | 🟡 普通 | 懸浮微粒 | 8 |
| 小港 | 高雄市 | `53` | 🟡 普通 | 懸浮微粒 | 14 |
| 恆春 | 屏東縣 | `51` | 🟡 普通 | 懸浮微粒 | 10 |
| 屏東（琉球） | 屏東縣 | `50` | 🟢 良好 | None | 8 |
| 大寮 | 高雄市 | `50` | 🟢 良好 | None | 15 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 76 | 90.5% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 7 | 8.3% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 1 | 1.2% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 金門縣 | 1 | `64.0` | `64 - 64` | 🟡 普通 |
| 屏東縣 | 5 | `58.0` | `33 - 109` | 🟡 普通 |
| 連江縣 | 1 | `55.0` | `55 - 55` | 🟡 普通 |
| 高雄市 | 12 | `50.8` | `30 - 83` | 🟡 普通 |
| 澎湖縣 | 1 | `47.0` | `47 - 47` | 🟢 良好 |
| 臺南市 | 5 | `45.0` | `37 - 48` | 🟢 良好 |
| 嘉義縣 | 2 | `38.0` | `38 - 38` | 🟢 良好 |
| 彰化縣 | 5 | `36.8` | `34 - 38` | 🟢 良好 |
| 臺東縣 | 2 | `35.5` | `33 - 38` | 🟢 良好 |
| 嘉義市 | 1 | `35.0` | `35 - 35` | 🟢 良好 |
| 雲林縣 | 4 | `34.2` | `32 - 38` | 🟢 良好 |
| 花蓮縣 | 1 | `33.0` | `33 - 33` | 🟢 良好 |
| 宜蘭縣 | 2 | `32.5` | `22 - 43` | 🟢 良好 |
| 苗栗縣 | 3 | `30.7` | `30 - 31` | 🟢 良好 |
| 新竹市 | 1 | `30.0` | `30 - 30` | 🟢 良好 |
| 桃園市 | 6 | `28.0` | `21 - 39` | 🟢 良好 |
| 新竹縣 | 2 | `27.5` | `26 - 29` | 🟢 良好 |
| 臺北市 | 7 | `25.0` | `15 - 38` | 🟢 良好 |
| 新北市 | 12 | `24.8` | `14 - 45` | 🟢 良好 |
| 南投縣 | 4 | `24.2` | `15 - 29` | 🟢 良好 |
| 臺中市 | 6 | `22.8` | `0 - 32` | 🟢 良好 |
| 基隆市 | 1 | `13.0` | `13 - 13` | 🟢 良好 |

<!-- STATS_END -->

---

## 🛠️ Getting Started & Configurations

### 1. Obtain MOENV Open Data API Key (Optional)
The application includes a public fallback API key that works out of the box. However, it is highly recommended to register for your own key to prevent rate limiting:
1. Go to [Ministry of Environment Open Data Platform](https://data.moenv.gov.tw/).
2. Register an account to receive your **API Key** via email.
3. Replace the `"moenv_api_key"` value in `config.json` with your personal key.

### 2. Usage Instructions

#### For Windows Users:
Simply double-click `run_tracker.bat` to launch the interactive console menu:
*   Option `1`: Fetches the latest air quality data from the API and updates JSON and README.md.
*   Option `2`: Spins up the local glassmorphism web dashboard.
*   Option `3`: Fetches new data and immediately opens the dashboard in your default browser.

#### For Command Line Users:
To fetch data:
```bash
python aqi_tracker.py --fetch
```

To run the local dashboard web server:
```bash
python aqi_tracker.py --serve
```

---

## ☁️ Deployment on PythonAnywhere

To automate crawling and keep your dashboard up to date, you can deploy the scraper as a scheduled task on **PythonAnywhere**:

1. Upload the files: `aqi_crawler_pa.py`, `config.json`, and the shell script `git_sync.sh` to PythonAnywhere.
2. In PythonAnywhere's **Console** tab, set up your git identity and add SSH keys so you can push commits back to your GitHub repository without password prompt.
3. Under the **Tasks** tab, add a new daily/hourly task pointing to your `git_sync.sh` script:
   ```bash
   bash /home/yourusername/taiwan-air-quality/git_sync.sh
   ```
4. The scheduler will execute the crawler, update files in the repo, and automatically push commits to GitHub, updating the dashboard and README tables continuously!
