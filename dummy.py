import pyautogui
import pyperclip
import pyttsx4
import tkinter as tk
import multiprocessing as m

def main():
    text = ""
    speed= 28

    class reader:
        def __init__(self):
            self.process = None
        
        def Main_Reader_Operation(self):
            # copy text
            self.Go_to_prev_window()
            self.Copy()
            self.Go_to_prev_window()
            # paste text
            text= str(pyperclip.paste())
            self.process=m.Process(self._read(text)) 
            print(text)
            # say text
            self.process.start()
            
        
            
        def stop_reading(self):
            if self.process and self.process.is_alive:
                self.process.terminate()
                self.process.join()
            #fuck this lib
            
        def Copy(self):
            pyautogui.keyDown('ctrl')
            pyautogui.hotkey( 'c')
            pyautogui.keyUp('ctrl')
            
        def Go_to_prev_window(self):
            pyautogui.keyDown('alt')
            pyautogui.hotkey( 'tab')
            pyautogui.keyUp('alt')
            
        
        def _read(self,text):
            # engine.startLoop
            engine = pyttsx4.init()
            engine.setProperty('rate',speed*10)
            engine.say(text)
            engine.runAndWait()
        
    # with m.Pool() as pool:
    #     pool.map(read)


    reeader= reader()
    root= tk.Tk()
    root.geometry("300x500")
    label = tk.Label(root, text="reader v0.0.2",)
    label.pack()
    button = tk.Button(root,text = "read", command= reeader.Main_Reader_Operation)
    button.pack()
    button = tk.Button(root,text = "stop", command= reeader.stop_reading)
    button.pack()
    root.mainloop()
    
    # reeader.Main_Reader_Operation()
    app_name = None
    read_button = None
    stop_button = None
    
    # Main_Reader_Operation()
        
        
  
if __name__ == '__main__':
     main()
