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

**⏰ Last Updated (Taipei Time)**: `2026-07-14 11:09:12`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `31.9` (良好)
- **🟢 Cleanest Location**: 臺東縣關山 (AQI: `15`)
- **🔴 Most Polluted Location**: 高雄市小港 (AQI: `58`, Main Pollutant: `二氧化硫`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 關山 | 臺東縣 | `15` | 🟢 良好 | 1 | 8 |
| 臺東 | 臺東縣 | `18` | 🟢 良好 | 2 | 12 |
| 三義 | 苗栗縣 | `20` | 🟢 良好 | 5 | 17 |
| 花蓮 | 花蓮縣 | `20` | 🟢 良好 | 5 | 14 |
| 新營 | 臺南市 | `20` | 🟢 良好 | 0 | 16 |
| 朴子 | 嘉義縣 | `20` | 🟢 良好 | 3 | 13 |
| 陽明 | 臺北市 | `21` | 🟢 良好 | 6 | 9 |
| 南投（鹿谷） | 南投縣 | `21` | 🟢 良好 |  | 18 |
| 左營 | 高雄市 | `22` | 🟢 良好 | 6 | 5 |
| 崙背 | 雲林縣 | `22` | 🟢 良好 | 3 | 6 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 小港 | 高雄市 | `58` | 🟡 普通 | 二氧化硫 | 20 |
| 大同 | 臺北市 | `52` | 🟡 普通 | 細懸浮微粒 | 9 |
| 林園 | 高雄市 | `52` | 🟡 普通 | 懸浮微粒 | 7 |
| 冬山 | 宜蘭縣 | `51` | 🟡 普通 | 懸浮微粒 | 12 |
| 古亭 | 臺北市 | `51` | 🟡 普通 | 懸浮微粒 | 8 |
| 三重 | 新北市 | `50` | 🟢 良好 | None | 11 |
| 中壢 | 桃園市 | `50` | 🟢 良好 | None | 8 |
| 前鎮 | 高雄市 | `45` | 🟢 良好 | None | 15 |
| 永和 | 新北市 | `43` | 🟢 良好 | None | 11 |
| 臺灣大道 | 臺中市 | `43` | 🟢 良好 | None | 11 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 79 | 94.0% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 5 | 6.0% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 宜蘭縣 | 2 | `43.0` | `35 - 51` | 🟢 良好 |
| 新竹市 | 1 | `40.0` | `40 - 40` | 🟢 良好 |
| 臺北市 | 7 | `38.4` | `21 - 52` | 🟢 良好 |
| 桃園市 | 6 | `37.7` | `30 - 50` | 🟢 良好 |
| 新北市 | 12 | `35.9` | `30 - 50` | 🟢 良好 |
| 高雄市 | 12 | `34.8` | `22 - 58` | 🟢 良好 |
| 新竹縣 | 2 | `33.0` | `28 - 38` | 🟢 良好 |
| 臺中市 | 6 | `32.3` | `27 - 43` | 🟢 良好 |
| 澎湖縣 | 1 | `32.0` | `32 - 32` | 🟢 良好 |
| 彰化縣 | 5 | `30.8` | `24 - 40` | 🟢 良好 |
| 屏東縣 | 5 | `28.8` | `24 - 38` | 🟢 良好 |
| 苗栗縣 | 3 | `28.7` | `20 - 43` | 🟢 良好 |
| 臺南市 | 5 | `26.6` | `20 - 33` | 🟢 良好 |
| 雲林縣 | 4 | `26.5` | `22 - 32` | 🟢 良好 |
| 連江縣 | 1 | `26.0` | `26 - 26` | 🟢 良好 |
| 金門縣 | 1 | `26.0` | `26 - 26` | 🟢 良好 |
| 嘉義市 | 1 | `25.0` | `25 - 25` | 🟢 良好 |
| 南投縣 | 4 | `24.8` | `21 - 33` | 🟢 良好 |
| 基隆市 | 1 | `23.0` | `23 - 23` | 🟢 良好 |
| 嘉義縣 | 2 | `21.5` | `20 - 23` | 🟢 良好 |
| 花蓮縣 | 1 | `20.0` | `20 - 20` | 🟢 良好 |
| 臺東縣 | 2 | `16.5` | `15 - 18` | 🟢 良好 |

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
