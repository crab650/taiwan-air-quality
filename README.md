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

**⏰ Last Updated (Taipei Time)**: `2026-07-05 13:09:13`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `26.5` (良好)
- **🟢 Cleanest Location**: 臺東縣臺東 (AQI: `12`)
- **🔴 Most Polluted Location**: 新北市永和 (AQI: `52`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 臺東 | 臺東縣 | `12` | 🟢 良好 | 4 | 6 |
| 恆春 | 屏東縣 | `12` | 🟢 良好 | 0 | 2 |
| 屏東（琉球） | 屏東縣 | `12` | 🟢 良好 | 1 | 5 |
| 關山 | 臺東縣 | `13` | 🟢 良好 | 0 | 4 |
| 花蓮 | 花蓮縣 | `14` | 🟢 良好 | 3 | 7 |
| 左營 | 高雄市 | `15` | 🟢 良好 | 0 | 5 |
| 南投（鹿谷） | 南投縣 | `16` | 🟢 良好 | 6 | 10 |
| 埔里 | 南投縣 | `17` | 🟢 良好 | 6 | 9 |
| 大寮 | 高雄市 | `18` | 🟢 良好 | 0 | 8 |
| 屏東 | 屏東縣 | `19` | 🟢 良好 | 6 | 9 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 永和 | 新北市 | `52` | 🟡 普通 | 懸浮微粒 | 8 |
| 屏東（枋山） | 屏東縣 | `45` | 🟢 良好 | None | 10 |
| 三重 | 新北市 | `40` | 🟢 良好 | None | 11 |
| 員林 | 彰化縣 | `39` | 🟢 良好 | None | 12 |
| 中山 | 臺北市 | `38` | 🟢 良好 | None | 11 |
| 林園 | 高雄市 | `38` | 🟢 良好 | None | 1 |
| 松山 | 臺北市 | `37` | 🟢 良好 | None | 16 |
| 富貴角 | 新北市 | `35` | 🟢 良好 | None | 9 |
| 汐止 | 新北市 | `35` | 🟢 良好 | None | 8 |
| 新莊 | 新北市 | `34` | 🟢 良好 | None | 9 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 83 | 98.8% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 1 | 1.2% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 新北市 | 12 | `32.7` | `20 - 52` | 🟢 良好 |
| 基隆市 | 1 | `32.0` | `32 - 32` | 🟢 良好 |
| 臺北市 | 7 | `31.6` | `23 - 38` | 🟢 良好 |
| 彰化縣 | 5 | `31.2` | `27 - 39` | 🟢 良好 |
| 新竹市 | 1 | `29.0` | `29 - 29` | 🟢 良好 |
| 宜蘭縣 | 2 | `28.5` | `26 - 31` | 🟢 良好 |
| 連江縣 | 1 | `28.0` | `28 - 28` | 🟢 良好 |
| 雲林縣 | 4 | `28.0` | `25 - 33` | 🟢 良好 |
| 臺中市 | 6 | `27.7` | `23 - 31` | 🟢 良好 |
| 桃園市 | 6 | `26.5` | `20 - 33` | 🟢 良好 |
| 苗栗縣 | 3 | `26.3` | `23 - 30` | 🟢 良好 |
| 新竹縣 | 2 | `24.5` | `24 - 25` | 🟢 良好 |
| 臺南市 | 5 | `24.4` | `22 - 28` | 🟢 良好 |
| 金門縣 | 1 | `24.0` | `24 - 24` | 🟢 良好 |
| 嘉義市 | 1 | `23.0` | `23 - 23` | 🟢 良好 |
| 嘉義縣 | 2 | `23.0` | `23 - 23` | 🟢 良好 |
| 高雄市 | 12 | `22.9` | `15 - 38` | 🟢 良好 |
| 南投縣 | 4 | `22.0` | `16 - 28` | 🟢 良好 |
| 屏東縣 | 5 | `22.0` | `12 - 45` | 🟢 良好 |
| 澎湖縣 | 1 | `20.0` | `20 - 20` | 🟢 良好 |
| 花蓮縣 | 1 | `14.0` | `14 - 14` | 🟢 良好 |
| 臺東縣 | 2 | `12.5` | `12 - 13` | 🟢 良好 |

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
