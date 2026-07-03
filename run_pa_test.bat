@echo off
:: Windows Test Runner for PythonAnywhere MOENV Air Quality Crawler
:: Executes the standalone script and displays its log output

set LOCAL_PATH=%~dp0
cd /d %LOCAL_PATH%

echo ==================================================
echo       Testing: aqi_crawler_pa.py (Air Quality)
echo ==================================================
echo.
echo [*] Preparing to run aqi_crawler_pa.py ...

if not exist aqi_crawler_pa.py (
    echo [!] Error: aqi_crawler_pa.py not found!
    goto error
)

if not exist config.json (
    echo [!] Warning: config.json not found.
    echo [*] The script will create a template config.json.
)

echo [*] Running Python crawler script...
echo --------------------------------------------------
python aqi_crawler_pa.py
echo --------------------------------------------------
echo.
echo [+] Execution finished.
goto end

:error
echo.
echo [!] Execution failed. Please check the project directory.

:end
echo.
pause
