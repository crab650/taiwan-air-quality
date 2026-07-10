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

**⏰ Last Updated (Taipei Time)**: `2026-07-10 22:09:12`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `54.9` (普通)
- **🟢 Cleanest Location**: 臺北市陽明 (AQI: `20`)
- **🔴 Most Polluted Location**: 雲林縣崙背 (AQI: `111`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 陽明 | 臺北市 | `20` | 🟢 良好 | 3 | 5 |
| 苗栗 | 苗栗縣 | `28` | 🟢 良好 | 3 | 5 |
| 三義 | 苗栗縣 | `28` | 🟢 良好 | 4 | 21 |
| 南投（鹿谷） | 南投縣 | `29` | 🟢 良好 | 3 | 17 |
| 豐原 | 臺中市 | `30` | 🟢 良好 | 5 | 21 |
| 宜蘭 | 宜蘭縣 | `31` | 🟢 良好 | 8 | 18 |
| 竹東 | 新竹縣 | `33` | 🟢 良好 | 6 | 17 |
| 埔里 | 南投縣 | `33` | 🟢 良好 | 7 | 22 |
| 恆春 | 屏東縣 | `36` | 🟢 良好 | 9 | 15 |
| 頭份 | 苗栗縣 | `37` | 🟢 良好 | 3 | 13 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 崙背 | 雲林縣 | `111` | 🟠 對敏感族群不健康 | 懸浮微粒 | 10 |
| 關山 | 臺東縣 | `91` | 🟡 普通 | 懸浮微粒 | 9 |
| 麥寮 | 雲林縣 | `90` | 🟡 普通 | 懸浮微粒 | 16 |
| 左營 | 高雄市 | `86` | 🟡 普通 | 懸浮微粒 | 8 |
| 臺西 | 雲林縣 | `83` | 🟡 普通 | 懸浮微粒 | 12 |
| 新港 | 嘉義縣 | `82` | 🟡 普通 | 懸浮微粒 | 11 |
| 斗六 | 雲林縣 | `82` | 🟡 普通 | 懸浮微粒 | 9 |
| 朴子 | 嘉義縣 | `80` | 🟡 普通 | 懸浮微粒 | 8 |
| 二林 | 彰化縣 | `79` | 🟡 普通 | 懸浮微粒 | 10 |
| 線西 | 彰化縣 | `79` | 🟡 普通 | 懸浮微粒 | 11 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 39 | 46.4% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 44 | 52.4% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 1 | 1.2% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 雲林縣 | 4 | `91.5` | `82 - 111` | 🟡 普通 |
| 臺東縣 | 2 | `83.5` | `76 - 91` | 🟡 普通 |
| 嘉義縣 | 2 | `81.0` | `80 - 82` | 🟡 普通 |
| 臺南市 | 5 | `75.8` | `72 - 78` | 🟡 普通 |
| 嘉義市 | 1 | `68.0` | `68 - 68` | 🟡 普通 |
| 高雄市 | 12 | `66.9` | `46 - 86` | 🟡 普通 |
| 彰化縣 | 5 | `64.2` | `47 - 79` | 🟡 普通 |
| 基隆市 | 1 | `61.0` | `61 - 61` | 🟡 普通 |
| 花蓮縣 | 1 | `59.0` | `59 - 59` | 🟡 普通 |
| 澎湖縣 | 1 | `55.0` | `55 - 55` | 🟡 普通 |
| 連江縣 | 1 | `55.0` | `55 - 55` | 🟡 普通 |
| 金門縣 | 1 | `55.0` | `55 - 55` | 🟡 普通 |
| 新北市 | 12 | `46.2` | `37 - 69` | 🟢 良好 |
| 桃園市 | 6 | `45.3` | `37 - 53` | 🟢 良好 |
| 屏東縣 | 5 | `44.6` | `36 - 54` | 🟢 良好 |
| 臺北市 | 7 | `44.3` | `20 - 57` | 🟢 良好 |
| 臺中市 | 6 | `44.2` | `30 - 52` | 🟢 良好 |
| 新竹縣 | 2 | `39.0` | `33 - 45` | 🟢 良好 |
| 南投縣 | 4 | `38.2` | `29 - 48` | 🟢 良好 |
| 宜蘭縣 | 2 | `38.0` | `31 - 45` | 🟢 良好 |
| 新竹市 | 1 | `38.0` | `38 - 38` | 🟢 良好 |
| 苗栗縣 | 3 | `31.0` | `28 - 37` | 🟢 良好 |

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
