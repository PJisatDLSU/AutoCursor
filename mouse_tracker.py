import time
import pyautogui
from pynput import mouse

def track_mouse(app):
    """Tracks mouse movements and clicks, storing them in app.track_data."""
    print("Tracking mouse...")
    app.track_data = []  # Reset previous data

    def on_click(x, y, button, pressed):
        """Handles mouse click events."""
        if pressed:  # Only record when the button is pressed down
            timestamp = time.time()
            button_type = "left" if button == mouse.Button.left else "right"
            app.track_data.append((x, y, timestamp, button_type))  # Store click event

    listener = mouse.Listener(on_click=on_click)
    listener.start()  # Start listening for clicks

    while app.recording:
        x, y = pyautogui.position()  # Get cursor position
        timestamp = time.time()  # Get current time
        app.track_data.append((x, y, timestamp, None))  # Store movement without click

        time.sleep(0.01)  # Prevent CPU overload

    listener.stop()  # Stop the listener
    print("Tracking stopped.")

FAST_FORWARD_FACTOR = 10

def replay_mouse(app):
    """Replays recorded mouse movements and clicks at accelerated speed."""
    if not app.track_data:
        print("No data recorded.")
        return

    print("Replaying started...")

    loop_count = 0  
    step = max(1, int(len(app.track_data) / (FAST_FORWARD_FACTOR * 10)))  # Skip movement points dynamically

    while app.replaying:
        loop_count += 1  
        print(f"Loop #{loop_count} started...")  

        start_time = app.track_data[0][2]  
        playback_start = time.time()  

        for i in range(len(app.track_data)):  # Don't skip over clicks
            x, y, timestamp, click = app.track_data[i]

            if not app.replaying:  
                print("Replaying stopped.")
                return

            elapsed_time = (timestamp - start_time) / FAST_FORWARD_FACTOR
            target_time = playback_start + elapsed_time
            current_time = time.time()
            delay = target_time - current_time

            if delay > 0:
                time.sleep(delay / FAST_FORWARD_FACTOR)  

            # Only move mouse every 'step' frames to speed up movement
            if i % step == 0 or click is not None:  
                pyautogui.moveTo(x, y, duration=0)  

            # Ensure clicks are never skipped
            if click == "left":
                pyautogui.click()
                print(f"Left click at ({x}, {y})")
            elif click == "right":
                pyautogui.rightClick()
                print(f"Right click at ({x}, {y})")

        print(f"Loop #{loop_count} completed. Restarting...")

    print("Replaying stopped.")

