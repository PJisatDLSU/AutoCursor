import tkinter as tk
import keyboard
import threading
from mouse_tracker import track_mouse, replay_mouse

class AutoCursorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Interface")
        self.root.geometry("300x150")
        self.root.attributes('-topmost', True)

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        self.labels = ["Play/Stop", "Record/Stop"]
        self.keys = ["z", "x"]
        self.squares = {}
        self.recording = False
        self.replaying = False
        self.track_data = []

        self.setup_ui()
        self.listen_for_keys()

    def setup_ui(self):
        for i, (label, key) in enumerate(zip(self.labels, self.keys)):
            square = tk.Label(self.frame, text=label, width=10, height=4, bg="gray", relief="raised", font=("Roboto", 10, "bold"))
            square.grid(row=0, column=i, padx=10, pady=10)
            self.squares[key] = square

    def toggle_color(self, key):
        """Toggle square color and trigger tracking functions."""
        if key in self.squares:
            current_color = self.squares[key].cget("bg")
            new_color = "green" if current_color == "gray" else "gray"
            self.squares[key].config(bg=new_color)

            if key == "x":  # Toggle Recordingxxz
                self.recording = not self.recording
                if self.recording:
                    self.track_data = []
                    threading.Thread(target=track_mouse, args=(self,), daemon=True).start()
                else:
                    print("Recording stopped.")

            elif key == "z":  # Toggle Replaying
                self.replaying = not self.replaying
                if self.replaying:
                    threading.Thread(target=replay_mouse, args=(self,), daemon=True).start()
                else:
                    print("Replaying stopped.")

    def listen_for_keys(self):
        """Start a separate thread to listen for key presses."""
        def key_listener():
            while True:
                event = keyboard.read_event(suppress=False)
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == "c":
                        self.root.quit()
                    elif event.name in self.keys:
                        self.root.after(0, self.toggle_color, event.name)

        threading.Thread(target=key_listener, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoCursorApp(root)
    root.mainloop()
