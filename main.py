from keithley2000 import Keithley2000
from light_sensor import LightSensor
from database import Database
from time import sleep
import datetime


verbose = False
db = Database(db_file_name="lightmeter.db")
mm = Keithley2000(interface='/dev/ttyUSB0', baudrate=9600, verbose=verbose)
ls = LightSensor(verbose=verbose)


db.create_tables()
mm.reset()
mm.set_mode_dc_current()
for pchaaa in range(600):
    time = datetime.datetime.now()
    current = mm.fetch_latest_reading()
    light = ls.read_light_intensity()
    print(f"{time} current: {current * 1000:.1f} mA at {light} lux ")
    db.insert_current_reading(current, light)
    sleep(10)

mm.set_local_control()