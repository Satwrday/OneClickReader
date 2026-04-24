import pyautogui
import pyperclip
import pyttsx4
import tkinter as tk
import multiprocessing as m
import time
class Reader:
    
    def __init__(self):
       
        self.process = None

    def _read_task(self, text,speed):
        # Engine must be initialized inside the new process
        engine = pyttsx4.init()
        engine.setProperty('rate', speed * 10)
        engine.say(text)
        engine.runAndWait()

    def main_reader_operation(self):
        # Stop any existing speech before starting new
        self.stop_reading()

        # Switch to previous window, copy, and switch back
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.1)  # Give the OS a moment to switch focus
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        pyautogui.hotkey('alt', 'tab')

        text = str(pyperclip.paste())
        print(f"Reading: {text}")

        if text.strip():
            # Pass the function and arguments separately
            self.process = m.Process(target=self._read_task, args=(text, 28))
            self.process.start()

    def stop_reading(self):
        if self.process and self.process.is_alive():
            self.process.terminate()
            self.process.join()
            print("Reading stopped.")

def main():
    # Multiprocessing on Windows requires this inside the entry point
    m.freeze_support() 

    reader_instance = Reader()
    
    root = tk.Tk()
    root.title("Reader v0.0.2")
    root.geometry("300x200")
    root.attributes("-topmost", True) # Keep it on top for easier use

    tk.Label(root, text="Simple TTS Reader", pady=10).pack()
    
    tk.Button(root, text="Read ", 
              command=reader_instance.main_reader_operation, 
              width=20, bg="green", fg="white").pack(pady=5)
    
    tk.Button(root, text="Stop ", 
              command=reader_instance.stop_reading, 
              width=20, bg="red", fg="white").pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
