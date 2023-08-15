<h1 align="center"> GeoIP </h1>

<p align="center">Parse ip address, return csv-file with IP, Country.</p>

Input:
|./assets/http.txt    | 
|-----------------------
|95.132.132.76:2252   |
|91.218.171.55        |
|84.50.12.232:123     |


Output:

|./proxy_by_country.csv| <!-- -->    |
|-------------         |-------------|
|95.132.132.76:2252    |Украина
|91.218.171.55         |Таджикистан
|84.50.12.232:123      |Эстония

## Installation
```
git clone https://github.com/mikedigriz/geoip.git
cd geoip
pip3 install -r requriments.txt
```
## Execute
```
python3 main.py
```
## Update GeoIP database
- You can [download here](
https://cdn.jsdelivr.net/npm/geolite2-country@1.0.5/GeoLite2-Country.mmdb.gz) actual Country database
