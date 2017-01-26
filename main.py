# -*- coding: utf-8 -*-


import sys

# check if we are running python 3.x or python 2.x 
if sys.version_info[0] >= 3:
    # for python 3.x
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter.colorchooser import askcolor
else:
    # for python 2.x
    import Tkinter as tk
    import ttk
    from tkColorChooser import askcolor



class MainApp(tk.Frame):
    
    def __init__(self, master):
        """
        This is the Main Window for our applicaiton. This Creates a frame
        which will hold our application information 
        """
        tk.Frame.__init__(self, master=master)
        self.pack(side="top", fill="both", expand=True)
        
        self.buttons = []        
        
        self.buttons.append(ColorButton(self, "Button 1", [lambda x: print_color(x, "1")]))
        self.buttons.append(ColorButton(self, "Button 2", [lambda x: print_color(x, "2")]))
        self.buttons.append(ColorButton(self, "Button 3", [lambda x: print_color(x, "3")]))
        self.buttons.append(ColorButton(self, "Button 4", [lambda x: print_color(x, "4")]))
        
        for btn in self.buttons:
            btn.pack()
        
class ColorButton(tk.Frame):
    
    def __init__(self, master=None, btn_text="", callbacks=[]):
        """
        Tkinter widget containing a button and a canvas side by side that
        can then change its color
        
        NB callbacks take a color
        """
        tk.Frame.__init__(self, master=master)
        
        self.button = ttk.Button(master=self, text=btn_text, command=self._btn1)
        self.button.pack(side="left", padx=2, pady=2)
        
        self.canvas = tk.Canvas(master=self, width=20, height=20, relief="flat")
        self.canvas.pack(side="left", padx=2, pady=2)
        
        self.rect = self.canvas.create_rectangle(0, 0, 20 ,20, fill="white")
        
        # set up a dictionary of callbacks to be run when the button is pressed
        self._callbacks = {} # callback dictionary 
        self._cur_cbh = 0 # current callback handel
        
        for callback in callbacks:
            self.register_call(callback)
        
    def change_color(self, color):
        self.canvas.itemconfig(self.rect, fill=color)
  
    def _btn1(self):
        mycolor = askcolor()
        self.change_color(mycolor[-1])
        for callback in self._callbacks:
            # run all registred callbacks with the color
            self._callbacks[callback](mycolor)
        
    def register_call(self, callback):
        """
        register a callback for the button press
        """
        self._callbacks[self._cur_cbh] = callback
        cbh = self._cur_cbh
        self._cur_cbh += 1
        
        return cbh
        
    def unregister_call(self, cbh):
        """
        unregister a callback by its handle
        """
        return self._callbacks.pop(cbh, None)

def print_color(color, btn=""):
    print("Button {} color is {}".format(btn, color[-1]))
        
        
def color_btn_program():
    """
    Function to encapsulate starting the Application
    """
    
    root = tk.Tk()
    root.title("Color Changer Application") # Change the window title
    root.geometry("200x200") # set the defualt size to be 200x200 pixels 
    
    app = MainApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    color_btn_program()
    
