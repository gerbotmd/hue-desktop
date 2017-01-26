import Tkinter as tk
import ttk
#from Tkinter.colorchooser import askcolor
from tkColorChooser import askcolor

# mainapp makes a frame
class MainApp(tk.Frame):

    def __init__(self, master):
        #super().__init__(master=master)
        tk.Frame.__init__(self, master=master)
        self.pack(side='top', fill='both', expand=True)

        self.buttons = []

        self.buttons.append(tk.Button(master=self, text='Button 1', command=self.btn1))
        self.buttons.append(tk.Button(master=self, text='Button 2', command=self.btn2))
        self.buttons.append(tk.Button(master=self, text='Button 3', command=self.btn3))
        self.buttons.append(tk.Button(master=self, text='Button 4', command=self.btn4))

        for btn in self.buttons:
            btn.pack()

        # button1 = tk.Button(master=self, text='chill', command=self.btn1)
        # button1.pack()

        # button1 = tk.Button(master=self, text='intense', command=self.btn2)
        # button1.pack()

        # button1 = tk.Button(master=self, text='solid', command=self.btn3)
        # button1.pack()

        # button1 = tk.Button(master=self, text='blackout', command=self.btn4)
        # button1.pack()

    def btn1(self):
        print('button 1')
        mycolor = askcolor()
        print mycolor
        self.buttons[0].configure(fg='#ff00e0')

    def btn2(self):
        print('button 3')

    def btn3(self):
        print('button 4')

    def btn4(self):
        print('button 4')

# class ColorButton(tk


root = tk.Tk()
app = MainApp(root)

root.mainloop()


# #Create & Configure root 
# root = Tk()
# Grid.rowconfigure(root, 0, weight=1)
# Grid.columnconfigure(root, 0, weight=1)
# 
# #Create & Configure frame 
# frame=Frame(root)
# frame.grid(row=0, column=0, sticky=N+S+E+W)
# 
# #Create a 5x10 (rows x columns) grid of buttons inside the frame
# for row_index in range(5):
#     Grid.rowconfigure(frame, row_index, weight=1)
#     for col_index in range(10):
#         Grid.columnconfigure(frame, col_index, weight=1)
#         btn = Button(frame) #create a button inside frame 
#         btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)  
# 
# root.mainloop()
