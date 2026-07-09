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

**⏰ Last Updated (Taipei Time)**: `2026-07-10 03:09:08`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `35.3` (良好)
- **🟢 Cleanest Location**: 臺北市陽明 (AQI: `15`)
- **🔴 Most Polluted Location**: 彰化縣員林 (AQI: `61`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 陽明 | 臺北市 | `15` | 🟢 良好 | 1 | 12 |
| 竹東 | 新竹縣 | `20` | 🟢 良好 | 1 | 11 |
| 板橋 | 新北市 | `20` | 🟢 良好 | 3 | 14 |
| 桃園 | 桃園市 | `22` | 🟢 良好 | 5 | 15 |
| 平鎮 | 桃園市 | `23` | 🟢 良好 | 3 | 13 |
| 林口 | 新北市 | `23` | 🟢 良好 | 6 | 21 |
| 新店 | 新北市 | `23` | 🟢 良好 | 6 | 14 |
| 土城 | 新北市 | `23` | 🟢 良好 | 4 | 20 |
| 三義 | 苗栗縣 | `25` | 🟢 良好 | 5 | 17 |
| 萬華 | 臺北市 | `25` | 🟢 良好 | 7 | 19 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 員林 | 彰化縣 | `61` | 🟡 普通 | 細懸浮微粒 | 12 |
| 竹山 | 南投縣 | `59` | 🟡 普通 | 細懸浮微粒 | 11 |
| 南投 | 南投縣 | `58` | 🟡 普通 | 細懸浮微粒 | 14 |
| 臺灣大道 | 臺中市 | `57` | 🟡 普通 | 二氧化氮 | 17 |
| 金門 | 金門縣 | `51` | 🟡 普通 | 細懸浮微粒 | 11 |
| 彰化 | 彰化縣 | `50` | 🟢 良好 | None | 11 |
| 忠明 | 臺中市 | `50` | 🟢 良好 | None | 14 |
| 沙鹿 | 臺中市 | `50` | 🟢 良好 | None | 12 |
| 斗六 | 雲林縣 | `50` | 🟢 良好 | None | 10 |
| 埔里 | 南投縣 | `49` | 🟢 良好 | None | 15 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 79 | 94.0% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 5 | 6.0% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 南投縣 | 4 | `52.5` | `44 - 59` | 🟡 普通 |
| 金門縣 | 1 | `51.0` | `51 - 51` | 🟡 普通 |
| 臺中市 | 6 | `49.3` | `44 - 57` | 🟢 良好 |
| 彰化縣 | 5 | `46.4` | `38 - 61` | 🟢 良好 |
| 雲林縣 | 4 | `41.0` | `36 - 50` | 🟢 良好 |
| 臺東縣 | 2 | `39.0` | `30 - 48` | 🟢 良好 |
| 高雄市 | 12 | `38.1` | `27 - 48` | 🟢 良好 |
| 嘉義市 | 1 | `37.0` | `37 - 37` | 🟢 良好 |
| 嘉義縣 | 2 | `36.0` | `30 - 42` | 🟢 良好 |
| 臺南市 | 5 | `35.6` | `31 - 44` | 🟢 良好 |
| 屏東縣 | 5 | `34.4` | `27 - 38` | 🟢 良好 |
| 連江縣 | 1 | `32.0` | `32 - 32` | 🟢 良好 |
| 宜蘭縣 | 2 | `31.0` | `27 - 35` | 🟢 良好 |
| 花蓮縣 | 1 | `31.0` | `31 - 31` | 🟢 良好 |
| 苗栗縣 | 3 | `30.7` | `25 - 35` | 🟢 良好 |
| 澎湖縣 | 1 | `30.0` | `30 - 30` | 🟢 良好 |
| 桃園市 | 6 | `28.2` | `22 - 36` | 🟢 良好 |
| 基隆市 | 1 | `27.0` | `27 - 27` | 🟢 良好 |
| 新北市 | 12 | `26.8` | `20 - 38` | 🟢 良好 |
| 臺北市 | 7 | `26.4` | `15 - 33` | 🟢 良好 |
| 新竹市 | 1 | `25.0` | `25 - 25` | 🟢 良好 |
| 新竹縣 | 2 | `23.5` | `20 - 27` | 🟢 良好 |

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
