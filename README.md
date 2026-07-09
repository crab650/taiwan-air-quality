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

**⏰ Last Updated (Taipei Time)**: `2026-07-09 08:09:08`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `40.8` (良好)
- **🟢 Cleanest Location**: 屏東縣恆春 (AQI: `12`)
- **🔴 Most Polluted Location**: 彰化縣二林 (AQI: `67`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 恆春 | 屏東縣 | `12` | 🟢 良好 | 3 | 14 |
| 關山 | 臺東縣 | `17` | 🟢 良好 | 3 | 14 |
| 臺東 | 臺東縣 | `17` | 🟢 良好 | 5 | 22 |
| 馬公 | 澎湖縣 | `17` | 🟢 良好 | 4 | 6 |
| 臺南 | 臺南市 | `19` | 🟢 良好 | 7 | 13 |
| 林森 | 臺南市 | `21` | 🟢 良好 | 8 | 18 |
| 屏東 | 屏東縣 | `22` | 🟢 良好 | 8 | 15 |
| 美濃 | 高雄市 | `23` | 🟢 良好 | 6 | 24 |
| 前金 | 高雄市 | `23` | 🟢 良好 | 8 | 15 |
| 屏東（琉球） | 屏東縣 | `23` | 🟢 良好 | 6 | 12 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 二林 | 彰化縣 | `67` | 🟡 普通 | 細懸浮微粒 | 24 |
| 冬山 | 宜蘭縣 | `63` | 🟡 普通 | 細懸浮微粒 | 12 |
| 中壢 | 桃園市 | `63` | 🟡 普通 | 細懸浮微粒 | 19 |
| 崙背 | 雲林縣 | `63` | 🟡 普通 | 細懸浮微粒 | 29 |
| 新莊 | 新北市 | `61` | 🟡 普通 | 細懸浮微粒 | 17 |
| 大同 | 臺北市 | `60` | 🟡 普通 | 細懸浮微粒 | 17 |
| 斗六 | 雲林縣 | `60` | 🟡 普通 | 細懸浮微粒 | 19 |
| 汐止 | 新北市 | `58` | 🟡 普通 | 細懸浮微粒 | 12 |
| 三重 | 新北市 | `57` | 🟡 普通 | 細懸浮微粒 | 16 |
| 桃園 | 桃園市 | `57` | 🟡 普通 | 細懸浮微粒 | 12 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 62 | 73.8% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 22 | 26.2% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 宜蘭縣 | 2 | `57.5` | `52 - 63` | 🟡 普通 |
| 雲林縣 | 4 | `53.0` | `44 - 63` | 🟡 普通 |
| 彰化縣 | 5 | `52.6` | `42 - 67` | 🟡 普通 |
| 新北市 | 12 | `52.5` | `44 - 61` | 🟡 普通 |
| 桃園市 | 6 | `49.7` | `31 - 63` | 🟢 良好 |
| 臺北市 | 7 | `49.6` | `33 - 60` | 🟢 良好 |
| 嘉義縣 | 2 | `45.0` | `35 - 55` | 🟢 良好 |
| 金門縣 | 1 | `43.0` | `43 - 43` | 🟢 良好 |
| 嘉義市 | 1 | `42.0` | `42 - 42` | 🟢 良好 |
| 南投縣 | 4 | `41.8` | `30 - 54` | 🟢 良好 |
| 新竹市 | 1 | `41.0` | `41 - 41` | 🟢 良好 |
| 新竹縣 | 2 | `40.0` | `38 - 42` | 🟢 良好 |
| 臺中市 | 6 | `37.2` | `32 - 43` | 🟢 良好 |
| 苗栗縣 | 3 | `34.0` | `31 - 36` | 🟢 良好 |
| 基隆市 | 1 | `33.0` | `33 - 33` | 🟢 良好 |
| 高雄市 | 12 | `31.2` | `23 - 39` | 🟢 良好 |
| 連江縣 | 1 | `31.0` | `31 - 31` | 🟢 良好 |
| 花蓮縣 | 1 | `30.0` | `30 - 30` | 🟢 良好 |
| 臺南市 | 5 | `27.8` | `19 - 39` | 🟢 良好 |
| 屏東縣 | 5 | `22.8` | `12 - 33` | 🟢 良好 |
| 澎湖縣 | 1 | `17.0` | `17 - 17` | 🟢 良好 |
| 臺東縣 | 2 | `17.0` | `17 - 17` | 🟢 良好 |

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
