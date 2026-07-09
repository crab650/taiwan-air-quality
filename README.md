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

**⏰ Last Updated (Taipei Time)**: `2026-07-09 14:09:11`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `37.9` (良好)
- **🟢 Cleanest Location**: 屏東縣屏東（琉球） (AQI: `19`)
- **🔴 Most Polluted Location**: 桃園市中壢 (AQI: `66`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 屏東（琉球） | 屏東縣 | `19` | 🟢 良好 | 3 | 8 |
| 麥寮 | 雲林縣 | `22` | 🟢 良好 | 1 | 13 |
| 前金 | 高雄市 | `23` | 🟢 良好 | 4 | 13 |
| 關山 | 臺東縣 | `23` | 🟢 良好 | 4 | 21 |
| 安南 | 臺南市 | `23` | 🟢 良好 | 5 | 20 |
| 陽明 | 臺北市 | `23` | 🟢 良好 | 6 |  |
| 恆春 | 屏東縣 | `23` | 🟢 良好 | 7 | 17 |
| 苗栗 | 苗栗縣 | `24` | 🟢 良好 | 6 | 13 |
| 三義 | 苗栗縣 | `24` | 🟢 良好 | 4 | 8 |
| 花蓮 | 花蓮縣 | `24` | 🟢 良好 | 2 | 10 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 中壢 | 桃園市 | `66` | 🟡 普通 | 細懸浮微粒 | 23 |
| 新北（樹林） | 新北市 | `57` | 🟡 普通 | 細懸浮微粒 | 10 |
| 新莊 | 新北市 | `57` | 🟡 普通 | 懸浮微粒 | 11 |
| 平鎮 | 桃園市 | `57` | 🟡 普通 | 細懸浮微粒 | 12 |
| 金門 | 金門縣 | `56` | 🟡 普通 | 細懸浮微粒 | 13 |
| 斗六 | 雲林縣 | `56` | 🟡 普通 | 細懸浮微粒 | 13 |
| 板橋 | 新北市 | `54` | 🟡 普通 | 細懸浮微粒 | 8 |
| 龍潭 | 桃園市 | `53` | 🟡 普通 | 細懸浮微粒 | 11 |
| 大同 | 臺北市 | `52` | 🟡 普通 | 細懸浮微粒 | 7 |
| 桃園 | 桃園市 | `51` | 🟡 普通 | 細懸浮微粒 | 8 |

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
| 金門縣 | 1 | `56.0` | `56 - 56` | 🟡 普通 |
| 桃園市 | 6 | `49.8` | `32 - 66` | 🟢 良好 |
| 連江縣 | 1 | `49.0` | `49 - 49` | 🟢 良好 |
| 南投縣 | 4 | `45.0` | `38 - 48` | 🟢 良好 |
| 新北市 | 12 | `45.0` | `28 - 57` | 🟢 良好 |
| 嘉義市 | 1 | `40.0` | `40 - 40` | 🟢 良好 |
| 新竹市 | 1 | `40.0` | `40 - 40` | 🟢 良好 |
| 臺北市 | 7 | `39.7` | `23 - 52` | 🟢 良好 |
| 高雄市 | 12 | `36.7` | `23 - 51` | 🟢 良好 |
| 雲林縣 | 4 | `36.5` | `22 - 56` | 🟢 良好 |
| 彰化縣 | 5 | `36.0` | `27 - 42` | 🟢 良好 |
| 臺中市 | 6 | `36.0` | `28 - 44` | 🟢 良好 |
| 嘉義縣 | 2 | `35.5` | `25 - 46` | 🟢 良好 |
| 新竹縣 | 2 | `34.5` | `33 - 36` | 🟢 良好 |
| 宜蘭縣 | 2 | `31.5` | `31 - 32` | 🟢 良好 |
| 屏東縣 | 5 | `31.2` | `19 - 50` | 🟢 良好 |
| 臺南市 | 5 | `30.2` | `23 - 35` | 🟢 良好 |
| 基隆市 | 1 | `29.0` | `29 - 29` | 🟢 良好 |
| 臺東縣 | 2 | `27.5` | `23 - 32` | 🟢 良好 |
| 苗栗縣 | 3 | `25.0` | `24 - 27` | 🟢 良好 |
| 澎湖縣 | 1 | `24.0` | `24 - 24` | 🟢 良好 |
| 花蓮縣 | 1 | `24.0` | `24 - 24` | 🟢 良好 |

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
