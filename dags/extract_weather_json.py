import pendulum

from airflow.decorators import dag, task
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
  "owner": "sutan",
  "owner_links": { 'sutan': 'https://flow.71182141.xyz/' },
  "provide_context": True,
  "retries": 0,
}

@dag(
  dag_id='extract-weather-data-from-json',
  description='Extract weather data from JSON files in S3, and create denormalized datasets suitable for reporting',
  default_args=default_args,
  schedule='20 * * * *',
  catchup=False,
  start_date=pendulum.datetime(2023, 10, 17),
  tags=['merpati'],
)

def SaveWeatherData():
  """
  ### Process the weather information stored in JSON files in S3 bucket
  Executes Python scripts hosted remotely to process JSON files obtained from
  Open-Meteo (based on [Merpati/weather-etl](https://github.com/stndn/merpati/tree/main/weather-etl))
  and store them in denormalized tables for reporting purpose
  """

  save_current_weather_dataset = SSHOperator(
      task_id='save-current-weather',
      ssh_conn_id='rumah_merpati',
      sla=pendulum.duration(minutes=5),
      command='cd /home/garuda/app/merpati/weather-tl && make current-weather-dataset'
    )

  save_hourly_weather_dataset = SSHOperator(
      task_id='save-hourly-weather',
      ssh_conn_id='rumah_merpati',
      sla=pendulum.duration(minutes=5),
      command='cd /home/garuda/app/merpati/weather-tl && make hourly-weather-dataset'
    )

  archive_weather_json_files = SSHOperator(
      task_id='archive-weather-json',
      ssh_conn_id='rumah_merpati',
      sla=pendulum.duration(minutes=5),
      command='cd /home/garuda/app/merpati/weather-tl && make archive-weather-json'
    )

  [ save_current_weather_dataset, save_hourly_weather_dataset ] >> archive_weather_json_files


_ = SaveWeatherData()
