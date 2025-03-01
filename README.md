# AutoCursor

AutoCursor is a Python-based automation tool that records and replays mouse movements and clicks, making it ideal for repetitive tasks. This project was initially developed to automate marking emails as "read" across 16,000+ pages but is flexible enough for various automation needs.

## Features
- **Record Mouse Movements & Clicks** – Tracks exact cursor positions and mouse clicks.
- **Replay Movements Infinitely** – Loops the recorded actions until manually stopped.
- **Fast-Forward Capability** – Adjust playback speed to optimize automation efficiency.
- **Customizable Automation** – Works for tasks beyond email automation, such as UI testing or workflow automation.

## Requirements
Ensure you have Python installed along with the following libraries:
```bash
pip install pyautogui pynput
```

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/PJisatDLSU/AutoCursor.git
   cd AutoCursor
   ```
2. Install the required dependencies:
   ```bash
   pip install pyautogui pynput
   ```

## How to Use

### **1️⃣ Start the Program**
Run the main script to begin tracking or replaying mouse movements:
```bash
python userInterface.py
```

### **2️⃣ Recording Mouse Movements**
- Press **'x'** to start recording mouse movements & clicks.
- Move the mouse as needed and perform the required clicks.
- Press **'x'** again to stop recording.

### **3️⃣ Replaying Mouse Movements**
- Press **'z'** to start replaying the recorded sequence.
- The program will continuously loop through the recorded actions.
- Press **'z'** again to stop the replay.

### **4️⃣ Customizing Speed**
- The replay speed can be adjusted by modifying `FAST_FORWARD_FACTOR` in `mouse_tracker.py`.

## Use Cases
- Automating tedious UI interactions (e.g., processing large numbers of emails).
- Repetitive form-filling or data entry.
- Software testing for UI interactions.

## License
This project is open-source under the MIT License.

