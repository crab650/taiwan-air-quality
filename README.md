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

**⏰ Last Updated (Taipei Time)**: `2026-07-10 18:09:14`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `64.3` (普通)
- **🟢 Cleanest Location**: 苗栗縣三義 (AQI: `23`)
- **🔴 Most Polluted Location**: 雲林縣崙背 (AQI: `131`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 三義 | 苗栗縣 | `23` | 🟢 良好 | 3 | 7 |
| 陽明 | 臺北市 | `23` | 🟢 良好 | 0 | 14 |
| 苗栗 | 苗栗縣 | `27` | 🟢 良好 | 6 | 14 |
| 竹東 | 新竹縣 | `30` | 🟢 良好 | 6 | 19 |
| 頭份 | 苗栗縣 | `32` | 🟢 良好 | 5 | 13 |
| 豐原 | 臺中市 | `32` | 🟢 良好 | 6 | 17 |
| 桃園 | 桃園市 | `35` | 🟢 良好 | 7 | 18 |
| 林口 | 新北市 | `37` | 🟢 良好 | 7 | 22 |
| 新竹 | 新竹市 | `38` | 🟢 良好 | 10 | 30 |
| 宜蘭 | 宜蘭縣 | `39` | 🟢 良好 | 7 | 18 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 崙背 | 雲林縣 | `131` | 🟠 對敏感族群不健康 | 懸浮微粒 | 21 |
| 新港 | 嘉義縣 | `112` | 🟠 對敏感族群不健康 | 懸浮微粒 | 13 |
| 關山 | 臺東縣 | `110` | 🟠 對敏感族群不健康 | 懸浮微粒 | 19 |
| 朴子 | 嘉義縣 | `106` | 🟠 對敏感族群不健康 | 懸浮微粒 | 9 |
| 線西 | 彰化縣 | `106` | 🟠 對敏感族群不健康 | 懸浮微粒 | 13 |
| 左營 | 高雄市 | `105` | 🟠 對敏感族群不健康 | 懸浮微粒 | 18 |
| 新營 | 臺南市 | `104` | 🟠 對敏感族群不健康 | 懸浮微粒 | 9 |
| 二林 | 彰化縣 | `102` | 🟠 對敏感族群不健康 | 懸浮微粒 | 7 |
| 臺西 | 雲林縣 | `102` | 🟠 對敏感族群不健康 | 懸浮微粒 | 11 |
| 斗六 | 雲林縣 | `101` | 🟠 對敏感族群不健康 | 懸浮微粒 | 14 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 31 | 36.9% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 43 | 51.2% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 10 | 11.9% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 嘉義縣 | 2 | `109.0` | `106 - 112` | 🟠 對敏感族群不健康 |
| 雲林縣 | 4 | `108.2` | `99 - 131` | 🟠 對敏感族群不健康 |
| 嘉義市 | 1 | `99.0` | `99 - 99` | 🟡 普通 |
| 臺東縣 | 2 | `97.0` | `84 - 110` | 🟡 普通 |
| 臺南市 | 5 | `96.2` | `90 - 104` | 🟡 普通 |
| 高雄市 | 12 | `82.6` | `55 - 105` | 🟡 普通 |
| 彰化縣 | 5 | `80.0` | `60 - 106` | 🟡 普通 |
| 花蓮縣 | 1 | `73.0` | `73 - 73` | 🟡 普通 |
| 屏東縣 | 5 | `69.4` | `48 - 97` | 🟡 普通 |
| 基隆市 | 1 | `59.0` | `59 - 59` | 🟡 普通 |
| 金門縣 | 1 | `58.0` | `58 - 58` | 🟡 普通 |
| 澎湖縣 | 1 | `52.0` | `52 - 52` | 🟡 普通 |
| 臺中市 | 6 | `50.8` | `32 - 65` | 🟡 普通 |
| 宜蘭縣 | 2 | `50.0` | `39 - 61` | 🟢 良好 |
| 南投縣 | 4 | `47.2` | `39 - 56` | 🟢 良好 |
| 新北市 | 12 | `47.2` | `37 - 63` | 🟢 良好 |
| 連江縣 | 1 | `47.0` | `47 - 47` | 🟢 良好 |
| 桃園市 | 6 | `45.5` | `35 - 54` | 🟢 良好 |
| 臺北市 | 7 | `45.1` | `23 - 53` | 🟢 良好 |
| 新竹縣 | 2 | `38.5` | `30 - 47` | 🟢 良好 |
| 新竹市 | 1 | `38.0` | `38 - 38` | 🟢 良好 |
| 苗栗縣 | 3 | `27.3` | `23 - 32` | 🟢 良好 |

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
