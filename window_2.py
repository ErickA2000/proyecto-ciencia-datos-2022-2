from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd

def main(df):
    window_2 = Tk()
    print('column: ', df['sex'])
    #window_2.mainloop()