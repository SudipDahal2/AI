'''Lab 1 (Python): Reflex-based Intelligent Agent
Objective:
To design and implement reflex-based intelligent agents that make real-time decisions based on percepts from dynamic environments, such as traffic flow and presence detection.
To simulate environment-agent interaction using Python, demonstrating how agents can control systems like traffic signals and smart home lighting based on simple condition–action rules.'''

import random

class TrafficEnvironment:
    def __init__(self):
        self.traffic_density = "low"
        self.timer = 0
        self.light = "Red"
    
    def get_percept(self):
        return self.traffic_density, self.timer, self.light
    
    def update_environment(self):
        # Simulate changes in traffic density and timer
        self.traffic_density = random.choice(["low", "high"])
        self.timer += 1
    
    def execute_action(self, action):
        if action == "SwitchToGreen":
            self.light = "Green"
            self.timer = 0
            print("Action: Switched to Green Light")
        elif action == "SwitchToRed":
            self.light = "Red"
            self.timer = 0
            print("Action: Switched to Red Light")
        else:
            self.light = "Yellow"
            self.timer = 0
            print("Action: Switched to Yellow Light")
class TrafficAgent:


    def decide(self, traffic_density, timer, light):
        if light == "Red" and traffic_density == "high":
            return "SwitchToGreen"
        elif light == "Green" and traffic_density == "low":
            return "SwitchToYellow"
        else:
           return "Yellow Light Get Ready"

#Case 2: Smart Light AUtomation System

class RoomEnvironment:
    def __init__(self):
        self.presence = False
        self.time = "Day"
        self.light = "Off"

    def get_percept(self):
        return self.presence, self.time, self.light
    
    def update_environment(self):
        self.presence = random.choice([True, False])
        self.time = random.choice(["Day", "Night"])

    def execute_action(self, action):
        if action == "TurnOn":
            self.light = "On"
            print("Action: Light Turned on")
        elif action == "TurnOff":
            self.light = "Off"
            print("Action: Light Turned Off")
        else:
            print("Action: No Change in Light State")

        