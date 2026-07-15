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

**⏰ Last Updated (Taipei Time)**: `2026-07-16 07:09:13`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `29.2` (良好)
- **🟢 Cleanest Location**: 苗栗縣三義 (AQI: `0`)
- **🔴 Most Polluted Location**: 屏東縣屏東（枋山） (AQI: `79`, Main Pollutant: `懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 三義 | 苗栗縣 | `0` | 🟢  | 3 | 11 |
| 新營 | 臺南市 | `20` | 🟢 良好 | 3 | 16 |
| 大園 | 桃園市 | `20` | 🟢 良好 | 5 | 13 |
| 新港 | 嘉義縣 | `20` | 🟢 良好 | 6 | 14 |
| 南投（鹿谷） | 南投縣 | `20` | 🟢 良好 | 2 | 5 |
| 苗栗 | 苗栗縣 | `21` | 🟢 良好 | 4 | 11 |
| 橋頭 | 高雄市 | `22` | 🟢 良好 | 6 | 19 |
| 崙背 | 雲林縣 | `22` | 🟢 良好 | 6 | 11 |
| 金門 | 金門縣 | `22` | 🟢 良好 | 6 | 13 |
| 萬華 | 臺北市 | `22` | 🟢 良好 | 4 | 16 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 屏東（枋山） | 屏東縣 | `79` | 🟡 普通 | 懸浮微粒 | 21 |
| 林園 | 高雄市 | `47` | 🟢 良好 | None | 9 |
| 大同 | 臺北市 | `43` | 🟢 良好 | None | 18 |
| 中壢 | 桃園市 | `41` | 🟢 良好 | None | 14 |
| 桃園 | 桃園市 | `41` | 🟢 良好 | None | 11 |
| 新莊 | 新北市 | `40` | 🟢 良好 | None | 10 |
| 楠梓 | 高雄市 | `40` | 🟢 良好 | None | 14 |
| 冬山 | 宜蘭縣 | `38` | 🟢 良好 | None | 10 |
| 新北（樹林） | 新北市 | `38` | 🟢 良好 | None | 11 |
| 竹東 | 新竹縣 | `38` | 🟢 良好 | None | 8 |

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
| 花蓮縣 | 1 | `37.0` | `37 - 37` | 🟢 良好 |
| 屏東縣 | 5 | `35.8` | `22 - 79` | 🟢 良好 |
| 宜蘭縣 | 2 | `34.0` | `30 - 38` | 🟢 良好 |
| 新竹縣 | 2 | `34.0` | `30 - 38` | 🟢 良好 |
| 桃園市 | 6 | `32.8` | `20 - 41` | 🟢 良好 |
| 新竹市 | 1 | `32.0` | `32 - 32` | 🟢 良好 |
| 新北市 | 12 | `31.8` | `25 - 40` | 🟢 良好 |
| 臺北市 | 7 | `30.0` | `22 - 43` | 🟢 良好 |
| 連江縣 | 1 | `30.0` | `30 - 30` | 🟢 良好 |
| 彰化縣 | 5 | `29.8` | `27 - 32` | 🟢 良好 |
| 高雄市 | 12 | `29.2` | `22 - 47` | 🟢 良好 |
| 臺東縣 | 2 | `28.5` | `27 - 30` | 🟢 良好 |
| 基隆市 | 1 | `28.0` | `28 - 28` | 🟢 良好 |
| 南投縣 | 4 | `27.8` | `20 - 37` | 🟢 良好 |
| 臺南市 | 5 | `27.4` | `20 - 30` | 🟢 良好 |
| 嘉義市 | 1 | `27.0` | `27 - 27` | 🟢 良好 |
| 澎湖縣 | 1 | `25.0` | `25 - 25` | 🟢 良好 |
| 雲林縣 | 4 | `24.5` | `22 - 28` | 🟢 良好 |
| 臺中市 | 6 | `24.3` | `22 - 29` | 🟢 良好 |
| 嘉義縣 | 2 | `22.5` | `20 - 25` | 🟢 良好 |
| 金門縣 | 1 | `22.0` | `22 - 22` | 🟢 良好 |
| 苗栗縣 | 3 | `18.7` | `0 - 35` | 🟢 良好 |

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
