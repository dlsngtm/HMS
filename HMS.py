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


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ==============================Dataframe==============================
        DataFrame=Frame(self.root, bd=20, padx=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                                                   font=("times new roman", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10,
                                                   font=("times new roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=980, y=5, width=460, height=350)

        # ==============================Buttonsframe==============================

        Buttonframe=Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1450, height=70)

        # ==============================Detailsframe==============================

        Detailsframe=Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1450, height=140)

        # ==============================DataframeLeft==============================

        lblNameTablet=Label(DataFrameLeft, text="Names of Tablet:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNametablet=ttk.Combobox(DataFrameLeft, textvariable=self.Nameoftablets, state="readonly",
                                                        font=("arial", 12, "bold"), width=33)

        comNametablet["values"]=("Nice", "Corona Vaccine", "Acetaminophan", "Adderall", "Amlodopine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)
        
        lblDose=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNooftablets=Label(DataFrameLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNooftablets.grid(row=3, column=0, sticky=W)
        txtNooftablets=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.NumberofTablets, width=35)
        txtNooftablets.grid(row=3, column=1)

        lblLot=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Issuedate, width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect=Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.sideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.FurtherInformation, width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblDrivingMachine=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblDrivingMachine.grid(row=1, column=2, sticky=W)
        txtDrivingMachine=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.DrivingUsingMachine, width=35)
        txtDrivingMachine.grid(row=1, column=3)

        lblStorage=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblHowToUseMedication=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblHowToUseMedication.grid(row=3, column=2, sticky=W)
        txtHowToUseMedication=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.HowToUseMedication, width=35)
        txtHowToUseMedication.grid(row=3, column=3, sticky=W)

        lblPatientId=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber=Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.PatientName, width=35)
        txtPatientname.grid(row=6, column=3)

        lblDateofBirth=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2, pady=6)
        lblDateofBirth.grid(row=7, column=2, sticky=W)
        txtDateofBirth=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.DateOfBirth, width=35)
        txtDateofBirth.grid(row=7, column=3)

        lblPatientAddress=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress=Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ==============================DataframeRight==============================
        self.txtPrescription=Text(DataFrameRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ==============================Buttons==============================
        btnPrescription=Button(Buttonframe, text="Prescription", bg="black", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData=Button(Buttonframe, text="Prescription Data", bg="black", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate=Button(Buttonframe, text="Update", bg="black", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete=Button(Buttonframe, text="Delete", bg="black", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear=Button(Buttonframe, text="Clear", bg="black", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit=Button(Buttonframe, text="Exit", bg="black", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # ==============================Table==============================
        # ===============Scrollbar===============
        scroll_x=ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hms_table=ttk.Treeview(Detailsframe, column=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate",
                                    "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hms_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hms_table.yview)

        self.hms_table.heading("nameoftable", text="Name of Table")
        self.hms_table.heading("ref", text="Reference No.")
        self.hms_table.heading("dose", text="Dose")
        self.hms_table.heading("nooftablets", text="No of Tablets")
        self.hms_table.heading("lot", text="Lot")
        self.hms_table.heading("issuedate", text="Issue Date")
        self.hms_table.heading("expdate", text="Exp Date")
        self.hms_table.heading("dailydose", text="Daily Dose")
        self.hms_table.heading("storage", text="Storage")
        self.hms_table.heading("nhsnumber", text="NHS Number")
        self.hms_table.heading("pname", text="Patient Name")
        self.hms_table.heading("dob", text="DOB")
        self.hms_table.heading("address", text="Address")

        self.hms_table["show"]="headings"

        self.hms_table.pack(fill=BOTH, expand=1)

        self.hms_table.column("nameoftable", width=100)
        self.hms_table.column("ref", width=100)
        self.hms_table.column("dose", width=100)
        self.hms_table.column("nooftablets", width=100)
        self.hms_table.column("lot", width=100)
        self.hms_table.column("issuedate", width=100)
        self.hms_table.column("expdate", width=100)
        self.hms_table.column("dailydose", width=100)
        self.hms_table.column("storage", width=100)
        self.hms_table.column("nhsnumber", width=100)
        self.hms_table.column("pname", width=100)
        self.hms_table.column("dob", width=100)
        self.hms_table.column("address", width=100)

        self.hms_table.pack(fill=BOTH, expand=1)

        # ==============================Functionality Declaration==============================
        




root = Tk()
ob = HMS(root)
root.mainloop()
