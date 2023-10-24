import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from PIL import Image, ImageTk
import os

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Fingerprint Match")
        master.geometry("500x300")

        # Create widgets
        self.upload_button = tk.Button(master, text="Select fingerprint to match", command=self.upload_file)
        self.match_button = tk.Button(master, text="Match", command=self.match)
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_app)
        self.textbox = tk.Text(master, height=15, width=50)
        self.image_label = tk.Label(master)
        #self.message_box = tk.Label(master, text="",height=15, width=50)

        # Position widgets
        self.textbox.pack( pady=10)
        self.upload_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.match_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.quit_button.pack(side=tk.RIGHT, padx=5, pady=10)

        #self.image_path = ""

    def upload_file(self):
        # Open file dialog to select a file
        file_path = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("all files", "*.*")))

        if file_path:
            self.textbox.insert(tk.END, f"File {file_path} uploaded successfully\n")
            self.image_path = file_path
            # Open the image file and display in a separate window
            #img = Image.open(file_path)
            #img.show()
        else:
            self.textbox.insert(tk.END, "No file selected\n")
    
    def match(self):
        self.textbox.insert(tk.END, "\n\nSTEP1: Running backgound removal process....")
        self.remove()
        self.textbox.insert(tk.END, "\n\n       Succesfully removed background")
        self.textbox.insert(tk.END, "\n\nSTEP2: Running furthur filtering operations....")
        self.filter()
        self.textbox.insert(tk.END, "\n\n       Succesfully filtered input fingerprint")
        self.textbox.insert(tk.END, "\n\nSTEP3: Running matching algorithm....")
        self.checkDB()
        
        # self.textbox.insert(tk.END, f"File {file_path} uploaded successfully\n")
        if self.IsMatch:
            self.textbox.insert(tk.END, "\n\n       ******** Finger print is matched ********\n")
        else:
            self.textbox.insert(tk.END, "\n\n       ******** No matching fingerprint ********\n")


    def quit_app(self):
        # Show confirmation dialog before quitting
        #if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        self.master.destroy()

    def run(self):
        # Create the GUI window
        #root = tk.Tk()
        #gui = GUI(root)
        self.master.mainloop()
