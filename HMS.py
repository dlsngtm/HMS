from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class HMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ==============================Dataframe==============================
        DataFrame=Frame(self.root, bd=20, padx=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                                                   font=("times new roman", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=840, height=350)

        DataFrameRight=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                                                   font=("times new roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=840, y=5, width=460, height=350)

        # ==============================Buttonsframe==============================

        Buttonframe=Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1450, height=70)

        # ==============================Detailsframe==============================

        Detailsframe=Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1450, height=140)



root = Tk()
ob = HMS(root)
root.mainloop()
