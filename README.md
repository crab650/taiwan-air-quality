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

**⏰ Last Updated (Taipei Time)**: `2026-07-11 23:09:10`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `34.8` (良好)
- **🟢 Cleanest Location**: 臺中市大里 (AQI: `0`)
- **🔴 Most Polluted Location**: 澎湖縣馬公 (AQI: `118`, Main Pollutant: `臭氧八小時`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 大里 | 臺中市 | `0` | 🟢  |  |  |
| 萬華 | 臺北市 | `19` | 🟢 良好 | 0 | 3 |
| 松山 | 臺北市 | `20` | 🟢 良好 | 1 | 3 |
| 大同 | 臺北市 | `20` | 🟢 良好 | 3 | 0 |
| 中山 | 臺北市 | `20` | 🟢 良好 | 5 | 6 |
| 永和 | 新北市 | `20` | 🟢 良好 | 1 | 2 |
| 菜寮 | 新北市 | `21` | 🟢 良好 | 2 | 0 |
| 新店 | 新北市 | `21` | 🟢 良好 | 1 | 3 |
| 三重 | 新北市 | `21` | 🟢 良好 | 2 | 5 |
| 基隆 | 基隆市 | `21` | 🟢 良好 | 4 | 2 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 馬公 | 澎湖縣 | `118` | 🟠 對敏感族群不健康 | 臭氧八小時 | 10 |
| 屏東（枋山） | 屏東縣 | `97` | 🟡 普通 | 懸浮微粒 | 17 |
| 金門 | 金門縣 | `69` | 🟡 普通 | 細懸浮微粒 | 29 |
| 關山 | 臺東縣 | `63` | 🟡 普通 | 懸浮微粒 | 7 |
| 前金 | 高雄市 | `57` | 🟡 普通 | 懸浮微粒 | 7 |
| 左營 | 高雄市 | `56` | 🟡 普通 | 細懸浮微粒 | 13 |
| 潮州 | 屏東縣 | `54` | 🟡 普通 | 細懸浮微粒 | 11 |
| 屏東（琉球） | 屏東縣 | `52` | 🟡 普通 | 懸浮微粒 | 4 |
| 恆春 | 屏東縣 | `52` | 🟡 普通 | 懸浮微粒 | 11 |
| 前鎮 | 高雄市 | `52` | 🟡 普通 | 細懸浮微粒 | 12 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 71 | 84.5% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 12 | 14.3% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 1 | 1.2% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 澎湖縣 | 1 | `118.0` | `118 - 118` | 🟠 對敏感族群不健康 |
| 金門縣 | 1 | `69.0` | `69 - 69` | 🟡 普通 |
| 屏東縣 | 5 | `56.8` | `29 - 97` | 🟡 普通 |
| 臺東縣 | 2 | `53.0` | `43 - 63` | 🟡 普通 |
| 高雄市 | 12 | `48.8` | `28 - 57` | 🟢 良好 |
| 花蓮縣 | 1 | `45.0` | `45 - 45` | 🟢 良好 |
| 臺南市 | 5 | `41.4` | `35 - 47` | 🟢 良好 |
| 連江縣 | 1 | `37.0` | `37 - 37` | 🟢 良好 |
| 嘉義縣 | 2 | `36.0` | `34 - 38` | 🟢 良好 |
| 雲林縣 | 4 | `35.8` | `30 - 39` | 🟢 良好 |
| 彰化縣 | 5 | `34.0` | `31 - 37` | 🟢 良好 |
| 苗栗縣 | 3 | `29.0` | `27 - 30` | 🟢 良好 |
| 宜蘭縣 | 2 | `27.0` | `22 - 32` | 🟢 良好 |
| 桃園市 | 6 | `26.7` | `22 - 38` | 🟢 良好 |
| 新竹市 | 1 | `25.0` | `25 - 25` | 🟢 良好 |
| 新竹縣 | 2 | `25.0` | `25 - 25` | 🟢 良好 |
| 嘉義市 | 1 | `24.0` | `24 - 24` | 🟢 良好 |
| 南投縣 | 4 | `23.8` | `21 - 26` | 🟢 良好 |
| 新北市 | 12 | `23.8` | `20 - 32` | 🟢 良好 |
| 臺中市 | 6 | `22.2` | `0 - 29` | 🟢 良好 |
| 臺北市 | 7 | `21.1` | `19 - 25` | 🟢 良好 |
| 基隆市 | 1 | `21.0` | `21 - 21` | 🟢 良好 |

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
