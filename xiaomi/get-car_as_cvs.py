from lywsd03mmc import Lywsd03mmcClient
import datetime

import sys

sensors=[
    { 'name':'Vitalna-Car', 'id': 'A4:C1:38:11:FF:B4' },
]

current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%d-%m-%Y,%H:%M')

results = []
results.append(formatted_time)

for sensor in sensors:

    client = Lywsd03mmcClient(sensor['id'])

    for attempt in range(1,10):
        try:
            data = client.data
        except:
            a = 3
        else:
            break
    else:
        print("10 tries failed")

    results.append(str(data.temperature))
    results.append(str(data.humidity))
    results.append(str(data.battery))
    results.append(str(attempt))

print(",".join(results))
