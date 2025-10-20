# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:49:19 2025

@author: 91956
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:37:18 2025

@author: 91956
"""

import time

# Define OSI layers
osi_layers = [
    "Application Layer",
    "Presentation Layer",
    "Session Layer",
    "Transport Layer",
    "Network Layer",
    "Data Link Layer",
    "Physical Layer"
]

# Sample message
message = "HELLO FROM SENDER"

# Function to simulate encapsulation (sender side)
def encapsulate(data):
    print("\n--- ENCAPSULATION (Sender Side) ---\n")
    for layer in osi_layers:
        data = f"[{layer} Header + {data}]"
        print(f"Passing through {layer} → Data becomes:\n{data}\n")
        time.sleep(1)
    return data

# Function to simulate decapsulation (receiver side)
def decapsulate(data):
    print("\n--- DECAPSULATION (Receiver Side) ---\n")
    for layer in reversed(osi_layers):
        print(f"At {layer} → Removing {layer} Header")
        data = data.replace(f"[{layer} Header + ", "")
        data = data[:-1]  # remove trailing ']'
        print(f"Remaining data: {data}\n")
        time.sleep(1)
    return data

# Simulate the process
print("SENDER preparing message...")
time.sleep(1)
packet = encapsulate(message)

print("Transmitting data through physical medium...\n")
time.sleep(1.5)

print("RECEIVER receiving message...")
time.sleep(1)
received_data = decapsulate(packet)

print(f"Final message received at Application Layer: '{received_data}'")
