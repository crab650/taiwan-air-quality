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

**⏰ Last Updated (Taipei Time)**: `2026-07-10 12:09:12`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `46.9` (良好)
- **🟢 Cleanest Location**: 臺北市陽明 (AQI: `22`)
- **🔴 Most Polluted Location**: 彰化縣線西 (AQI: `83`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 陽明 | 臺北市 | `22` | 🟢 良好 | 5 | 14 |
| 竹東 | 新竹縣 | `28` | 🟢 良好 | 7 | 18 |
| 林口 | 新北市 | `28` | 🟢 良好 | 6 | 25 |
| 三義 | 苗栗縣 | `30` | 🟢 良好 | 2 | 23 |
| 桃園 | 桃園市 | `30` | 🟢 良好 | 6 | 24 |
| 龍潭 | 桃園市 | `31` | 🟢 良好 | 9 | 23 |
| 淡水 | 新北市 | `32` | 🟢 良好 | 7 | 26 |
| 埔里 | 南投縣 | `34` | 🟢 良好 |  | 23 |
| 關山 | 臺東縣 | `35` | 🟢 良好 | 5 | 20 |
| 平鎮 | 桃園市 | `35` | 🟢 良好 | 7 | 31 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 線西 | 彰化縣 | `83` | 🟡 普通 | 懸浮微粒 | 24 |
| 二林 | 彰化縣 | `82` | 🟡 普通 | 懸浮微粒 | 20 |
| 臺西 | 雲林縣 | `76` | 🟡 普通 | 懸浮微粒 | 9 |
| 臺東 | 臺東縣 | `68` | 🟡 普通 | 懸浮微粒 | 12 |
| 麥寮 | 雲林縣 | `64` | 🟡 普通 | 懸浮微粒 | 7 |
| 崙背 | 雲林縣 | `63` | 🟡 普通 | 懸浮微粒 | 19 |
| 大城 | 彰化縣 | `61` | 🟡 普通 | 懸浮微粒 | 11 |
| 沙鹿 | 臺中市 | `61` | 🟡 普通 | 懸浮微粒 | 15 |
| 西屯 | 臺中市 | `60` | 🟡 普通 | 懸浮微粒 | 7 |
| 金門 | 金門縣 | `60` | 🟡 普通 | 細懸浮微粒 | 19 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 52 | 61.9% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 32 | 38.1% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 彰化縣 | 5 | `67.6` | `55 - 83` | 🟡 普通 |
| 雲林縣 | 4 | `64.0` | `53 - 76` | 🟡 普通 |
| 金門縣 | 1 | `60.0` | `60 - 60` | 🟡 普通 |
| 嘉義縣 | 2 | `53.5` | `53 - 54` | 🟡 普通 |
| 臺中市 | 6 | `52.7` | `39 - 61` | 🟡 普通 |
| 臺東縣 | 2 | `51.5` | `35 - 68` | 🟡 普通 |
| 嘉義市 | 1 | `51.0` | `51 - 51` | 🟡 普通 |
| 高雄市 | 12 | `50.1` | `37 - 58` | 🟡 普通 |
| 基隆市 | 1 | `50.0` | `50 - 50` | 🟢 良好 |
| 南投縣 | 4 | `48.2` | `34 - 57` | 🟢 良好 |
| 臺南市 | 5 | `48.0` | `46 - 51` | 🟢 良好 |
| 連江縣 | 1 | `46.0` | `46 - 46` | 🟢 良好 |
| 屏東縣 | 5 | `45.2` | `36 - 58` | 🟢 良好 |
| 花蓮縣 | 1 | `43.0` | `43 - 43` | 🟢 良好 |
| 新竹市 | 1 | `42.0` | `42 - 42` | 🟢 良好 |
| 新北市 | 12 | `40.5` | `28 - 54` | 🟢 良好 |
| 臺北市 | 7 | `37.6` | `22 - 43` | 🟢 良好 |
| 宜蘭縣 | 2 | `37.5` | `35 - 40` | 🟢 良好 |
| 桃園市 | 6 | `37.3` | `30 - 45` | 🟢 良好 |
| 苗栗縣 | 3 | `36.7` | `30 - 40` | 🟢 良好 |
| 澎湖縣 | 1 | `36.0` | `36 - 36` | 🟢 良好 |
| 新竹縣 | 2 | `35.0` | `28 - 42` | 🟢 良好 |

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
