// Taiwan Air Quality Tracker - Dashboard Logic

document.addEventListener('DOMContentLoaded', () => {
    // API data endpoint
    const DATA_URL = 'data/aqi.json';
    
    // Application State
    let stations = [];
    let filteredStations = [];
    let selectedSiteId = null;
    
    // Filters State
    let searchQuery = '';
    let statusFilter = 'all';
    let countyFilter = 'all';

    // DOM Elements
    const searchInput = document.getElementById('search-input');
    const statusFilterContainer = document.getElementById('status-filter');
    const countySelect = document.getElementById('county-select');
    
    const listContainer = document.getElementById('station-list');
    const listCountBadge = document.getElementById('list-count');
    
    const selectPrompt = document.getElementById('select-prompt');
    const detailContent = document.getElementById('detail-content');
    
    // Statistics Elements
    const statTotal = document.getElementById('stat-total');
    const statAvgAqi = document.getElementById('stat-avg-aqi');
    const statBestSite = document.getElementById('stat-best-site');
    const statWorstSite = document.getElementById('stat-worst-site');
    const updateTimeEl = document.getElementById('update-time');

    // Detail Panel Elements
    const detCounty = document.getElementById('det-county');
    const detSiteId = document.getElementById('det-site-id');
    const detSiteName = document.getElementById('det-site-name');
    const detTime = document.getElementById('det-time');
    const detAqiValue = document.getElementById('det-aqi-value');
    const detAqiCircle = document.getElementById('det-aqi-circle');
    const detStatusBadge = document.getElementById('det-status-badge');
    const detPollutantDesc = document.getElementById('det-pollutant-desc');
    const detHealthTips = document.getElementById('det-health-tips');
    const detHealthText = document.getElementById('det-health-text');
    
    // Pollutant Elements
    const detPm25 = document.getElementById('det-pm25');
    const detPm25Avg = document.getElementById('det-pm25-avg');
    const detPm10 = document.getElementById('det-pm10');
    const detPm10Avg = document.getElementById('det-pm10-avg');
    const detO3 = document.getElementById('det-o3');
    const detO38hr = document.getElementById('det-o3-8hr');
    const detCo = document.getElementById('det-co');
    const detCo8hr = document.getElementById('det-co-8hr');
    const detSo2 = document.getElementById('det-so2');
    const detSo2Avg = document.getElementById('det-so2-avg');
    const detNo2 = document.getElementById('det-no2');
    const detNo = document.getElementById('det-no');
    
    // Weather & Map Elements
    const detWindSpeed = document.getElementById('det-wind-speed');
    const detWindDirec = document.getElementById('det-wind-direc');
    const windCompassIcon = document.getElementById('wind-compass-icon');
    const detCoords = document.getElementById('det-coords');
    const detMapLink = document.getElementById('det-map-link');

    // Initialize application
    init();

    async function init() {
        setupEventListeners();
        await fetchAqiData();
    }

    // Set up sidebar filter change and card click events
    function setupEventListeners() {
        // Search Input filter
        searchInput.addEventListener('input', (e) => {
            searchQuery = e.target.value.trim().toLowerCase();
            applyFilters();
        });

        // AQI Status filter buttons
        statusFilterContainer.addEventListener('click', (e) => {
            if (e.target.classList.contains('filter-btn') || e.target.parentElement.classList.contains('filter-btn')) {
                const target = e.target.classList.contains('filter-btn') ? e.target : e.target.parentElement;
                
                // Update active state
                statusFilterContainer.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
                target.classList.add('active');
                
                statusFilter = target.dataset.status;
                applyFilters();
            }
        });

        // County Select dropdown filter
        countySelect.addEventListener('change', (e) => {
            countyFilter = e.target.value;
            applyFilters();
        });
    }

    // Fetch simplified JSON data from the server
    async function fetchAqiData() {
        try {
            showLoading(true);
            const response = await fetch(DATA_URL);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            stations = await response.json();
            filteredStations = [...stations];
            
            showLoading(false);
            populateCountyDropdown();
            calculateStats();
            renderList();
            
            // Auto-select the first station with valid AQI
            const firstValid = stations.find(s => s.aqi !== null);
            if (firstValid) {
                selectStation(firstValid.site_id);
            }
            
        } catch (error) {
            console.error('Failed to load air quality data:', error);
            showError();
        }
    }

    // Populate county select list dynamically
    function populateCountyDropdown() {
        // Get unique counties
        const counties = [...new Set(stations.map(s => s.county))].sort();
        
        // Reset dropdown to "All" option only
        countySelect.innerHTML = '<option value="all">所有縣市 (全部)</option>';
        
        counties.forEach(county => {
            const opt = document.createElement('option');
            opt.value = county;
            opt.textContent = county;
            countySelect.appendChild(opt);
        });
    }

    // Calculate metadata/statistics from the loaded dataset
    function calculateStats() {
        const validStations = stations.filter(s => s.aqi !== null);
        if (!validStations.length) return;
        
        statTotal.textContent = stations.length;
        
        const sumAqi = validStations.reduce((sum, s) => sum + s.aqi, 0);
        const avg = sumAqi / validStations.length;
        statAvgAqi.textContent = Math.round(avg);
        
        // Find best site (lowest AQI) and worst site (highest AQI)
        const sorted = [...validStations].sort((a, b) => a.aqi - b.aqi);
        const best = sorted[0];
        const worst = sorted[sorted.length - 1];
        
        statBestSite.textContent = `${best.site_name} (${best.aqi})`;
        statBestSite.title = `${best.county}${best.site_name}`;
        statWorstSite.textContent = `${worst.site_name} (${worst.aqi})`;
        statWorstSite.title = `${worst.county}${worst.site_name}`;
        
        // Update time
        if (validStations.length > 0 && validStations[0].publish_time) {
            updateTimeEl.textContent = validStations[0].publish_time;
        } else {
            const now = new Date();
            updateTimeEl.textContent = now.toLocaleTimeString('zh-TW', { hour12: false });
        }
    }

    // Filter stations based on active filters
    function applyFilters() {
        filteredStations = stations.filter(s => {
            // 1. Search Query filter (matches site name, county)
            const matchesSearch = s.site_name.toLowerCase().includes(searchQuery) || 
                                  s.county.toLowerCase().includes(searchQuery);
                                  
            // 2. County filter
            const matchesCounty = countyFilter === 'all' || s.county === countyFilter;
            
            // 3. AQI status filter
            let matchesStatus = true;
            if (s.aqi === null) {
                matchesStatus = (statusFilter === 'all'); // Null only shows in all
            } else {
                if (statusFilter === 'good') {
                    matchesStatus = s.aqi <= 50;
                } else if (statusFilter === 'moderate') {
                    matchesStatus = s.aqi > 50 && s.aqi <= 100;
                } else if (statusFilter === 'unhealthy') {
                    matchesStatus = s.aqi > 100;
                }
            }
            
            return matchesSearch && matchesCounty && matchesStatus;
        });
        
        renderList();
    }

    // Render list of stations in left panel
    function renderList() {
        listContainer.innerHTML = '';
        listCountBadge.textContent = `顯示 ${filteredStations.length} 站`;
        
        if (filteredStations.length === 0) {
            listContainer.innerHTML = `
                <div class="empty-state">
                    <i class="fa-solid fa-wind-ban"></i>
                    <p>沒有符合條件的測站</p>
                </div>
            `;
            return;
        }
        
        filteredStations.forEach(s => {
            const card = document.createElement('div');
            card.className = `station-card glass-inner ${s.site_id === selectedSiteId ? 'selected' : ''}`;
            card.dataset.id = s.site_id;
            
            const aqiText = s.aqi !== null ? s.aqi : '無';
            const colorClass = getAqiColorClass(s.aqi);
            
            card.innerHTML = `
                <div class="station-card-left">
                    <h3>${s.site_name}</h3>
                    <p><i class="fa-solid fa-location-dot"></i> ${s.county}</p>
                </div>
                <div class="station-card-right">
                    <span class="aqi-badge ${colorClass}">${aqiText}</span>
                    <span class="status-desc text-muted">${s.status || '未知'}</span>
                </div>
            `;
            
            card.addEventListener('click', () => {
                selectStation(s.site_id);
            });
            
            listContainer.appendChild(card);
        });
    }

    // Handle station selection
    function selectStation(siteId) {
        selectedSiteId = siteId;
        
        // Update selected class in sidebar cards
        listContainer.querySelectorAll('.station-card').forEach(card => {
            if (card.dataset.id === siteId) {
                card.classList.add('selected');
            } else {
                card.classList.remove('selected');
            }
        });
        
        const station = stations.find(s => s.site_id === siteId);
        if (!station) return;
        
        // Hide prompt and show content
        selectPrompt.classList.add('hidden');
        detailContent.classList.remove('hidden');
        
        // Populate detail view
        detCounty.textContent = station.county;
        detSiteId.textContent = `測站編號：${station.site_id || '-'}`;
        detSiteName.textContent = `${station.site_name} 觀測站`;
        detTime.textContent = `${station.publish_time || '-'} (台北時間)`;
        
        // AQI Score
        const aqiText = station.aqi !== null ? station.aqi : '--';
        detAqiValue.textContent = aqiText;
        
        // Reset and apply AQI color styling to circle
        detAqiCircle.className = 'aqi-circle';
        const colorClass = getAqiColorClass(station.aqi);
        detAqiCircle.classList.add(colorClass);
        
        // Status Badge
        detStatusBadge.textContent = station.status || '未知';
        detStatusBadge.className = 'status-badge';
        detStatusBadge.classList.add(colorClass);
        
        // Pollutant description
        detPollutantDesc.innerHTML = station.pollutant 
            ? `指標污染物：<strong>${formatChemicalFormula(station.pollutant)}</strong>`
            : `指標污染物：<strong>無</strong>`;
            
        // Health Tips & Protective guidelines
        detHealthText.textContent = getHealthAdvice(station.aqi);
        
        // Pollutant concentrations
        fillPollutantField(detPm25, station.pm2_5);
        fillPollutantField(detPm25Avg, station.pm2_5_avg);
        fillPollutantField(detPm10, station.pm10);
        fillPollutantField(detPm10Avg, station.pm10_avg);
        fillPollutantField(detO3, station.o3);
        fillPollutantField(detO38hr, station.o3_8hr);
        fillPollutantField(detCo, station.co);
        fillPollutantField(detCo8hr, station.co_8hr);
        fillPollutantField(detSo2, station.so2);
        fillPollutantField(detSo2Avg, station.so2_avg);
        fillPollutantField(detNo2, station.no2);
        fillPollutantField(detNo, station.no);
        
        // Meteorological data
        detWindSpeed.innerHTML = station.wind_speed 
            ? `${station.wind_speed} <small>m/s</small>` 
            : `- <small>m/s</small>`;
            
        if (station.wind_direc) {
            detWindDirec.textContent = `${station.wind_direc}° (${getWindDirectionName(station.wind_direc)})`;
            // Rotate compass needle based on wind direction
            windCompassIcon.style.transform = `rotate(${station.wind_direc}deg)`;
            windCompassIcon.style.display = 'inline-block';
        } else {
            detWindDirec.textContent = '-';
            windCompassIcon.style.transform = 'none';
        }
        
        // Coordinates and Google Maps Link
        if (station.latitude && station.longitude) {
            detCoords.textContent = `${parseFloat(station.latitude).toFixed(4)}, ${parseFloat(station.longitude).toFixed(4)}`;
            detMapLink.href = `https://www.google.com/maps/search/?api=1&query=${station.latitude},${station.longitude}`;
            detMapLink.style.display = 'inline-block';
        } else {
            detCoords.textContent = '-';
            detMapLink.style.display = 'none';
        }
    }

    // Format chemical symbols (like PM2.5, O3, SO2) with subscript tags
    function formatChemicalFormula(text) {
        if (!text) return '';
        return text
            .replace(/PM2\.5/g, 'PM<sub>2.5</sub>')
            .replace(/PM10/g, 'PM<sub>10</sub>')
            .replace(/O3/g, 'O<sub>3</sub>')
            .replace(/SO2/g, 'SO<sub>2</sub>')
            .replace(/NO2/g, 'NO<sub>2</sub>')
            .replace(/CO/g, 'CO');
    }

    // Helper to safely write pollutant numbers or dashes
    function fillPollutantField(element, val) {
        if (val === undefined || val === null || val === '') {
            element.textContent = '-';
        } else {
            element.textContent = val;
        }
    }

    // Determine color class based on AQI value
    function getAqiColorClass(aqi) {
        if (aqi === null || aqi === undefined) return 'color-gray';
        if (aqi <= 50) return 'color-green';
        if (aqi <= 100) return 'color-yellow';
        if (aqi <= 150) return 'color-orange';
        if (aqi <= 200) return 'color-red';
        if (aqi <= 300) return 'color-purple';
        return 'color-maroon';
    }

    // Get health recommendations based on AQI
    function getHealthAdvice(aqi) {
        if (aqi === null || aqi === undefined) return '暫無監測資料，請參考鄰近觀測站數據。';
        if (aqi <= 50) {
            return '空氣品質良好，非常適合進行所有戶外活動與正常作息。';
        } else if (aqi <= 100) {
            return '空氣品質普通。極少數極敏感者可能會對某些污染物產生輕微不適（如咳嗽），但對一般大眾健康影響極低，可正常戶外活動。';
        } else if (aqi <= 150) {
            return '對敏感族群不健康。敏感族群（如心血管或呼吸道疾病患者、老人、幼童）建議減少體力消耗活動，特別是避免在戶外進行劇烈運動。一般民眾可正常活動。';
        } else if (aqi <= 200) {
            return '對所有族群不健康。所有人都應開始注意個人呼吸道感受。敏感族群應留在室內並減少戶外體力消耗；一般民眾應減少在戶外劇烈運動，出門建議佩戴口罩。';
        } else if (aqi <= 300) {
            return '非常不健康。所有人均應減少戶外活動，並避免在戶外從事劇烈體力消耗。敏感族群應留在室內，視需要開啟空氣清淨機。學校應考慮調整戶外體育課。';
        } else {
            return '危害等級！所有人應避免一切戶外活動。室內應緊閉門窗、開啟空氣清淨機。此空氣品質可能對人體健康造成立即性或嚴重的影響。';
        }
    }

    // Get English and Chinese wind direction category
    function getWindDirectionName(degree) {
        const deg = parseFloat(degree);
        if (isNaN(deg)) return '';
        
        const directions = [
            '北', '東北北', '東北', '東北東',
            '東', '東南東', '東南', '東南南',
            '南', '西南南', '西南', '西南西',
            '西', '西北西', '西北', '西北北'
        ];
        
        // Normalize degree to 0-360
        const normalized = ((deg % 360) + 360) % 360;
        const index = Math.round(normalized / 22.5) % 16;
        return directions[index] + '風';
    }

    // UI Helpers
    function showLoading(isLoading) {
        if (isLoading) {
            listContainer.innerHTML = `
                <div class="loading-state">
                    <i class="fa-solid fa-circle-notch fa-spin"></i>
                    <p>載入空氣品質資料中...</p>
                </div>
            `;
        }
    }

    function showError() {
        listContainer.innerHTML = `
            <div class="empty-state">
                <i class="fa-solid fa-triangle-exclamation font-red"></i>
                <p>資料載入失敗</p>
                <button onclick="window.location.reload()" class="btn-retry">重新整理</button>
            </div>
        `;
    }
});
