from gui_1_2 import GUI
from remove_back import removeBackground
from preprocess import process
import sys

#import runMatcher
import tkinter as tk
from tkinter import filedialog, messagebox

sys.path.insert(0, '/Users/chandrakiran/Downloads/Finger_Print/output')
from sift_detect import runMatcher

class fingerPrintMatcher(GUI,removeBackground, process, runMatcher):
    def _init_(self, master):
        self.image_path= ""
        self.bgRemovedFile = ""
        self.processedFile = ""
        self.output = ""
        self.IsMatch = False

    def runGUI(self):
        self.run()

root = tk.Tk()
obj = fingerPrintMatcher(root)
obj.run()






    
    