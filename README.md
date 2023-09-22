# python-obd-bolt-ev
Python scripts to get Bolt EV specific metrics

```
(.venv) root@raspberrypi:/home/pi/obd# python get_car_metrics.py
Battery SOC: 53.72549019607843
Battery Temp 1: 17
Battery Temp 2: 18
Battery Temp 3: 18
Battery Temp 4: 19
Battery Temp 5: 18
Battery Temp 6: 18
```

Logging example:
```
(.venv) pi@raspberrypi:~ $ tail -f obd/log1.txt
22-09-2023,22:33,20.39,23,23,23,25,23,24
22-09-2023,22:40,20.39,23,23,23,25,23,24
22-09-2023,22:50,20.39,23,23,23,25,23,23
22-09-2023,23:00,20.39,23,23,23,25,23,23
22-09-2023,23:10,20.39,23,23,23,25,23,23
22-09-2023,23:20,20.39,23,23,23,25,23,23
(.venv) pi@raspberrypi:~ $ tail -f sensor-xiaomi/log1.txt
22-09-2023,22:42,27.91,55,86,1
22-09-2023,22:52,28.08,55,86,1
22-09-2023,23:02,28.2,55,86,1
22-09-2023,23:12,28.32,54,86,1
```
