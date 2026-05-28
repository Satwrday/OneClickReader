import pyautogui
import pyperclip
import pyttsx4
import tkinter as tk
import multiprocessing as m
import time
class Reader:
    
    def __init__(self):
       
        self.process = None
        self.speed = 35
        self.speed_change_var = 4

    def _read_task(self, text,speed):
        # Engine must be initialized inside the new process
        engine = pyttsx4.init()
        engine.setProperty('rate', speed * 10)
        engine.setProperty('volume', 0.9)
        engine.say(text)
        engine.runAndWait()

    def main_reader_operation(self):
        # Stop any existing speech before starting new
        self.stop_reading()

        # Switch to previous window, copy, and switch back
        self.Go_to_prev_window()
        # time.sleep(0.01)  # Give the OS a moment to switch focus
        self.Copy()
        # time.sleep(0.01)
        #self.Go_to_prev_window()
        

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
    
    def image_copy(self):
        pyautogui.keyDown('win')
        pyautogui.keyDown('shift')
        pyautogui.hotkey('t')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('win')
        
    def image_read(self):
        # # Stop any existing speech before starting new
        self.stop_reading()

        # # Switch to previous window, copy, and switch back
        # self.Go_to_prev_window()
        # # time.sleep(0.01)  # Give the OS a moment to switch focus
        # self.Copy()
        # # time.sleep(0.01)
        self.Go_to_prev_window()
        

        text_paceholder = str(pyperclip.paste())
        text = " ".join(text_paceholder.splitlines())
        print(f"Reading: {text}")

        if text.strip():
            # Pass the function and arguments separately              change speed here;;;;;;;;;;;;;
            self.process = m.Process(target=self._read_task, args=(text, self.speed))
            self.process.start()

def main():
    # Multiprocessing on Windows requires this inside the entry point
    m.freeze_support() 

    reader_instance = Reader()
    
    root = tk.Tk()
    #root.attributes("-toolwindow", True)
    root.title("One Click Reader v0.1.01 Q-+iqx ")
    root.geometry("320x30")

    
    #vim mode edits
    root.attributes("-topmost", True) # Keep it on top for easier use

    # tk.Label(root, text="Highlight Text -> Click Read", pady=0.5).pack(side="bottom")
    
    tk.Button(root, text="t.Read ", 
              command=reader_instance.main_reader_operation, 
              width=10, height= 3, bg="green", fg="white").pack(side="left")
    
    
    root.bind_all("Q", lambda e : reader_instance.main_reader_operation())
    root.bind_all("q", lambda e : reader_instance.image_read())
    
    tk.Button(root, text="-Speed ", 
              command=reader_instance.dec_speed, 
              width=5, height= 3, bg="green", fg="white").pack(side="left")

    root.bind_all("-", lambda e : reader_instance.dec_speed())

    tk.Button(root, text="+Speed ", 
              command=reader_instance.inc_speed, 
              width=5, height= 3, bg="green", fg="white").pack(side="left")
    

    root.bind_all("+", lambda e : reader_instance.inc_speed())

    tk.Button(root, text="i.Copy ", 
              command=reader_instance.image_copy, 
              width=4, height= 3, bg="blue", fg="white").pack(side="left")
    root.bind_all("i", lambda e : reader_instance.image_copy())
    tk.Button(root, text="i.Read ", 
              command=reader_instance.image_read, 
              width=4, height= 3, bg="blue", fg="white").pack(side="left")
    tk.Button(root, text="Stop ", 
              command=reader_instance.stop_reading,  
              width=10, height= 3, bg="blue", fg="white").pack(side="left")
    
    root.bind_all("x", lambda e : reader_instance.stop_reading())

    root.mainloop()

if __name__ == '__main__':
    main()
