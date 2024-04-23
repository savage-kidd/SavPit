import kivy
import pyodbc
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student LastName'))
        self.s_lastname = TextInput()
        self.add_widget(self.s_lastname)

        self.add_widget(Label(text='Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = 'Submit')
        self.press.bind(on_press = self.Submit)
        self.add_widget(self.press)

    def Submit(self, instance):
        name = self.s_name.text
        lastname = self.s_lastname.text
        marks = self.s_marks.text
        gender = self.s_gender.text

        # print("Name of the Student is "+self.s_name.text)
        # print("Last Name of the Student is "+self.s_lastname.text)
        # print("Marks Obtained by Student "+self.s_marks.text)
        # print("Gender of the Student is "+self.s_gender.text)
        # print("")

        # Connect to SQl Server Database
        conn = pyodbc.connect(
            r'Driver={SQL SERVER};'
            r'SERVER=HOCPT-IT-01\SQLEXPRESS;'
            r'Database=StudentData;'
            r'Trusted_Connection=Yes'  # If Using Windows Authentication
            # If Using SQL Server Authentication
            # r'UID=Username;'
            # r'PWD=Password;'
        )
        cursor = conn.cursor()

        # Create registration table if it doesn't exist
        cursor.execute('''IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.Tables WHERE TABLE_NAME = N'students') 
        CREATE TABLE students (StudentName NVARCHAR(MAX), StudentLastName NVARCHAR(MAX), Marks INT, Gender NVARCHAR(
        MAX))''')

        # Insert student data
        cursor.execute("INSERT INTO students (StudentName, StudentLastName, Marks, Gender) VALUES(?, ?, ?, ?)", (
        name, lastname, marks, gender))
        conn.commit()
        conn.close()

        print("Data Saved to StudentDatabase")
class parentApp(App):
    def build(self):
        return childApp()


if __name__ == "__main__":
    parentApp().run()
