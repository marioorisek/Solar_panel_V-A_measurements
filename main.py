from keithley2000 import Keithley2000
from light_sensor import LightSensor
from database import Database
from time import sleep
import datetime
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-d", "--duration", dest="duration", default=1,
                    help="set measurement duration in hours")
parser.add_argument("-p", "--period",
                    dest="period", default=10,
                    help="set period of measurements in seconds")

args = vars(parser.parse_args())
for key in args:
    args[key] = float(args[key])

period = args['period']
if period < 1:
    period = 1

duration = args['duration']

count = (duration * 3600) / period

print(f"Acquiring data for {duration} hours with {period} seconds period.\n")

verbose = False
db = Database(db_file_name="lightmeter.db")
mm = Keithley2000(interface='/dev/ttyUSB0', baudrate=9600, verbose=verbose)
ls = LightSensor(verbose=verbose)


db.create_tables()
mm.reset()
mm.set_mode_dc_current()
for pchaaa in range(int(count)):
    time = datetime.datetime.now()
    current = mm.fetch_latest_reading()
    light = ls.read_light_intensity()
    print(f"{time} current: {current * 1000:.1f} mA at {light} lux ")
    db.insert_current_reading(current, light)
    sleep(period)

mm.set_local_control()
