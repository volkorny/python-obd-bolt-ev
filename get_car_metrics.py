import obd
from obd import OBDCommand

def batterySOC(messages):
    d = messages[0].data # only operate on a single message
    d = d[2:] # chop off mode and PID bytes
    v = d[0]/2.55
    return v

def batteryTemp(messages):
    d = messages[0].data
    d = d[3:]
    v = d[0] - 40
    return v

commands = [
    OBDCommand("SOC",        "Battery SOC",    b"015B",   3, batterySOC                   ),
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

for cmd in commands:
    result = connection.query(cmd)
    print(f"{cmd.desc}: {result}")
