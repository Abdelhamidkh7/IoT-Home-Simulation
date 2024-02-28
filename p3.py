


from p1 import SmartLight, Thermostat, SecurityCamera
from p2 import AutomationSystem

import tkinter as tk
from tkinter import ttk

# Initialize example devices
smart_light = SmartLight("Light1")
thermostat = Thermostat("Thermo1")
camera = SecurityCamera("Camera1")

# Main application class
class SmartHomeApp:
    def __init__(self, root):
        self.root = root
        root.title("Smart Home IoT Simulator")
        root.state('zoomed')  # This maximizes the window on start

        # Status Text Box
        self.status_text = tk.Text(root, height=5, width=50)
        self.status_text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # SmartLight GUI Components
        self.light_brightness_scale = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=self.update_light_brightness)
        self.light_brightness_scale.set(smart_light.brightness)
        self.light_brightness_scale.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.light_toggle_button = tk.Button(root, text="Toggle ON/OFF", command=self.toggle_light)
        self.light_toggle_button.grid(row=1, column=1, padx=5, pady=5)
        self.light_brightness_value_label = tk.Label(root, text="Brightness: 0%")
        self.light_brightness_value_label.grid(row=2, column=0, padx=5, pady=0, sticky="w")

        # Thermostat GUI Components
        self.thermo_temp_scale = ttk.Scale(root, from_=15, to=30, orient='horizontal', command=self.update_thermo_temp)
        self.thermo_temp_scale.set(thermostat.temperature)
        self.thermo_temp_scale.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.thermo_toggle_button = tk.Button(root, text="Toggle ON/OFF", command=self.toggle_thermostat)
        self.thermo_toggle_button.grid(row=3, column=1, padx=5, pady=5)
        self.thermo_temp_value_label = tk.Label(root, text="Temperature: 20°C")
        self.thermo_temp_value_label.grid(row=4, column=0, padx=5, pady=0, sticky="w")

        # SecurityCamera GUI Components
        self.camera_motion_button = tk.Button(root, text="Random Detect Motion", command=self.random_detect_motion)
        self.camera_motion_button.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        self.camera_toggle_button = tk.Button(root, text="Toggle ON/OFF", command=self.toggle_camera)
        self.camera_toggle_button.grid(row=5, column=1, padx=5, pady=5)
        self.camera_motion_value_label = tk.Label(root, text="Motion: No")
        self.camera_motion_value_label.grid(row=6, column=0, padx=5, pady=0, sticky="w")

        # Automation Rule Display
        self.rule_label = tk.Label(root, text="Automation Rule: Turn on lights when motion is detected")
        self.rule_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # Call to update the status text and value labels
        self.update_status_text()

    # Method to update the status text and value labels
    def update_status_text(self):
        # Update the status text box
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete('1.0', tk.END)
        self.status_text.insert(tk.END, f"Living Room Light: {'On' if smart_light.status == 'on' else 'Off'}\n")
        self.status_text.insert(tk.END, f"Living Room Thermostat: {'On' if thermostat.status == 'on' else 'Off'}\n")
        self.status_text.insert(tk.END, f"Front Door Camera: {'On' if camera.status == 'on' else 'Off'}\n")
        self.status_text.config(state=tk.DISABLED)

        # Update the value labels
        self.light_brightness_value_label.config(text=f"Brightness: {smart_light.brightness}%")
        self.thermo_temp_value_label.config(text=f"Temperature: {thermostat.temperature}°C")
        self.camera_motion_value_label.config(text=f"Motion: {'Detected' if camera.security_status == 'alert' else 'No'}")

    def update_light_brightness(self, brightness):
        print(f"Updating light brightness: {brightness}")
        smart_light.set_brightness(int(float(brightness)))
        self.light_brightness_value_label.config(text=f"Brightness: {smart_light.brightness}%")  # Update brightness label
        self.update_status_text()

    def toggle_light(self):
        print("Toggling light")
        if smart_light.status == 'off':
            smart_light.turn_on()
        else:
          smart_light.turn_off()
        self.update_status_text()

    def update_thermo_temp(self, temperature):
        print(f"Updating thermostat temperature: {temperature}")
        thermostat.set_temperature(int(float(temperature)))
        self.thermo_temp_value_label.config(text=f"Temperature: {thermostat.temperature}°C")  # Update temperature label
        self.update_status_text()

    def toggle_thermostat(self):
        print("Toggling thermostat")
        if thermostat.status == 'off':
            thermostat.turn_on()
        else:
            thermostat.turn_off()
        self.update_status_text()

    def toggle_camera(self):
        print("Toggling camera")
        if camera.status == 'off':
            camera.turn_on()
        else:
            camera.turn_off()
        self.update_status_text()

    def random_detect_motion(self):
        print("Random motion detection")
    # This method would be connected to the security camera to simulate motion detection
        camera.security_status = 'alert' if camera.security_status == 'normal' else 'normal'
        self.update_status_text()
    # Implement the automation rule (turn on lights when motion is detected)
        if camera.security_status == 'alert':
            smart_light.turn_on()
        self.update_status_text()


# Run the application
root = tk.Tk()
app = SmartHomeApp(root)
root.mainloop()
