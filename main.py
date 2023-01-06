import requests
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime , date, timedelta
load_dotenv()

actual= date.today()
string_actual=actual.strftime("%Y%m%dT%H%M%S")
yesterday=actual -timedelta(days=1)
string_yesterday=yesterday.strftime("%Y%m%dT%H%M%S")


TOKEN=os.getenv('TOKEN')
URL="https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area%3ASNCF%3A87471003/physical_modes/physical_mode%3ALongDistanceTrain/arrivals?from_datetime="+string_yesterday+"&until_datetime="+string_actual+"&count=1000"
response= requests.get(URL,headers={'Authorization':TOKEN})
result=response.json()
arrivals=result['arrivals']
retard_count=0
for arrival in arrivals:

    infs=arrival["stop_date_time"]
    base_arrival=infs["base_arrival_date_time"]
    time_arrival=infs["arrival_date_time"]
    base_arrival=datetime.strptime(base_arrival,"%Y%m%dT%H%M%S")
    time_arrival=datetime.strptime(time_arrival,"%Y%m%dT%H%M%S")
    if time_arrival > base_arrival:
        retard_count+=1

final_res= retard_count/len(arrivals)
print(final_res)
