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

**⏰ Last Updated (Taipei Time)**: `2026-07-07 03:09:07`

### 🚨 Current Air Quality Summary
- **Total Active Stations**: 84
- **National Average AQI**: `26.2` (良好)
- **🟢 Cleanest Location**: 屏東縣恆春 (AQI: `8`)
- **🔴 Most Polluted Location**: 新北市永和 (AQI: `67`, Main Pollutant: `細懸浮微粒`)

### 🗺️ Top 10 Cleanest Stations
| Station | County | AQI | Status | PM2.5 (μg/m³) | PM10 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 恆春 | 屏東縣 | `8` | 🟢 良好 | 0 | 4 |
| 屏東（琉球） | 屏東縣 | `8` | 🟢 良好 | 2 | 1 |
| 左營 | 高雄市 | `10` | 🟢 良好 | 4 | 3 |
| 臺東 | 臺東縣 | `10` | 🟢 良好 | 4 | 7 |
| 屏東（枋山） | 屏東縣 | `10` | 🟢 良好 | 1 | 2 |
| 觀音 | 桃園市 | `13` | 🟢 良好 | 3 | 6 |
| 屏東 | 屏東縣 | `13` | 🟢 良好 | 2 | 12 |
| 前金 | 高雄市 | `14` | 🟢 良好 | 0 | 2 |
| 花蓮 | 花蓮縣 | `15` | 🟢 良好 | 4 | 9 |
| 關山 | 臺東縣 | `15` | 🟢 良好 | 4 | 9 |

### 🚨 Top 10 Most Polluted Stations
| Station | County | AQI | Status | Main Pollutant | PM2.5 (μg/m³) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 永和 | 新北市 | `67` | 🟡 普通 | 細懸浮微粒 | 50 |
| 新北（樹林） | 新北市 | `61` | 🟡 普通 | 細懸浮微粒 | 18 |
| 士林 | 臺北市 | `56` | 🟡 普通 | 細懸浮微粒 | 12 |
| 板橋 | 新北市 | `55` | 🟡 普通 | 細懸浮微粒 | 12 |
| 三重 | 新北市 | `52` | 🟡 普通 | 細懸浮微粒 | 14 |
| 汐止 | 新北市 | `52` | 🟡 普通 | 細懸浮微粒 | 14 |
| 中山 | 臺北市 | `52` | 🟡 普通 | 細懸浮微粒 | 11 |
| 新莊 | 新北市 | `51` | 🟡 普通 | 細懸浮微粒 | 10 |
| 陽明 | 臺北市 | `51` | 🟡 普通 | 細懸浮微粒 | 16 |
| 新店 | 新北市 | `46` | 🟢 良好 | None | 11 |

<!-- AQI_END -->

---

## 📈 County & level Statistics

<!-- STATS_START -->

### 📊 National AQI Level Distribution
| AQI Level | Range | Color | Station Count | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| 良好 (Good) | 0 - 50 | 🟢 Green | 75 | 89.3% |
| 普通 (Moderate) | 51 - 100 | 🟡 Yellow | 9 | 10.7% |
| 對敏感族群不健康 (USG) | 101 - 150 | 🟠 Orange | 0 | 0.0% |
| 對所有族群不健康 (Unhealthy) | 151 - 200 | 🔴 Red | 0 | 0.0% |
| 非常不健康 (Very Unhealthy) | 201 - 300 | 🟣 Purple | 0 | 0.0% |
| 危害 (Hazardous) | 301+ | 🟤 Maroon | 0 | 0.0% |

### 🏢 Average AQI by County / City
| County | Station Count | Average AQI | Range (Min - Max) | Status |
| :--- | :--- | :--- | :--- | :--- |
| 臺北市 | 7 | `46.1` | `38 - 56` | 🟢 良好 |
| 新北市 | 12 | `44.8` | `25 - 67` | 🟢 良好 |
| 桃園市 | 6 | `27.5` | `13 - 39` | 🟢 良好 |
| 新竹縣 | 2 | `27.0` | `21 - 33` | 🟢 良好 |
| 南投縣 | 4 | `26.8` | `19 - 32` | 🟢 良好 |
| 新竹市 | 1 | `26.0` | `26 - 26` | 🟢 良好 |
| 彰化縣 | 5 | `25.0` | `20 - 32` | 🟢 良好 |
| 連江縣 | 1 | `25.0` | `25 - 25` | 🟢 良好 |
| 宜蘭縣 | 2 | `24.5` | `22 - 27` | 🟢 良好 |
| 基隆市 | 1 | `23.0` | `23 - 23` | 🟢 良好 |
| 苗栗縣 | 3 | `22.7` | `18 - 28` | 🟢 良好 |
| 嘉義市 | 1 | `22.0` | `22 - 22` | 🟢 良好 |
| 臺中市 | 6 | `22.0` | `18 - 27` | 🟢 良好 |
| 雲林縣 | 4 | `21.2` | `18 - 25` | 🟢 良好 |
| 嘉義縣 | 2 | `20.0` | `18 - 22` | 🟢 良好 |
| 金門縣 | 1 | `18.0` | `18 - 18` | 🟢 良好 |
| 高雄市 | 12 | `17.2` | `10 - 21` | 🟢 良好 |
| 澎湖縣 | 1 | `17.0` | `17 - 17` | 🟢 良好 |
| 臺南市 | 5 | `16.2` | `15 - 17` | 🟢 良好 |
| 花蓮縣 | 1 | `15.0` | `15 - 15` | 🟢 良好 |
| 臺東縣 | 2 | `12.5` | `10 - 15` | 🟢 良好 |
| 屏東縣 | 5 | `10.8` | `8 - 15` | 🟢 良好 |

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
