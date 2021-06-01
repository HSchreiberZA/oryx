class Value(object):
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit


class BMX280(object):
    def __init__(self, temperature: Value, pressure: Value, humidity: Value):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity


class GPS(object):
    def __init__(self, latitude:float, longitude: float, valid:bool):
        self.latitude = latitude
        self.longitude = longitude
        self.valid = valid


class SPS30(object):
    def __init__(self,
                 mc_pm1: Value,
                 mc_pm2_5: Value,
                 mc_pm4: Value,
                 mc_pm10: Value,
                 nc_pm0_5: Value,
                 nc_pm1: Value,
                 nc_pm2_5: Value,
                 nc_pm4: Value,
                 nc_pm10: Value,
                 ps: Value):
        self.mc_pm1 = mc_pm1
        self.mc_pm2_5 = mc_pm2_5
        self.mc_pm4 = mc_pm4
        self.mc_pm10 = mc_pm10
        self.nc_pm0_5 = nc_pm0_5
        self.nc_pm1 = nc_pm1
        self.nc_pm2_5 = nc_pm2_5
        self.nc_pm4 = nc_pm4
        self.nc_pm10 = nc_pm10
        self.ps = ps


class Response(object):
    def __init__(self, sps30: SPS30, bmx280: BMX280, gps: GPS):
        self.sps30 = sps30
        self.bmx280 = bmx280
        self.gps = gps