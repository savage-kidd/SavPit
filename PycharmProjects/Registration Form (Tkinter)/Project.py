from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

# Heading
Label(root,text="Registration Form", font="Arial 15 bold").grid(row=0, column=3)

# Field Name
name=Label(root, text="Name")
phone=Label(root, text="Phone Number")
gender=Label(root, text="Gender")
emergencycontact=Label(root, text="Emergency Contact")
paymentmethod=Label(root, text="Payment Method")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergencycontact.grid(row=4, column=2)
paymentmethod.grid(row=5, column=2)

# Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencycontact = StringVar
paymentmethod = StringVar
checkvalue = IntVar

# Creating entry field
nameentry = Entry(root,textvariable= namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
genderentry = Entry(root,textvariable=gendervalue)
emergencycontactentry = Entry(root,textvariable=emergencycontact)
paymentmethodentry = Entry(root,textvariable=paymentmethod)

# Packing entry fields
nameentry.grid(row= 1, column=3)
phoneentry.grid(row= 2, column=3)
genderentry.grid(row= 3, column=3)
emergencycontactentry.grid(row= 4, column=3)
paymentmethodentry.grid(row= 5, column=3)

# Creating Checkbox
chechbtn = Checkbutton(text="remember me" ,variable=checkvalue)
chechbtn.grid(row=6, column=3)

#Submit button
Button(text="Submit",command=getvals).grid(row= 7, column =3)

root.mainloop()