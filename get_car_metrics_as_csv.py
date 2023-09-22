import obd
import datetime
from obd import OBDCommand

def batterySOC(messages):
    d = messages[0].data # only operate on a single message
    d = d[2:] # chop off mode and PID bytes
    v = d[0]/255*100
    v = round(v, 2)
    return v

def batteryTemp(messages):
    d = messages[0].data
    d = d[3:]
    v = d[0] - 40
    return v


current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%d-%m-%Y,%H:%M')

commands = [
    OBDCommand("SOC",        "Battery SOC",    b"228334", 3, batterySOC,  header = b"7E4" ),
    OBDCommand("MOD_1_TEMP", "Battery Temp 1", b"2240D7", 4, batteryTemp, header = b"7E7" ),
    OBDCommand("MOD_2_TEMP", "Battery Temp 2", b"2240D9", 4, batteryTemp, header = b"7E7" ),
    OBDCommand("MOD_3_TEMP", "Battery Temp 3", b"2240DB", 4, batteryTemp, header = b"7E7" ),
    OBDCommand("MOD_4_TEMP", "Battery Temp 4", b"2240DD", 4, batteryTemp, header = b"7E7" ),
    OBDCommand("MOD_5_TEMP", "Battery Temp 5", b"2240DF", 4, batteryTemp, header = b"7E7" ),
    OBDCommand("MOD_6_TEMP", "Battery Temp 6", b"2240E1", 4, batteryTemp, header = b"7E7" ),
]

connection = obd.OBD(fast=False, timeout=30)

for cmd in commands:
    connection.supported_commands.add(cmd)

results=[]
results.append(formatted_time)

for cmd in commands:
    value = connection.query(cmd)
    results.append(str(value))

print(",".join(results))
