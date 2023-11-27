# Light controller
This little script is used to controll my room lights from my keychron knob

The knob is mapped to F21(left) F22(right) and F23 (press).

In homeassistant there are MQTT automations that brighten dim and toggale the lights.

The main.py script is run in the background in order to monitor the keys.

## Windows
In windows I'm using the task scheduuler to call pythonw.exe main.py on startup.

