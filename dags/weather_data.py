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
  dag_id='get-and-save-weather-data',
  description='Download weather data via API calls, parse it, and save to S3 storage',
  default_args=default_args,
  schedule='@hourly',
  catchup=False,
  start_date=pendulum.datetime(2023, 10, 1),
  tags=['merpati'],
)

def GetWeatherData():
  """
  ### Download and store weather information from Open-Meteo
  Executes Python scripts hosted in specified `ssh_conn_id` to
  [download weather information](https://github.com/stndn/merpati/tree/main/weather)
  and stores them in S3
  """

  get_weather = SSHOperator(
      task_id='get-weather',
      ssh_conn_id='rumah_merpati',
      command='cd /home/garuda/app/merpati/weather && make get-weather'
    )

  parse_weather = SSHOperator(
      task_id='parse-weather',
      ssh_conn_id='rumah_merpati',
      command='cd /home/garuda/app/merpati/weather && make parse-weather'
    )

  save_weather = SSHOperator(
      task_id='save-weather',
      ssh_conn_id='rumah_merpati',
      command='cd /home/garuda/app/merpati/weather && make save-weather'
    )

  get_weather >> parse_weather >> save_weather


_ = GetWeatherData()
