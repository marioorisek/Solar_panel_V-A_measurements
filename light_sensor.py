class LightSensor:
    """Class to read Yoctopuce V3 light sensor"""
    def __init__(self, verbose=False):
        from yoctopuce.yocto_lightsensor import YRefParam, YAPI, YLightSensor
        import sys

        errmsg = YRefParam()
        if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
            sys.exit("init error :" + errmsg.value)

        self.light_sensor = YLightSensor.FirstLightSensor()
        self.verbose = verbose

    def read_light_intensity(self):
        """Read current light intensity in lux"""
        readout = self.light_sensor.get_currentValue()
        if self.verbose:
            print(f"Light intensity: {readout:,} lux")
        return readout
