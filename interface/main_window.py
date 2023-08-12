"""
This is a basic example of a GUI using the tkinter framework. 
This example uses a few buttons that could be useful in our project.
The goal is to add several windows in the GUI so that you can see what the AI is doing.
It should look something like a security camera monitor.
"""

import tkinter as tk

class MyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("My Window")
        
        # Create and configure widgets
        self.label = tk.Label(self.root, text="Hello, World!")
        self.label.pack()
        
        # Button with a command
        self.button = tk.Button(self.root, text="Click Me", command=self.button_clicked)
        self.button.pack()
        
        # Button with a custom style
        self.custom_button = tk.Button(self.root, text="Custom Style", bg="blue", fg="white", font=("Arial", 12))
        self.custom_button.pack()
        
        # Checkbutton
        self.check_var = tk.BooleanVar()
        self.checkbutton = tk.Checkbutton(self.root, text="Check", variable=self.check_var)
        self.checkbutton.pack()
        
        # Radiobuttons
        self.radio_var = tk.StringVar()
        self.radio_var.set("Option 1")
        
        self.radio_button1 = tk.Radiobutton(self.root, text="Option 1", variable=self.radio_var, value="Option 1")
        self.radio_button1.pack()
        
        self.radio_button2 = tk.Radiobutton(self.root, text="Option 2", variable=self.radio_var, value="Option 2")
        self.radio_button2.pack()
        
        # Entry
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_var)
        self.entry.pack()
        
        # Text widget
        self.text = tk.Text(self.root, height=5, width=30)
        self.text.pack()
        
        # Duplicates of buttons and text with different styles
        self.button2 = tk.Button(self.root, text="Click Me 2", bg="green", fg="white", font=("Arial", 12))
        self.button2.pack()
        
        self.custom_button2 = tk.Button(self.root, text="Custom Style 2", bg="red", fg="white", font=("Arial", 12, "bold"))
        self.custom_button2.pack()
        
        self.text2 = tk.Text(self.root, height=3, width=20, bg="yellow", fg="black")
        self.text2.pack()
        
    def button_clicked(self):
        print("Button clicked!")
        
    def run(self):
        self.root.mainloop()

# Create the Tkinter window and run the application
root = tk.Tk()
window = MyWindow(root)
window.run()