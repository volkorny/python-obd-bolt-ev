import obd
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int

def batterySOC1(messages):
    d = messages[0].data # only operate on a single message
    d = d[2:] # chop off mode and PID bytes
    print(d[0])
    v = bytes_to_int(d)/2.55
    return v

pin = b"015B"

c = OBDCommand("%",
               "Battery SOC 1",
               pin,
               3,
               batterySOC1,
               )

o = obd.OBD(fast=False, timeout=30)
o.supported_commands.add(c)
rez = o.query(c)

print(rez)
