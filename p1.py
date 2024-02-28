import random

# Base class for all IoT devices
class IoTDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = 'off'

    def turn_on(self):
        self.status = 'on'

    def turn_off(self):
        self.status = 'off'

# SmartLight class
class SmartLight(IoTDevice):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.brightness = 0

    def set_brightness(self, brightness):
        self.brightness = brightness

    def randomize(self):
        self.brightness = random.randint(0, 100)

# Thermostat class
class Thermostat(IoTDevice):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.temperature = 20  

    def set_temperature(self, temperature):
        self.temperature = temperature

    def randomize(self):
        self.temperature = random.randint(15, 30)

# SecurityCamera class
class SecurityCamera(IoTDevice):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.security_status = 'normal'

    def set_security_status(self, status):
        self.security_status = status

    def randomize(self):
        self.security_status = random.choice(['normal', 'alert'])

# Example Usage
smart_light = SmartLight("Light1")
thermostat = Thermostat("Thermo1")
camera = SecurityCamera("Camera1")

# Simulate random behavior
smart_light.randomize()
thermostat.randomize()
camera.randomize()
