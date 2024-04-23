import kivy
import pyodbc
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import  TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        head_label = Label(text="Python User Registration App", font_size=26, bold=True,
                           height=40)
        # Adding Label
        name_label = Label(text="Name", font_size=18)
        self.name_input = TextInput(multiline=False, font_size=18)

        email_label = Label(text="Email", font_size=18)
        self.email_input = TextInput(multiline=False, font_size=18)

        password_label = Label(text="Password", font_size=18)
        self.password_input = TextInput(multiline=False, font_size=18, password=True)

        confirm_label = Label(text="Confirm Password", font_size=18)
        self.confirm_input = TextInput(multiline=False, font_size=18, password=True)

        #Button
        sumbit_button =Button(text='Register', font_size=18, on_press=self.register)

        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(sumbit_button)
        return layout

    def register(self, instance):
        # Collect information
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_input.text

        # Validation
        if name.strip() == "" or email.strip() == "" or password.strip() == "" or confirm_password.strip() == "":
            message = "Please fill in all the fields"

        elif password != confirm_password:
            message= "Passwords do not match"

        else:
            try:
                # Connect to SQl Server Database
                conn =pyodbc.connect(
                    r'Driver={SQL SERVER};'
                    r'SERVER=HOCPT-IT-01\SQLEXPRESS;'
                    r'Database=Registrations;'
                    r'Trusted_Connection=Yes' # If Using Windows Authentication
                    #If Using SQL Server Authentication
                    #r'UID=Username;'
                    #r'PWD=Password;'
                )
                cursor = conn.cursor()

                # Create registration table if it doesn't exist
                cursor.execute('''IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.Tables
                                   WHERE TABLE_NAME = N'registrations')
                                   CREATE TABLE registrations (name NVARCHAR(MAX), email NVARCHAR(MAX), password NVARCHAR(MAX))''')

                # Insert registration data
                cursor.execute( "INSERT INTO registrations (name, email, password) VALUES(?, ?, ?)", (name, email, password))
                conn.commit()
                conn.close()

                message = "Registration successful!\nName: {}\nEmail: {}".format(name, email)
            except Exception as e:
                message = "Error: {}".format(str(e))

        # Popup
        popup = Popup(title= "Registration Status", content=Label(text=message), size_hint=(None,None), size=(400, 200))
        popup.open()

if __name__=='__main__':
    RegistrationApp().run()