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

**⏰ Last Updated (Taipei Time)**: `2026-07-11 02:09:09`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `45.3` (良好)
- **🟢 Cleanest Location**: 新北市富貴角 (AQI: `0`)
- **🔴 Most Polluted Location**: 雲林縣崙背 (AQI: `89`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 富貴角 | 新北市 | `0` | 🟢 普通 | 16 | 60 |
| 三義 | 苗栗縣 | `15` | 🟢 良好 | 0 | 8 |
| 陽明 | 臺北市 | `17` | 🟢 良好 | 4 | 2 |
| 豐原 | 臺中市 | `17` | 🟢 良好 | 0 | 1 |
| 竹東 | 新竹縣 | `17` | 🟢 良好 | 1 | 4 |
| 苗栗 | 苗栗縣 | `19` | 🟢 良好 | 6 | 14 |
| 南投（鹿谷） | 南投縣 | `20` | 🟢 良好 | 1 | 2 |
| 忠明 | 臺中市 | `22` | 🟢 良好 | 3 | 8 |
| 西屯 | 臺中市 | `23` | 🟢 良好 | 0 | 4 |
| 臺灣大道 | 臺中市 | `23` | 🟢 良好 | 0 | 7 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 崙背 | 雲林縣 | `89` | 🟡 普通 | 懸浮微粒 | 4 |
| 關山 | 臺東縣 | `86` | 🟡 普通 | 懸浮微粒 | 8 |
| 臺東 | 臺東縣 | `73` | 🟡 普通 | 懸浮微粒 | 5 |
| 楠梓 | 高雄市 | `69` | 🟡 普通 | 懸浮微粒 | 8 |
| 安南 | 臺南市 | `65` | 🟡 普通 | 懸浮微粒 | 9 |
| 臺西 | 雲林縣 | `65` | 🟡 普通 | 懸浮微粒 | 11 |
| 前金 | 高雄市 | `65` | 🟡 普通 | 懸浮微粒 | 4 |
| 左營 | 高雄市 | `65` | 🟡 普通 | 懸浮微粒 | 4 |
| 朴子 | 嘉義縣 | `63` | 🟡 普通 | 懸浮微粒 | 5 |
| 麥寮 | 雲林縣 | `63` | 🟡 普通 | 懸浮微粒 | 5 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 47 | 56.0% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 37 | 44.0% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 臺東縣 | 2 | `79.5` | `73 - 86` | 🟡 普通 |
| 雲林縣 | 4 | `69.0` | `59 - 89` | 🟡 普通 |
| 嘉義縣 | 2 | `62.5` | `62 - 63` | 🟡 普通 |
| 臺南市 | 5 | `61.8` | `59 - 65` | 🟡 普通 |
| 金門縣 | 1 | `61.0` | `61 - 61` | 🟡 普通 |
| 基隆市 | 1 | `59.0` | `59 - 59` | 🟡 普通 |
| 高雄市 | 12 | `58.8` | `45 - 69` | 🟡 普通 |
| 澎湖縣 | 1 | `55.0` | `55 - 55` | 🟡 普通 |
| 連江縣 | 1 | `53.0` | `53 - 53` | 🟡 普通 |
| 嘉義市 | 1 | `52.0` | `52 - 52` | 🟡 普通 |
| 屏東縣 | 5 | `48.6` | `39 - 57` | 🟢 良好 |
| 彰化縣 | 5 | `45.8` | `30 - 62` | 🟢 良好 |
| 新竹市 | 1 | `45.0` | `45 - 45` | 🟢 良好 |
| 桃園市 | 6 | `43.8` | `30 - 59` | 🟢 良好 |
| 花蓮縣 | 1 | `43.0` | `43 - 43` | 🟢 良好 |
| 臺北市 | 7 | `40.0` | `17 - 61` | 🟢 良好 |
| 新北市 | 12 | `35.1` | `0 - 52` | 🟢 良好 |
| 新竹縣 | 2 | `30.0` | `17 - 43` | 🟢 良好 |
| 宜蘭縣 | 2 | `29.5` | `27 - 32` | 🟢 良好 |
| 南投縣 | 4 | `26.5` | `20 - 32` | 🟢 良好 |
| 臺中市 | 6 | `22.5` | `17 - 27` | 🟢 良好 |
| 苗栗縣 | 3 | `22.0` | `15 - 32` | 🟢 良好 |

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
