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

**⏰ Last Updated (Taipei Time)**: `2026-07-10 08:09:08`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `38.8` (良好)
- **🟢 Cleanest Location**: 臺北市陽明 (AQI: `20`)
- **🔴 Most Polluted Location**: 金門縣金門 (AQI: `63`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 陽明 | 臺北市 | `20` | 🟢 良好 | 4 | 16 |
| 竹東 | 新竹縣 | `20` | 🟢 良好 | 9 | 15 |
| 關山 | 臺東縣 | `24` | 🟢 良好 | 3 | 10 |
| 林口 | 新北市 | `24` | 🟢 良好 | 7 | 13 |
| 花蓮 | 花蓮縣 | `26` | 🟢 良好 | 4 | 24 |
| 淡水 | 新北市 | `27` | 🟢 良好 | 8 | 14 |
| 新店 | 新北市 | `27` | 🟢 良好 | 7 | 20 |
| 冬山 | 宜蘭縣 | `27` | 🟢 良好 | 7 | 23 |
| 桃園 | 桃園市 | `28` | 🟢 良好 | 5 | 20 |
| 土城 | 新北市 | `28` | 🟢 良好 | 7 | 18 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 金門 | 金門縣 | `63` | 🟡 普通 | 細懸浮微粒 | 22 |
| 竹山 | 南投縣 | `60` | 🟡 普通 | 細懸浮微粒 | 14 |
| 員林 | 彰化縣 | `59` | 🟡 普通 | 細懸浮微粒 | 19 |
| 大城 | 彰化縣 | `57` | 🟡 普通 | 懸浮微粒 | 18 |
| 南投 | 南投縣 | `56` | 🟡 普通 | 細懸浮微粒 | 14 |
| 大里 | 臺中市 | `56` | 🟡 普通 | 細懸浮微粒 | 14 |
| 二林 | 彰化縣 | `54` | 🟡 普通 | 懸浮微粒 | 16 |
| 忠明 | 臺中市 | `53` | 🟡 普通 | 細懸浮微粒 | 11 |
| 臺灣大道 | 臺中市 | `53` | 🟡 普通 | 懸浮微粒 | 12 |
| 沙鹿 | 臺中市 | `52` | 🟡 普通 | 細懸浮微粒 | 17 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 71 | 84.5% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 13 | 15.5% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 金門縣 | 1 | `63.0` | `63 - 63` | 🟡 普通 |
| 彰化縣 | 5 | `53.6` | `47 - 59` | 🟡 普通 |
| 臺中市 | 6 | `51.0` | `45 - 56` | 🟡 普通 |
| 雲林縣 | 4 | `49.8` | `47 - 51` | 🟢 良好 |
| 南投縣 | 4 | `49.5` | `34 - 60` | 🟢 良好 |
| 嘉義縣 | 2 | `44.0` | `40 - 48` | 🟢 良好 |
| 連江縣 | 1 | `40.0` | `40 - 40` | 🟢 良好 |
| 臺南市 | 5 | `38.4` | `33 - 46` | 🟢 良好 |
| 高雄市 | 12 | `38.0` | `32 - 47` | 🟢 良好 |
| 屏東縣 | 5 | `37.4` | `29 - 45` | 🟢 良好 |
| 嘉義市 | 1 | `37.0` | `37 - 37` | 🟢 良好 |
| 基隆市 | 1 | `37.0` | `37 - 37` | 🟢 良好 |
| 桃園市 | 6 | `34.5` | `28 - 43` | 🟢 良好 |
| 臺東縣 | 2 | `33.5` | `24 - 43` | 🟢 良好 |
| 新北市 | 12 | `33.1` | `24 - 50` | 🟢 良好 |
| 新竹市 | 1 | `33.0` | `33 - 33` | 🟢 良好 |
| 苗栗縣 | 3 | `32.3` | `29 - 36` | 🟢 良好 |
| 臺北市 | 7 | `32.1` | `20 - 37` | 🟢 良好 |
| 宜蘭縣 | 2 | `29.5` | `27 - 32` | 🟢 良好 |
| 澎湖縣 | 1 | `29.0` | `29 - 29` | 🟢 良好 |
| 新竹縣 | 2 | `26.0` | `20 - 32` | 🟢 良好 |
| 花蓮縣 | 1 | `26.0` | `26 - 26` | 🟢 良好 |

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
