class Keithley2000:
    def __init__(self, interface='/dev/ttyUSB0', baudrate=9600, verbose=False):
        """Create object to communicate with Keithley 2000 via RS 232"""

        import serial

        self.interface = interface
        self.baudrate = baudrate
        self.verbose = verbose
        self.port = serial.Serial(self.interface, self.baudrate)
        self.port.timeout = 10
        self.units = "DCV"

    def set_local_control(self):
        """Set Keithley 2000 to local control"""
        if self.verbose:
            print("Keithley 2000 local control enabled.")
        self.query(":SYSTEM:LOCAL", return_response=False)

    def reset(self):
        """Reset Keithley 2000 to default"""
        if self.verbose:
            print("Keithley 2000 reset.")
        self.query("*rst", return_response=False)

    def set_mode_dc_current(self):
        "Set Keithley 2000 to measure DC current"
        if self.verbose:
            print("DC voltage measurement set.")
        self.units = "DCA"
        return self.query(":CONF:CURR:DC", return_response=False)

    def set_mode_dc_voltage(self):
        "Set Keithley 2000 to measure DC voltage"
        if self.verbose:
            print("DC voltage measurement set.")
        self.units = "DCV"
        return self.query(":CONF:VOLT:DC", return_response=False)

    def fetch_latest_reading(self):
        "Return last reading"
        response = float(self.query(":READ?", return_response=True))
        if self.verbose:
            print(f"Last reading : {response:.3f} {self.units}")
        return response

    def query(self, query: str, return_response=True):
        """Send query to device and return response"""

        from time import sleep

        with self.port:
            if self.verbose:
                print(query)
            query = query + "\n"
            self.port.write(query.encode('ascii'))
            if return_response:
                sleep(0.01)
                response = self.port.readline().decode('ascii')
                if self.verbose:
                    print(response)
                return response

