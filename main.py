import pyautogui
import pyperclip
import pyttsx4
import tkinter as tk
import multiprocessing as m
import time
class Reader:
    
    def __init__(self):
       
        self.process = None
        self.speed = 45
        self.speed_change_var = 6

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
        self.Go_to_prev_window()
        time.sleep(0.01)  # Give the OS a moment to switch focus
        self.Copy()
        time.sleep(0.01)
        self.Go_to_prev_window()
        

        text_paceholder = str(pyperclip.paste())
        text = " ".join(text_paceholder.splitlines())
        print(f"Reading: {text}")

        if text.strip():
            # Pass the function and arguments separately              change speed here;;;;;;;;;;;;;
            self.process = m.Process(target=self._read_task, args=(text, self.speed))
            self.process.start()
            
    def Copy(self):
            pyautogui.keyDown('ctrl')
            pyautogui.hotkey( 'c')
            pyautogui.keyUp('ctrl')
            
    def Go_to_prev_window(self):
        pyautogui.keyDown('alt')
        pyautogui.hotkey( 'tab')
        pyautogui.keyUp('alt')

    def stop_reading(self):
        if self.process and self.process.is_alive():
            self.process.terminate()
            self.process.join()
            print("Reading stopped.")
            
            
    def inc_speed(self):
        self.speed +=self.speed_change_var
        self.main_reader_operation()
    
    def dec_speed(self):
        self.speed -= self.speed_change_var
        self.main_reader_operation()
        

def main():
    # Multiprocessing on Windows requires this inside the entry point
    m.freeze_support() 

    reader_instance = Reader()
    
    root = tk.Tk()
    root.title("Reader v0.0.2")
    root.geometry("60x90")
    root.attributes("-topmost", True) # Keep it on top for easier use

    tk.Label(root, text="Reader", pady=10).pack()
    
    tk.Button(root, text="Read ", 
              command=reader_instance.main_reader_operation, 
              width=20, height= 3, bg="green", fg="white").pack(pady=5)
    
    tk.Button(root, text="+speed ", 
              command=reader_instance.inc_speed, 
              width=10, height= 2, bg="green", fg="white").pack(pady=5)
    tk.Button(root, text="-speed ", 
              command=reader_instance.dec_speed, 
              width=10, height= 2, bg="green", fg="white").pack(pady=5)
    tk.Button(root, text="Stop ", 
              command=reader_instance.stop_reading, 
              width=20, height= 3, bg="red", fg="white").pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
