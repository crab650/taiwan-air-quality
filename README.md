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

**⏰ Last Updated (Taipei Time)**: `2026-07-11 06:09:10`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `40.1` (良好)
- **🟢 Cleanest Location**: 南投縣南投（鹿谷） (AQI: `12`)
- **🔴 Most Polluted Location**: 金門縣金門 (AQI: `81`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 南投（鹿谷） | 南投縣 | `12` | 🟢 良好 | 0 | 0 |
| 宜蘭 | 宜蘭縣 | `16` | 🟢 良好 | 1 | 2 |
| 美濃 | 高雄市 | `17` | 🟢 良好 | 2 | 0 |
| 三義 | 苗栗縣 | `18` | 🟢 良好 | 0 | 9 |
| 埔里 | 南投縣 | `18` | 🟢 良好 | 0 | 5 |
| 豐原 | 臺中市 | `19` | 🟢 良好 | 0 | 11 |
| 大里 | 臺中市 | `20` | 🟢 良好 | 0 | 20 |
| 竹山 | 南投縣 | `20` | 🟢 良好 | 4 | 12 |
| 南投 | 南投縣 | `20` | 🟢 良好 | 5 | 13 |
| 冬山 | 宜蘭縣 | `21` | 🟢 良好 | 2 | 0 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 金門 | 金門縣 | `81` | 🟡 普通 | 細懸浮微粒 | 38 |
| 富貴角 | 新北市 | `80` | 🟡 普通 | 懸浮微粒 | 23 |
| 屏東 | 屏東縣 | `70` | 🟡 普通 | 懸浮微粒 | 7 |
| 臺東 | 臺東縣 | `64` | 🟡 普通 | 懸浮微粒 | 24 |
| 關山 | 臺東縣 | `63` | 🟡 普通 | 懸浮微粒 | 8 |
| 大城 | 彰化縣 | `61` | 🟡 普通 | 懸浮微粒 | 11 |
| 臺西 | 雲林縣 | `60` | 🟡 普通 | 懸浮微粒 | 7 |
| 麥寮 | 雲林縣 | `59` | 🟡 普通 | 懸浮微粒 | 7 |
| 基隆 | 基隆市 | `57` | 🟡 普通 | 懸浮微粒 | 8 |
| 屏東（枋山） | 屏東縣 | `57` | 🟡 普通 | 懸浮微粒 | 11 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 66 | 78.6% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 18 | 21.4% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 金門縣 | 1 | `81.0` | `81 - 81` | 🟡 普通 |
| 臺東縣 | 2 | `63.5` | `63 - 64` | 🟡 普通 |
| 基隆市 | 1 | `57.0` | `57 - 57` | 🟡 普通 |
| 澎湖縣 | 1 | `54.0` | `54 - 54` | 🟡 普通 |
| 雲林縣 | 4 | `51.2` | `33 - 60` | 🟡 普通 |
| 屏東縣 | 5 | `51.0` | `35 - 70` | 🟡 普通 |
| 臺南市 | 5 | `48.8` | `43 - 53` | 🟢 良好 |
| 連江縣 | 1 | `46.0` | `46 - 46` | 🟢 良好 |
| 桃園市 | 6 | `45.7` | `37 - 54` | 🟢 良好 |
| 彰化縣 | 5 | `45.4` | `32 - 61` | 🟢 良好 |
| 嘉義縣 | 2 | `45.0` | `43 - 47` | 🟢 良好 |
| 高雄市 | 12 | `44.3` | `17 - 53` | 🟢 良好 |
| 花蓮縣 | 1 | `43.0` | `43 - 43` | 🟢 良好 |
| 新竹市 | 1 | `42.0` | `42 - 42` | 🟢 良好 |
| 新北市 | 12 | `36.4` | `25 - 80` | 🟢 良好 |
| 嘉義市 | 1 | `33.0` | `33 - 33` | 🟢 良好 |
| 新竹縣 | 2 | `32.5` | `23 - 42` | 🟢 良好 |
| 臺北市 | 7 | `31.7` | `28 - 37` | 🟢 良好 |
| 苗栗縣 | 3 | `27.0` | `18 - 38` | 🟢 良好 |
| 臺中市 | 6 | `24.3` | `19 - 37` | 🟢 良好 |
| 宜蘭縣 | 2 | `18.5` | `16 - 21` | 🟢 良好 |
| 南投縣 | 4 | `17.5` | `12 - 20` | 🟢 良好 |

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
