from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "Reading:7.0 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "Reading: 25°C" 


sensor = PHSensor()
temperature = TempSensor()
print("--- Lab Inventory System ---")
print(sensor.get_reading())
print(temperature.get_reading())
