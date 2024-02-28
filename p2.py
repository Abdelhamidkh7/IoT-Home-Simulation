from p1 import SmartLight, Thermostat, SecurityCamera
import time
import threading

class AutomationSystem:
    def __init__(self):
        self.devices = []
   
    def discover_and_add_device(self, device):
        self.devices.append(device)
        print(f"Device {device.device_id} added.")

    def execute_automation_tasks(self):
        # Placeholder for complex automation logic
        for device in self.devices:
            if isinstance(device, Thermostat):
                if device.temperature > 25:
                    device.set_temperature(20)
                    print(f"{device.device_id} temperature adjusted for energy saving.")
            elif isinstance(device, SmartLight):
                if device.status == 'on' and device.time_on > 60:
                    device.turn_off()
                print(f"{device.device_id} turned off after being on for more than an hour.")
            elif isinstance(device, SecurityCamera):
                if device.security_status == 'alert':
                    #device.start_recording()
                    print(f"{device.device_id} started recording due to detected motion.")
           

    def simulate_device_behavior(self):
        for device in self.devices:
            device.randomize()

    def run_simulation_loop(self):
        while True:
            self.execute_automation_tasks()
            self.simulate_device_behavior()
            time.sleep(5)  # Simulation loop runs every 5 seconds

# Example Usage
automation_system = AutomationSystem()
smart_light = SmartLight('222')
thermostat = Thermostat('333')
camera = SecurityCamera('444')


# Adding devices to the system
automation_system.discover_and_add_device(smart_light)
automation_system.discover_and_add_device(thermostat)
automation_system.discover_and_add_device(camera)

# Running the simulation in a separate thread
simulation_thread = threading.Thread(target=automation_system.run_simulation_loop)
simulation_thread.start()
