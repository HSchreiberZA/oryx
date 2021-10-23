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
    def __init__(self, bmx280: BMX280, gps: GPS, device: Device):
        self.device = device
        self.bmx280 = bmx280
        self.gps = gps

    @staticmethod
    def as_reading(json_dict: dict):
        device: Device = Device.empty()
        bmx280: BMX280 = BMX280.empty()
        gps: GPS = GPS.empty()

        if 'device' in json_dict:
            device = Device(**json_dict['device'])
        if 'bmx280' in json_dict:
            bmx280 = BMX280(**json_dict['bmx280'])
        if 'gps' in json_dict:
            gps = GPS(**json_dict['gps'])
        return Reading(bmx280, gps, device)

    def to_dict(self):
        return {'device': self.device.to_dict(), 'bmx280': self.bmx280.to_dict(),
                'gps': self.gps.to_dict()}
