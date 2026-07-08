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

**⏰ Last Updated (Taipei Time)**: `2026-07-09 07:09:11`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `39.8` (良好)
- **🟢 Cleanest Location**: 屏東縣恆春 (AQI: `10`)
- **🔴 Most Polluted Location**: 宜蘭縣冬山 (AQI: `65`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 恆春 | 屏東縣 | `10` | 🟢 良好 | 5 | 7 |
| 臺東 | 臺東縣 | `16` | 🟢 良好 | 2 | 13 |
| 關山 | 臺東縣 | `17` | 🟢 良好 | 3 | 13 |
| 馬公 | 澎湖縣 | `17` | 🟢 良好 | 2 | 4 |
| 林森 | 臺南市 | `18` | 🟢 良好 | 5 | 17 |
| 臺南 | 臺南市 | `19` | 🟢 良好 | 5 | 11 |
| 美濃 | 高雄市 | `20` | 🟢 良好 | 9 | 20 |
| 屏東（枋山） | 屏東縣 | `20` | 🟢 良好 | 8 | 19 |
| 屏東 | 屏東縣 | `22` | 🟢 良好 | 6 | 20 |
| 前鎮 | 高雄市 | `23` | 🟢 良好 | 7 | 22 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 冬山 | 宜蘭縣 | `65` | 🟡 普通 | 細懸浮微粒 | 25 |
| 二林 | 彰化縣 | `64` | 🟡 普通 | 細懸浮微粒 | 20 |
| 新莊 | 新北市 | `60` | 🟡 普通 | 細懸浮微粒 | 16 |
| 汐止 | 新北市 | `59` | 🟡 普通 | 細懸浮微粒 | 14 |
| 中壢 | 桃園市 | `59` | 🟡 普通 | 細懸浮微粒 | 22 |
| 土城 | 新北市 | `58` | 🟡 普通 | 細懸浮微粒 | 17 |
| 大同 | 臺北市 | `58` | 🟡 普通 | 細懸浮微粒 | 17 |
| 斗六 | 雲林縣 | `58` | 🟡 普通 | 細懸浮微粒 | 15 |
| 桃園 | 桃園市 | `57` | 🟡 普通 | 細懸浮微粒 | 17 |
| 三重 | 新北市 | `56` | 🟡 普通 | 細懸浮微粒 | 16 |

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
| 宜蘭縣 | 2 | `59.0` | `53 - 65` | 🟡 普通 |
| 新北市 | 12 | `52.5` | `44 - 60` | 🟡 普通 |
| 彰化縣 | 5 | `51.8` | `44 - 64` | 🟡 普通 |
| 雲林縣 | 4 | `51.8` | `44 - 58` | 🟡 普通 |
| 臺北市 | 7 | `49.6` | `36 - 58` | 🟢 良好 |
| 桃園市 | 6 | `48.5` | `29 - 59` | 🟢 良好 |
| 南投縣 | 4 | `42.0` | `32 - 55` | 🟢 良好 |
| 新竹縣 | 2 | `39.5` | `39 - 40` | 🟢 良好 |
| 嘉義市 | 1 | `39.0` | `39 - 39` | 🟢 良好 |
| 嘉義縣 | 2 | `38.0` | `28 - 48` | 🟢 良好 |
| 新竹市 | 1 | `38.0` | `38 - 38` | 🟢 良好 |
| 金門縣 | 1 | `38.0` | `38 - 38` | 🟢 良好 |
| 臺中市 | 6 | `36.0` | `32 - 39` | 🟢 良好 |
| 苗栗縣 | 3 | `33.7` | `28 - 37` | 🟢 良好 |
| 基隆市 | 1 | `32.0` | `32 - 32` | 🟢 良好 |
| 高雄市 | 12 | `29.6` | `20 - 36` | 🟢 良好 |
| 花蓮縣 | 1 | `28.0` | `28 - 28` | 🟢 良好 |
| 臺南市 | 5 | `27.0` | `18 - 39` | 🟢 良好 |
| 連江縣 | 1 | `27.0` | `27 - 27` | 🟢 良好 |
| 屏東縣 | 5 | `21.4` | `10 - 32` | 🟢 良好 |
| 澎湖縣 | 1 | `17.0` | `17 - 17` | 🟢 良好 |
| 臺東縣 | 2 | `16.5` | `16 - 17` | 🟢 良好 |

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
