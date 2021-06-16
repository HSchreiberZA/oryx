from datetime import datetime


class Value(object):
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    @staticmethod
    def empty():
        return Value(-1, '')

    def serial_json(self):
        return self.__dict__


class BMX280(object):
    def __init__(self, temperature: Value, pressure: Value, humidity: Value):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity

    @staticmethod
    def empty():
        return BMX280(Value.empty(), Value.empty(), Value.empty())

    def to_dict(self):
        return self.__dict__


class GPS(object):
    def __init__(self, latitude: float, longitude: float, valid: bool):
        self.latitude = latitude
        self.longitude = longitude
        self.valid = valid

    @staticmethod
    def empty():
        return GPS(-1, -1, False)

    def to_dict(self):
        return {"valid": self.valid, "loc": [self.longitude, self.latitude]}


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

    @staticmethod
    def empty():
        return SPS30(Value.empty(), Value.empty(), Value.empty(), Value.empty(), Value.empty(), Value.empty(),
                     Value.empty(), Value.empty(), Value.empty(), Value.empty())

    def to_dict(self):
        return self.__dict__


class Device(object):
    def __init__(self, node: str):
        self.node: str = node
        self.time: datetime = datetime.utcnow()

    @staticmethod
    def empty():
        return Device('-1')

    def to_dict(self):
        return {"node": self.node, "time": datetime.utcnow()}


class Reading(object):
    def __init__(self, sps30: SPS30, bmx280: BMX280, gps: GPS, device: Device):
        self.device = device
        self.sps30 = sps30
        self.bmx280 = bmx280
        self.gps = gps

    @staticmethod
    def as_reading(json_dict: dict):
        device: Device = Device.empty()
        bmx280: BMX280 = BMX280.empty()
        sps30: SPS30 = SPS30.empty()
        gps: GPS = GPS.empty()

        if 'device' in json_dict:
            device = Device(**json_dict['device'])
        if 'bmx280' in json_dict:
            bmx280 = BMX280(**json_dict['bmx280'])
        if 'sps30' in json_dict:
            sps30 = SPS30(**json_dict['sps30'])
        if 'gps' in json_dict:
            gps = GPS(**json_dict['gps'])
        return Reading(sps30, bmx280, gps, device)

    def to_dict(self):
        return {'device': self.device.to_dict(), 'sps30': self.sps30.to_dict(), 'bmx280': self.bmx280.to_dict(),
                'gps': self.gps.to_dict()}
