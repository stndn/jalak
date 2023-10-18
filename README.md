# Jalak

Repository for DAG's used in [Garudata Data Platform Project][url-garudata]


### List of DAGs:

1. [`get-and-save-weather-data`][url-weather-data]: Download weather data from [Open-Meteo][url-open-meteo] and save the files into S3 bucket
1. [`extract-weather-data-from-json`][url-extract-weather-json]: Extract and transform the data in the JSON files and store in the PostgreSQL database for reporting

TODO:
- [X] Auto deploy to [Airflow][url-garudata-airflow]
- [ ] Test DAG's before deployment


<!-- Links -->

[url-garudata]: https://github.com/stndn/garudata "Garudata Data Platform"
[url-garudata-airflow]: https://flow.71182141.xyz/ "Garudata - Airflow"
[url-open-meteo]: https://open-meteo.com/ "Open-Meteo"
[url-weather-data]: /dags/weather_data.py
[url-extract-weather-json]: /dags/extract_weather_json.py
