import obd
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int

def batteryTemp(messages):
    d = messages[0].data # only operate on a single message
    print(d)
    d = d[3:] # chop off mode and PID bytes
    print(d)
    v = bytes_to_int(d)-40
    return v

def batteryModule(messages):
    d = messages[0].data # only operate on a single message
    print(d)
    d = d[3:] # chop off mode and PID bytes
    print(d)
    v = bytes_to_int(d)
    return v

#pin1 = b"2240D7" header = b"7E7"
#pin2 = b"2240D9" header = b"7E7"

pin1 = b"224349" #header = b"7E4"
pin2 = b"22434A" #header = b"7E4"

pin1 = b"22434B" #header = b"7E4" (no )
pin2 = b"22434C" #header = b"7E4"

c1 = OBDCommand("%",
               "Battery SOC 1",
               pin1,
               4,
               batteryModule,
               header = b"7E4"
               )

c2 = OBDCommand("%",
               "Battery SOC 1",
               pin2,
               4,
               batteryModule,
               header = b"7E4"
               )

o = obd.OBD()
o.supported_commands.add(c1)
o.supported_commands.add(c2)
rez = o.query(c1)
print("-")
print(rez)
rez = o.query(c2)
print("-")
print(rez)
