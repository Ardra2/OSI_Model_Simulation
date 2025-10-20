# OSI Model Simulation in Python

## Overview
This project simulates how a message travels through the **7 layers of the OSI model** — from the sender to the receiver — using Python.

It demonstrates **encapsulation** (adding headers) and **decapsulation** (removing headers) to help visualize how communication happens between systems.

---

##  OSI Layers Simulated
1. Application Layer  
2. Presentation Layer  
3. Session Layer  
4. Transport Layer  
5. Network Layer  
6. Data Link Layer  
7. Physical Layer  

---

##  How to Run
1. Open the file `osi_model_simulation.py` in **Spyder**, **VS Code**, or **Jupyter Notebook**.
2. Run the program.
3. Watch how data is processed through each OSI layer step-by-step.

---

##  Output Example

SENDER preparing message...

--- ENCAPSULATION (Sender Side) ---
Passing through Application Layer → Data becomes:
[Application Layer Header + HELLO FROM SENDER]

Passing through Presentation Layer → Data becomes:
[Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]

Passing through Session Layer → Data becomes:
[Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]

Passing through Transport Layer → Data becomes:
[Transport Layer Header + [Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]]

Passing through Network Layer → Data becomes:
[Network Layer Header + [Transport Layer Header + [Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]]]

Passing through Data Link Layer → Data becomes:
[Data Link Layer Header + [Network Layer Header + [Transport Layer Header + [Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]]]]

Passing through Physical Layer → Data becomes:
[Physical Layer Header + [Data Link Layer Header + [Network Layer Header + [Transport Layer Header + [Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]]]]]

Transmitting data through physical medium...

--- DECAPSULATION (Receiver Side) ---
At Physical Layer → Removing Physical Layer Header
Remaining data: [Data Link Layer Header + [Network Layer Header + [Transport Layer Header + [Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]]]]

At Data Link Layer → Removing Data Link Layer Header
Remaining data: [Network Layer Header + [Transport Layer Header + [Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]]]

At Network Layer → Removing Network Layer Header
Remaining data: [Transport Layer Header + [Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]]

At Transport Layer → Removing Transport Layer Header
Remaining data: [Session Layer Header + [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]]

At Session Layer → Removing Session Layer Header
Remaining data: [Presentation Layer Header + [Application Layer Header + HELLO FROM SENDER]]

At Presentation Layer → Removing Presentation Layer Header
Remaining data: [Application Layer Header + HELLO FROM SENDER]

At Application Layer → Removing Application Layer Header
Remaining data: HELLO FROM SENDER

Final message received at Application Layer: 'HELLO FROM SENDER'
---

##  Future Enhancements
- Add a graphical visualization using Matplotlib or Tkinter to show packet flow.
- Simulate real headers like TCP/IP, Ethernet frames, etc.
- Add interactivity to let users input their own message.
- Extend to show multiple packets or a simple network scenario.



##  Author
Ardra V Ganesh  
Electronics and Communication Engineering (Communication Systems Stream)
