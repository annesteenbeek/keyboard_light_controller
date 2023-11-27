import time
import paho.mqtt.client as mqtt
from pynput import keyboard


address = "192.168.172.46"
topics = {
  "brighten": "lights/bedroom/brighten",
  "dim": "lights/bedroom/dim",
  "toggle": "lights/bedroom/toggle",
}

class KeyboardListener:
  def __init__(self):
    self.listener = keyboard.Listener(on_press=self.on_press)
    self.listener.start()
    self.client = mqtt.Client()

    self.client.on_connect = self.on_connect
    self.client.on_disconnect = self.on_disconnect

    self.client.connect(address, 1883, 60)

  def on_connect(self, client, userdata, flags, rc):
    print("connected")

  def on_disconnect(self, client, userdata, rc):
    print("disconnected")

  def publish(self, task: str):
    self.client.publish(topics[task], task)
    print(task)

  def on_press(self, key):
    if key == keyboard.Key.f21:
      self.publish("dim")
    if key == keyboard.Key.f22:
      self.publish("brighten")
    if key == keyboard.Key.f23:
      self.publish("toggle")

  def run(self):
    self.client.loop_forever()

if __name__ == "__main__":
  listener = KeyboardListener()
  listener.run() 