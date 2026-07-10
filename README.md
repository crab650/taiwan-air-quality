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

**⏰ Last Updated (Taipei Time)**: `2026-07-10 16:09:11`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `61.6` (普通)
- **🟢 Cleanest Location**: 新竹縣竹東 (AQI: `27`)
- **🔴 Most Polluted Location**: 雲林縣崙背 (AQI: `123`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 竹東 | 新竹縣 | `27` | 🟢 良好 | 8 | 18 |
| 陽明 | 臺北市 | `28` | 🟢 良好 | 5 | 12 |
| 苗栗 | 苗栗縣 | `31` | 🟢 良好 | 7 | 12 |
| 頭份 | 苗栗縣 | `35` | 🟢 良好 | 3 | 23 |
| 三義 | 苗栗縣 | `35` | 🟢 良好 | 4 | 14 |
| 豐原 | 臺中市 | `35` | 🟢 良好 | 7 | 13 |
| 新竹 | 新竹市 | `35` | 🟢 良好 | 6 | 14 |
| 林口 | 新北市 | `35` | 🟢 良好 | 13 | 26 |
| 桃園 | 桃園市 | `37` | 🟢 良好 | 7 | 25 |
| 龍潭 | 桃園市 | `39` | 🟢 良好 | 9 | 21 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 崙背 | 雲林縣 | `123` | 🟠 對敏感族群不健康 | 懸浮微粒 | 25 |
| 新港 | 嘉義縣 | `113` | 🟠 對敏感族群不健康 | 懸浮微粒 | 16 |
| 二林 | 彰化縣 | `109` | 🟠 對敏感族群不健康 | 懸浮微粒 | 10 |
| 線西 | 彰化縣 | `107` | 🟠 對敏感族群不健康 | 懸浮微粒 | 16 |
| 臺西 | 雲林縣 | `105` | 🟠 對敏感族群不健康 | 懸浮微粒 | 9 |
| 朴子 | 嘉義縣 | `103` | 🟠 對敏感族群不健康 | 懸浮微粒 | 11 |
| 左營 | 高雄市 | `103` | 🟠 對敏感族群不健康 | 懸浮微粒 | 17 |
| 麥寮 | 雲林縣 | `101` | 🟠 對敏感族群不健康 | 懸浮微粒 | 11 |
| 新營 | 臺南市 | `94` | 🟡 普通 | 懸浮微粒 | 16 |
| 花蓮 | 花蓮縣 | `88` | 🟡 普通 | 懸浮微粒 | 14 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 35 | 41.7% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 41 | 48.8% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 8 | 9.5% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 嘉義縣 | 2 | `108.0` | `103 - 113` | 🟠 對敏感族群不健康 |
| 雲林縣 | 4 | `104.0` | `87 - 123` | 🟠 對敏感族群不健康 |
| 花蓮縣 | 1 | `88.0` | `88 - 88` | 🟡 普通 |
| 彰化縣 | 5 | `83.2` | `62 - 109` | 🟡 普通 |
| 嘉義市 | 1 | `83.0` | `83 - 83` | 🟡 普通 |
| 臺南市 | 5 | `81.2` | `74 - 94` | 🟡 普通 |
| 臺東縣 | 2 | `81.0` | `80 - 82` | 🟡 普通 |
| 高雄市 | 12 | `73.7` | `55 - 103` | 🟡 普通 |
| 屏東縣 | 5 | `65.4` | `51 - 84` | 🟡 普通 |
| 臺中市 | 6 | `58.8` | `35 - 80` | 🟡 普通 |
| 基隆市 | 1 | `57.0` | `57 - 57` | 🟡 普通 |
| 金門縣 | 1 | `54.0` | `54 - 54` | 🟡 普通 |
| 宜蘭縣 | 2 | `52.5` | `45 - 60` | 🟡 普通 |
| 南投縣 | 4 | `51.5` | `42 - 61` | 🟡 普通 |
| 澎湖縣 | 1 | `46.0` | `46 - 46` | 🟢 良好 |
| 新北市 | 12 | `44.9` | `35 - 60` | 🟢 良好 |
| 桃園市 | 6 | `44.3` | `37 - 53` | 🟢 良好 |
| 臺北市 | 7 | `43.3` | `28 - 50` | 🟢 良好 |
| 連江縣 | 1 | `42.0` | `42 - 42` | 🟢 良好 |
| 新竹縣 | 2 | `36.0` | `27 - 45` | 🟢 良好 |
| 新竹市 | 1 | `35.0` | `35 - 35` | 🟢 良好 |
| 苗栗縣 | 3 | `33.7` | `31 - 35` | 🟢 良好 |

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
