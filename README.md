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

**⏰ Last Updated (Taipei Time)**: `2026-07-12 16:09:13`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `35.1` (良好)
- **🟢 Cleanest Location**: 臺中市大里 (AQI: `0`)
- **🔴 Most Polluted Location**: 臺東縣關山 (AQI: `79`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 大里 | 臺中市 | `0` | 🟢 良好 | 0 | 15 |
| 富貴角 | 新北市 | `0` | 🟢  |  |  |
| 竹東 | 新竹縣 | `16` | 🟢 良好 | 2 | 8 |
| 南投（鹿谷） | 南投縣 | `19` | 🟢 良好 | 0 | 9 |
| 埔里 | 南投縣 | `21` | 🟢 良好 | 2 | 7 |
| 美濃 | 高雄市 | `25` | 🟢 良好 | 4 | 14 |
| 新營 | 臺南市 | `25` | 🟢 良好 | 5 | 13 |
| 善化 | 臺南市 | `25` | 🟢 良好 | 5 | 12 |
| 陽明 | 臺北市 | `25` | 🟢 良好 | 4 | 17 |
| 龍潭 | 桃園市 | `25` | 🟢 良好 | 5 | 27 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 關山 | 臺東縣 | `79` | 🟡 普通 | 懸浮微粒 | 7 |
| 林園 | 高雄市 | `76` | 🟡 普通 | 懸浮微粒 | 21 |
| 花蓮 | 花蓮縣 | `70` | 🟡 普通 | 懸浮微粒 | 14 |
| 馬祖 | 連江縣 | `69` | 🟡 普通 | 細懸浮微粒 | 19 |
| 屏東（枋山） | 屏東縣 | `63` | 🟡 普通 | 懸浮微粒 | 5 |
| 古亭 | 臺北市 | `63` | 🟡 普通 | 懸浮微粒 | 5 |
| 金門 | 金門縣 | `56` | 🟡 普通 | 細懸浮微粒 | 16 |
| 宜蘭 | 宜蘭縣 | `55` | 🟡 普通 | 懸浮微粒 | 12 |
| 三重 | 新北市 | `53` | 🟡 普通 | 二氧化氮 | 9 |
| 冬山 | 宜蘭縣 | `51` | 🟡 普通 | 懸浮微粒 | 9 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 73 | 86.9% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 11 | 13.1% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 花蓮縣 | 1 | `70.0` | `70 - 70` | 🟡 普通 |
| 連江縣 | 1 | `69.0` | `69 - 69` | 🟡 普通 |
| 臺東縣 | 2 | `64.5` | `50 - 79` | 🟡 普通 |
| 金門縣 | 1 | `56.0` | `56 - 56` | 🟡 普通 |
| 宜蘭縣 | 2 | `53.0` | `51 - 55` | 🟡 普通 |
| 澎湖縣 | 1 | `47.0` | `47 - 47` | 🟢 良好 |
| 基隆市 | 1 | `42.0` | `42 - 42` | 🟢 良好 |
| 臺北市 | 7 | `41.4` | `25 - 63` | 🟢 良好 |
| 屏東縣 | 5 | `40.6` | `25 - 63` | 🟢 良好 |
| 高雄市 | 12 | `38.6` | `25 - 76` | 🟢 良好 |
| 彰化縣 | 5 | `32.6` | `28 - 37` | 🟢 良好 |
| 新竹市 | 1 | `32.0` | `32 - 32` | 🟢 良好 |
| 桃園市 | 6 | `31.7` | `25 - 38` | 🟢 良好 |
| 新北市 | 12 | `31.6` | `0 - 53` | 🟢 良好 |
| 嘉義縣 | 2 | `30.5` | `30 - 31` | 🟢 良好 |
| 雲林縣 | 4 | `30.0` | `28 - 32` | 🟢 良好 |
| 臺南市 | 5 | `29.4` | `25 - 35` | 🟢 良好 |
| 苗栗縣 | 3 | `27.3` | `27 - 28` | 🟢 良好 |
| 嘉義市 | 1 | `25.0` | `25 - 25` | 🟢 良好 |
| 臺中市 | 6 | `23.2` | `0 - 30` | 🟢 良好 |
| 南投縣 | 4 | `22.8` | `19 - 26` | 🟢 良好 |
| 新竹縣 | 2 | `21.5` | `16 - 27` | 🟢 良好 |

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
