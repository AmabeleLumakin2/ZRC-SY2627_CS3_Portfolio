Activity 3: Spot the Error! (10 Minutes)

bell ringer activity (no submission required)


Here is a "Spot the Error" challenge designed for your Session 2 warm-up. This will help students realize that @abstractmethod isn't just a suggestion—it's a strict rule enforced by Python.

Instructions: Look at the following three code snippets. Only ONE of them will run successfully. The other two will crash with a TypeError. Can you find the "Legal" code?

Snippet A: 

Python

from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod

    def get_data(self):

        pass

class TempSensor(Sensor):

    # The student forgot to write the 'get_data' method!

    def calibrate(self):

        print("Calibrating...")

t = TempSensor() 

print("Success!")

Snippet B: 
Python

from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod

    def get_data(self):

        pass

class PHMeter(Sensor):

    def get_data(self):

        return "7.0 pH"

p = PHMeter()

print("Success!")

Snippet C: 
Python

from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod

    def get_data(self):

        pass

# Trying to create a generic sensor directly

s = Sensor() 

print("Success!")

The teacher will confirm the answer. 


ANSWER: The first code will result in an error since the method used in the child class is different from the parnet class, the second one is able to work for following all the rules of abstraction, while the third one will also result in an error due to the lack of its child class in the code.