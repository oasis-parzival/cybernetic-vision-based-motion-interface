# 🤖 Cybernetic Vision-Based Motion Interface

A real-time motion control system using computer vision and AI to interpret human body gestures as digital inputs. This project demonstrates how pose estimation can power gesture-controlled applications for gaming, UI interaction, and accessibility tools.

---

## 🧠 Overview

The Cybernetic Vision Interface leverages AI and camera-based vision systems to detect body poses and convert them into meaningful actions. It simulates input control (like keyboard or joystick events) using body movements, enabling natural and immersive control without physical devices.

---

## 🔧 Tech Stack

- **Python**
- **OpenCV** – for camera handling and frame processing
- **MediaPipe** – for real-time pose detection
- **pyvjoy** (or similar) – for simulating virtual joystick inputs *(optional)*
- **vJoy Driver** – for emulated joystick support *(optional)*

---

## 🚀 Features

- Real-time body pose detection using webcam
- Gesture-to-action mapping (e.g., hand up = jump)
- Cross-platform input simulation (game control, accessibility)
- Expandable for custom gestures and commands

---

## 🖥️ How It Works

1. The webcam captures live video feed.
2. MediaPipe detects body landmarks (hands, arms, shoulders, etc.).
3. Specific poses or movements are mapped to commands.
4. pyvjoy simulates the corresponding input to the system.

---

## 📁 Installation

1. git clone https://github.com/your-username/cybernetic-vision-interface.git
cd cybernetic-vision-interface
pip install -r requirements.txt

2. Install Python dependencies pip install -r requirements.txt

3. 🎮 Install vJoy Driver (for Virtual Joystick)
vJoy is required to simulate gamepad inputs.
Download from:
https://sourceforge.net/projects/vjoystick/
Run the installer and ensure vJoy Device 1 is enabled using vJoyConf.exe.
Restart your computer if prompted.

4. Install pyvjoy - pip install pyvjoy

5. 🎮 Map Controls in PPSSPP Emulator (for Tekken 6)
Launch PPSSPP Emulator.
Go to:
Settings > Controls > Control Mapping
Assign buttons to vJoy Device 1:
D-Pad → Movement (Up/Down/Left/Right)
Buttons like X, O, etc. → Punch/Kick actions
Save your mappings.
These button presses are triggered by body movements via code.

---

## 💡 How It Works (Under the Hood)

- **Webcam** captures real-time video stream.
- **MediaPipe** detects body landmarks (arms, head, torso).
- Code compares landmark positions to recognize gestures.
- Recognized gestures are **mapped to vJoy inputs** using `pyvjoy`.
- **PPSSPP Emulator** receives joystick input as if from a physical game controller.

---

## 🧪 Example Gesture Mappings

| Gesture        | Action in Game (via vJoy) |
|----------------|---------------------------|
| Left punch     | Button X                  |
| Right punch    | Button O                  |
| Crouch         | D-Pad Down                |
| Move forward   | D-Pad Right               |
| Move backward  | D-Pad Left                |

> 🛠️ You can modify gesture logic in `main.py`.


🧑‍💻 Author  
[Atharva Matale](https://www.linkedin.com/in/atharva-matale-428862354/)  
[GitHub](https://github.com/oasis-parzival)
