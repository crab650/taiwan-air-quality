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

**⏰ Last Updated (Taipei Time)**: `2026-07-11 12:09:12`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `36.2` (良好)
- **🟢 Cleanest Location**: 南投縣埔里 (AQI: `13`)
- **🔴 Most Polluted Location**: 屏東縣屏東（枋山） (AQI: `79`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 埔里 | 南投縣 | `13` | 🟢 良好 | 1 | 2 |
| 永和 | 新北市 | `17` | 🟢 良好 | 0 | 2 |
| 宜蘭 | 宜蘭縣 | `17` | 🟢 良好 | 2 | 1 |
| 萬華 | 臺北市 | `18` | 🟢 良好 | 1 | 8 |
| 中山 | 臺北市 | `18` | 🟢 良好 | 6 | 9 |
| 新店 | 新北市 | `18` | 🟢 良好 | 5 | 5 |
| 三重 | 新北市 | `18` | 🟢 良好 | 0 | 7 |
| 南投（鹿谷） | 南投縣 | `18` | 🟢 良好 |  | 0 |
| 美濃 | 高雄市 | `19` | 🟢 良好 | 3 | 11 |
| 三義 | 苗栗縣 | `19` | 🟢 良好 | 0 | 5 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 屏東（枋山） | 屏東縣 | `79` | 🟡 普通 | 細懸浮微粒 | 30 |
| 富貴角 | 新北市 | `71` | 🟡 普通 | 懸浮微粒 | 10 |
| 臺東 | 臺東縣 | `69` | 🟡 普通 | 懸浮微粒 | 9 |
| 金門 | 金門縣 | `67` | 🟡 普通 | 細懸浮微粒 | 13 |
| 陽明 | 臺北市 | `64` | 🟡 普通 | 細懸浮微粒 | 14 |
| 大園 | 桃園市 | `62` | 🟡 普通 | 細懸浮微粒 | 17 |
| 前鎮 | 高雄市 | `60` | 🟡 普通 | 懸浮微粒 | 22 |
| 前金 | 高雄市 | `57` | 🟡 普通 | 懸浮微粒 | 19 |
| 小港 | 高雄市 | `57` | 🟡 普通 | 細懸浮微粒 | 32 |
| 大城 | 彰化縣 | `55` | 🟡 普通 | 懸浮微粒 | 9 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 60 | 71.4% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 24 | 28.6% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 金門縣 | 1 | `67.0` | `67 - 67` | 🟡 普通 |
| 臺東縣 | 2 | `62.0` | `55 - 69` | 🟡 普通 |
| 澎湖縣 | 1 | `55.0` | `55 - 55` | 🟡 普通 |
| 屏東縣 | 5 | `54.6` | `42 - 79` | 🟡 普通 |
| 基隆市 | 1 | `52.0` | `52 - 52` | 🟡 普通 |
| 高雄市 | 12 | `52.0` | `19 - 60` | 🟡 普通 |
| 花蓮縣 | 1 | `51.0` | `51 - 51` | 🟡 普通 |
| 彰化縣 | 5 | `42.4` | `33 - 55` | 🟢 良好 |
| 臺南市 | 5 | `40.8` | `33 - 45` | 🟢 良好 |
| 新竹市 | 1 | `37.0` | `37 - 37` | 🟢 良好 |
| 桃園市 | 6 | `36.2` | `20 - 62` | 🟢 良好 |
| 雲林縣 | 4 | `36.2` | `25 - 48` | 🟢 良好 |
| 嘉義縣 | 2 | `33.0` | `33 - 33` | 🟢 良好 |
| 苗栗縣 | 3 | `27.3` | `19 - 38` | 🟢 良好 |
| 新竹縣 | 2 | `26.5` | `21 - 32` | 🟢 良好 |
| 臺北市 | 7 | `26.1` | `18 - 64` | 🟢 良好 |
| 連江縣 | 1 | `26.0` | `26 - 26` | 🟢 良好 |
| 新北市 | 12 | `25.7` | `17 - 71` | 🟢 良好 |
| 嘉義市 | 1 | `25.0` | `25 - 25` | 🟢 良好 |
| 臺中市 | 6 | `22.3` | `19 - 32` | 🟢 良好 |
| 宜蘭縣 | 2 | `18.5` | `17 - 20` | 🟢 良好 |
| 南投縣 | 4 | `17.5` | `13 - 20` | 🟢 良好 |

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
