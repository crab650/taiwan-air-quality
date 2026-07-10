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

**⏰ Last Updated (Taipei Time)**: `2026-07-11 00:09:08`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `50.6` (普通)
- **🟢 Cleanest Location**: 臺北市陽明 (AQI: `16`)
- **🔴 Most Polluted Location**: 雲林縣崙背 (AQI: `105`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 陽明 | 臺北市 | `16` | 🟢 良好 | 0 | 0 |
| 苗栗 | 苗栗縣 | `19` | 🟢 良好 | 2 | 2 |
| 三義 | 苗栗縣 | `23` | 🟢 良好 | 0 | 4 |
| 豐原 | 臺中市 | `25` | 🟢 良好 | 1 | 1 |
| 竹東 | 新竹縣 | `25` | 🟢 良好 | 3 | 1 |
| 南投（鹿谷） | 南投縣 | `25` | 🟢 良好 | 6 | 13 |
| 頭份 | 苗栗縣 | `28` | 🟢 良好 | 2 | 14 |
| 宜蘭 | 宜蘭縣 | `32` | 🟢 良好 | 7 | 8 |
| 大里 | 臺中市 | `33` | 🟢 良好 | 4 | 10 |
| 桃園 | 桃園市 | `33` | 🟢 良好 | 1 | 19 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 崙背 | 雲林縣 | `105` | 🟠 對敏感族群不健康 | 懸浮微粒 | 8 |
| 關山 | 臺東縣 | `83` | 🟡 普通 | 懸浮微粒 | 7 |
| 麥寮 | 雲林縣 | `81` | 🟡 普通 | 懸浮微粒 | 7 |
| 新港 | 嘉義縣 | `77` | 🟡 普通 | 懸浮微粒 | 5 |
| 臺東 | 臺東縣 | `76` | 🟡 普通 | 懸浮微粒 | 13 |
| 臺西 | 雲林縣 | `76` | 🟡 普通 | 懸浮微粒 | 8 |
| 朴子 | 嘉義縣 | `74` | 🟡 普通 | 懸浮微粒 | 6 |
| 安南 | 臺南市 | `72` | 🟡 普通 | 懸浮微粒 | 7 |
| 左營 | 高雄市 | `72` | 🟡 普通 | 懸浮微粒 | 6 |
| 二林 | 彰化縣 | `70` | 🟡 普通 | 懸浮微粒 | 9 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 43 | 51.2% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 40 | 47.6% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 1 | 1.2% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 雲林縣 | 4 | `81.8` | `65 - 105` | 🟡 普通 |
| 臺東縣 | 2 | `79.5` | `76 - 83` | 🟡 普通 |
| 嘉義縣 | 2 | `75.5` | `74 - 77` | 🟡 普通 |
| 臺南市 | 5 | `69.0` | `67 - 72` | 🟡 普通 |
| 嘉義市 | 1 | `61.0` | `61 - 61` | 🟡 普通 |
| 基隆市 | 1 | `61.0` | `61 - 61` | 🟡 普通 |
| 高雄市 | 12 | `59.9` | `45 - 72` | 🟡 普通 |
| 金門縣 | 1 | `58.0` | `58 - 58` | 🟡 普通 |
| 彰化縣 | 5 | `56.6` | `42 - 70` | 🟡 普通 |
| 澎湖縣 | 1 | `53.0` | `53 - 53` | 🟡 普通 |
| 花蓮縣 | 1 | `52.0` | `52 - 52` | 🟡 普通 |
| 連江縣 | 1 | `52.0` | `52 - 52` | 🟡 普通 |
| 屏東縣 | 5 | `47.0` | `40 - 53` | 🟢 良好 |
| 桃園市 | 6 | `44.7` | `33 - 57` | 🟢 良好 |
| 新北市 | 12 | `42.8` | `33 - 70` | 🟢 良好 |
| 臺北市 | 7 | `42.3` | `16 - 60` | 🟢 良好 |
| 新竹市 | 1 | `42.0` | `42 - 42` | 🟢 良好 |
| 臺中市 | 6 | `37.5` | `25 - 47` | 🟢 良好 |
| 新竹縣 | 2 | `36.0` | `25 - 47` | 🟢 良好 |
| 宜蘭縣 | 2 | `35.0` | `32 - 38` | 🟢 良好 |
| 南投縣 | 4 | `33.8` | `25 - 39` | 🟢 良好 |
| 苗栗縣 | 3 | `23.3` | `19 - 28` | 🟢 良好 |

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
