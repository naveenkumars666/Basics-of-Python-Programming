#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Loan calculation system based on coletral
#Authored by Naveen Kumar S
#Date 15/3/2023
#version 0.5
#Pyhton code is case sensetive

#importing all the required libraries for GUI
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox #for drop down in the forms
import tkinter as tk

root=Tk()

#Displaying the title 
root.title("Loan application form")
root.geometry("800x700+300+200")
root.resizable(False,False)
root.configure(bg="#00B2EE")

#for clearing all the data entered..
def clear():
   nameValue.set('')
   contactValue.set('')
   AgeValue.set('')
   MonthlyValue.set('')
   MembersValue.set('')
   AdressEntry.delete(1.0,END)
   LoanValue.set('')
   IntrestValue.set('')
   MonthsValue.set('')
   
#function for calculating the monthly EMI based on loan amount,intrest rate and duration of repayment   
def empty():
   print("")
   
def pay2(rate):
       loan = int(LoanEntry.get())
       # Calculate The Loan
       # Monthly Interest Rate
       monthly_rate = rate / 100 / 12 
       # Get Our Payment
       payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
       # Format Payment
       payment = f"{payment:,.2f}"

       # Output Payment to the screen
       payment_label.config(text=f"Intrest Rate is {rate}%")
       payment_label1.config(text=f"Monthly EMI: Rs.{payment}")
       
   
def payment():
   if LoanEntry.get() and IntrestEntry.get() and MonthsEntry.get():
       # Convert Entry Boxes to numbers
       months = int(MonthsEntry.get())
       
       
       score = float(IntrestEntry.get())
       if score >=750 and score <=950:
           rate=12
           pay2(rate)
       elif score >=650 and score <750:
           rate=14
           pay2(rate)
       elif score >=550 and score <550:
           rate=16
           pay2(rate)
       elif score <550:
           payment_label1.config(text="You Are Not Elegible For a Loan")
           empty()
       elif score >950:
           payment_label1.config(text="Enter a valid credit score")
           empty()

       
   else:
       payment_label.config(text="Please enter all the details above")

#heading of the program
Label(root,text="Loan EMI Calculation System",font="arial 15",bg="#00008B",fg="#fff").place(x=250,y=10)

#label 
Label(root,text="Name Of Customer",font=23,bg="#48D1CC",fg="#fff").place(x=20,y=150)
Label(root,text="Contact No.",font=23,bg="#48D1CC",fg="#fff").place(x=50,y=200)
Label(root,text="DOB(DD/MM/YY)",font=23,bg="#48D1CC",fg="#fff").place(x=30,y=250)
Label(root,text="Gender",font=23,bg="#48D1CC",fg="#fff").place(x=380,y=250)
Label(root,text="Address as PAN",font=23,bg="#48D1CC",fg="#fff").place(x=40,y=300)
Label(root,text="Monthly Income",font=23,bg="#48D1CC",fg="#fff").place(x=50,y=350)
Label(root,text="Members in Family",font=23,bg="#48D1CC",fg="#fff").place(x=350,y=350)
Label(root,text="Collateral Name",font=23,bg="#48D1CC",fg="#fff").place(x=50,y=400)
Label(root,text="Loan/coletral Amount ",font=23,bg="#48D1CC",fg="#fff").place(x=10,y=450)
Label(root,text="Credit Score",font=13,bg="#48D1CC",fg="#fff").place(x=330,y=450)
Label(root,text="Months Required",font=23,bg="#48D1CC",fg="#fff").place(x=40,y=500)

#Entry
nameValue=StringVar() #constructor with widget to accept values
contactValue=StringVar()
AgeValue=StringVar()
MonthlyValue=StringVar()
MembersValue=StringVar()
LoanValue=StringVar()
IntrestValue=StringVar()
MonthsValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=45,bd=2,font=20)
contactEntry=Entry(root,textvariable=contactValue,width=45,bd=2,font=20)
ageEntry=Entry(root,textvariable=AgeValue,width=15,bd=2,font=20)
MonthlyEntry=Entry(root,textvariable=MonthlyValue,width=13,bd=2,font=20)
MembersEntry=Entry(root,textvariable=MembersValue,width=10,bd=2,font=20)
AdressEntry=Text(root,width=50,height=2,bd=4)
LoanEntry=Entry(root,textvariable=LoanValue,width=10,bd=2,font=20)
IntrestEntry=Entry(root,textvariable=IntrestValue,width=10,bd=2,font=20)
MonthsEntry=Entry(root,textvariable=MonthsValue,width=15,bd=2,font=20)
#gender label
gender_combobox=Combobox(root,values=['Male','Female','Others'],font='arial 15',state='r',width=14)
gender_combobox.place(x=455,y=250)
#collateral label
collateral_combobox=Combobox(root,values=['Gold','Vehicle','Land','House'],font='arial 15',state='r',width=14)
collateral_combobox.place(x=200,y=400)


nameEntry.place(x=200,y=150)
contactEntry.place(x=200,y=200)
ageEntry.place(x=200,y=250)
MonthlyEntry.place(x=200,y=350)
MembersEntry.place(x=525,y=350)
AdressEntry.place(x=200,y=300)
LoanEntry.place(x=210,y=450)
IntrestEntry.place(x=450,y=450)
MonthsEntry.place(x=200,y=500)


Button(root,text="Submit",bg="#FA8072",fg="white",width=15,height=2,command=payment).place(x=200,y=600)
Button(root,text="clear",bg="#FA8072",fg="white",width=15,height=2,command=clear).place(x=350,y=600)
Button(root,text="Exit",bg="#FA8072",fg="white",width=15,height=2,command=lambda:root.destroy()).place(x=500,y=600)

payment_label = Label(root, text="", bg="#00B2EE",font='arial 15')
payment_label.pack(pady=45)
payment_label1 = Label(root, text="", bg="#00B2EE",font='arial 15')
payment_label1.pack(pady=1)
root.mainloop()


# # Pseudo code
# -Loan EMI Calculation system
# -Loan is calculated based on the credit score
# -The details of the customer is collected 
# -The loan amount required is entered 
# -Credit score is above 750 loan is approved with intrest rate of 12%
# -Credit score is in  between 650-750 intrest rate will be 14%
# -Credit score below 550 we dont provide a loan to the cutomer

# In[ ]:




