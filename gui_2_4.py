import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from PIL import Image

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Fingerprint Matching")
        master.geometry("400x400")

        # Create widgets
        self.upload_button = tk.Button(master, text="Upload", command=self.upload_file)
        self.preprocess_button = tk.Button(master, text="Preprocess", command=self.preprocess)
        self.background_remove_button = tk.Button(master, text="Background Remove", command=self.background_remove)
        self.sift_detect_button = tk.Button(master, text="Sift Detect", command=self.sift_detect)
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_app)
        self.textbox = tk.Text(master, height=15, width=50)
        self.image_label = tk.Label(master)

        # Position widgets
        self.upload_button.pack(pady=10)
        self.textbox.pack(pady=10)
        self.quit_button.pack(side=tk.BOTTOM, padx=5, pady=10)
        self.background_remove_button.pack(side=tk.LEFT, padx=5, pady=10)
        self.preprocess_button.pack(side=tk.RIGHT, padx=5, pady=10)
        self.sift_detect_button.pack(side=tk.RIGHT, padx=5, pady=10)

        self.image_path = ""

    def upload_file(self):
        # Open file dialog to select a file
        file_path = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("all files", "*.*")))

        if file_path:
            self.textbox.insert(tk.END, f"->File {file_path} uploaded successfully\n")
            self.image_path = file_path
            # Open the image file and display in a separate window
            img = Image.open(file_path)
            img.show()
        else:
            self.textbox.insert(tk.END, "->No file selected\n")
    
    def preprocess(self):
        # Check if an image has been uploaded
        if not self.image_path:
            messagebox.showerror("Error", "No image selected.")
            return
        
        self.textbox.insert(tk.END,"->Preprocessing image...\n")
        subprocess.run(["python", "preprocess.py", self.image_path], check=True)
        self.textbox.insert(tk.END,"->Preprocessing completed.\n")
        
    
    def background_remove(self):
        # Check if an image has been uploaded
        if not self.image_path:
            messagebox.showerror("Error", "No image selected.")
            return
        
        self.textbox.insert(tk.END,"->Removing background...\n")
        subprocess.run(["python", "background_remove.py", self.image_path], check=True)
        self.textbox.insert(tk.END, "->Background removal completed.\n")
        
    
    def sift_detect(self):
        # Check if an image has been uploaded
        if not self.image_path:
            messagebox.showerror("Error", "No image selected.")
            return
        
        self.textbox.insert(tk.END,"->Detecting SIFT features...\n")
        subprocess.run(["python", "sift_detect.py", self.image_path], check=True)
        self.textbox.insert(tk.END,"->SIFT detection completed.\n")

    def quit_app(self):
        # Show confirmation dialog before quitting
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.master.destroy()

# Create the GUI window
root = tk.Tk()
gui = GUI(root)
root.mainloop()
