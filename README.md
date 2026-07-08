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

**⏰ Last Updated (Taipei Time)**: `2026-07-09 02:09:12`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `34.2` (良好)
- **🟢 Cleanest Location**: 臺東縣關山 (AQI: `13`)
- **🔴 Most Polluted Location**: 臺北市大同 (AQI: `59`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 關山 | 臺東縣 | `13` | 🟢 良好 | 9 | 8 |
| 臺東 | 臺東縣 | `13` | 🟢 良好 | 3 | 8 |
| 恆春 | 屏東縣 | `13` | 🟢 良好 | 0 | 3 |
| 臺南 | 臺南市 | `15` | 🟢 良好 | 4 | 11 |
| 左營 | 高雄市 | `16` | 🟢 良好 | 3 | 8 |
| 屏東（琉球） | 屏東縣 | `16` | 🟢 良好 | 3 | 7 |
| 前鎮 | 高雄市 | `18` | 🟢 良好 | 2 | 13 |
| 前金 | 高雄市 | `18` | 🟢 良好 | 0 | 17 |
| 林森 | 臺南市 | `18` | 🟢 良好 | 7 | 9 |
| 馬公 | 澎湖縣 | `18` | 🟢 良好 | 5 | 7 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 大同 | 臺北市 | `59` | 🟡 普通 | 細懸浮微粒 | 11 |
| 斗六 | 雲林縣 | `59` | 🟡 普通 | 細懸浮微粒 | 20 |
| 二林 | 彰化縣 | `58` | 🟡 普通 | 細懸浮微粒 | 17 |
| 中壢 | 桃園市 | `58` | 🟡 普通 | 細懸浮微粒 | 12 |
| 新北（樹林） | 新北市 | `56` | 🟡 普通 | 細懸浮微粒 | 11 |
| 新莊 | 新北市 | `56` | 🟡 普通 | 細懸浮微粒 | 16 |
| 士林 | 臺北市 | `56` | 🟡 普通 | 細懸浮微粒 | 19 |
| 宜蘭 | 宜蘭縣 | `54` | 🟡 普通 | 細懸浮微粒 | 16 |
| 三重 | 新北市 | `54` | 🟡 普通 | 細懸浮微粒 | 13 |
| 竹山 | 南投縣 | `53` | 🟡 普通 | 細懸浮微粒 | 12 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 67 | 79.8% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 17 | 20.2% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 宜蘭縣 | 2 | `52.5` | `51 - 54` | 🟡 普通 |
| 臺北市 | 7 | `50.1` | `39 - 59` | 🟡 普通 |
| 新北市 | 12 | `49.8` | `40 - 56` | 🟢 良好 |
| 桃園市 | 6 | `41.8` | `28 - 58` | 🟢 良好 |
| 南投縣 | 4 | `41.2` | `35 - 53` | 🟢 良好 |
| 彰化縣 | 5 | `36.4` | `23 - 58` | 🟢 良好 |
| 雲林縣 | 4 | `34.5` | `20 - 59` | 🟢 良好 |
| 基隆市 | 1 | `31.0` | `31 - 31` | 🟢 良好 |
| 臺中市 | 6 | `31.0` | `27 - 34` | 🟢 良好 |
| 嘉義縣 | 2 | `30.5` | `23 - 38` | 🟢 良好 |
| 新竹縣 | 2 | `30.5` | `29 - 32` | 🟢 良好 |
| 連江縣 | 1 | `29.0` | `29 - 29` | 🟢 良好 |
| 苗栗縣 | 3 | `28.3` | `22 - 32` | 🟢 良好 |
| 嘉義市 | 1 | `28.0` | `28 - 28` | 🟢 良好 |
| 新竹市 | 1 | `25.0` | `25 - 25` | 🟢 良好 |
| 高雄市 | 12 | `23.2` | `16 - 28` | 🟢 良好 |
| 金門縣 | 1 | `23.0` | `23 - 23` | 🟢 良好 |
| 屏東縣 | 5 | `21.6` | `13 - 37` | 🟢 良好 |
| 臺南市 | 5 | `20.0` | `15 - 24` | 🟢 良好 |
| 花蓮縣 | 1 | `20.0` | `20 - 20` | 🟢 良好 |
| 澎湖縣 | 1 | `18.0` | `18 - 18` | 🟢 良好 |
| 臺東縣 | 2 | `13.0` | `13 - 13` | 🟢 良好 |

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
