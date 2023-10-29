import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# insert names for each - provided na ng system dapat, mamimili nalang yung patient
doctors = {
    "Dra. Dalusung": ["9:00 AM - 10:00 AM", "2:00 PM - 3:00 PM"],
    "Dra. Festejo": ["10:00 AM - 11:00 AM", "3:00 PM - 4:00 PM"],
    "Dra. Isip": ["7:00 AM - 8:00 AM", "5:00 - 6:00 PM"],
    "Dr. Sutare": ["11:00 AM - 12:00 PM", "7:00 - 8:00 PM"],
}

# dictionary to store appointments
appointments = {}

# dummy patient login credentials - bale, dito nalang sisingit yung code ni chloie for login/ signup
patients = {
    "patient1": "password1",
    "patient2": "password2",
}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in patients and patients[username] == password:
        open_appointment_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_appointment_window():
    login_window.destroy()

    appointment_window = tk.Tk()
    appointment_window.title("Appointment Scheduling")

    def schedule_appointment():
        patient_name = name_entry.get()
        age = age_entry.get()
        contact_number = contact_entry.get()
        sex = sex_var.get()
        selected_doctor = doctor_var.get()
        selected_slot = slot_var.get()
        appointment_datetime = date_time_entry.get()

        appointment_info = {
            "Name": patient_name,
            "Age": age,
            "Contact Number": contact_number,
            "Sex": sex,
            "Doctor": selected_doctor,
            "Slot": selected_slot,
            "Appointment Date and Time": appointment_datetime,
        }

        if patient_name and age and contact_number and appointment_datetime:
            appointments[patient_name] = appointment_info
            messagebox.showinfo("Appointment Scheduled", "Appointment scheduled successfully!")
        else:
            messagebox.showerror("Invalid Information", "Please fill in all required fields.")

    name_label = tk.Label(appointment_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(appointment_window)
    name_entry.pack()

    age_label = tk.Label(appointment_window, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(appointment_window)
    age_entry.pack()

    contact_label = tk.Label(appointment_window, text="Contact Number:")
    contact_label.pack()
    contact_entry = tk.Entry(appointment_window)
    contact_entry.pack()

    sex_label = tk.Label(appointment_window, text="Sex:")
    sex_label.pack()
    sex_var = tk.StringVar()
    sex_var.set("Male")
    sex_radio_male = tk.Radiobutton(appointment_window, text="Male", variable=sex_var, value="Male")
    sex_radio_female = tk.Radiobutton(appointment_window, text="Female", variable=sex_var, value="Female")
    sex_radio_male.pack()
    sex_radio_female.pack()

    doctor_label = tk.Label(appointment_window, text="Select Doctor:")
    doctor_label.pack()
    doctor_var = tk.StringVar()
    doctor_var.set("Dr. Smith")  # Default doctor
    doctor_option_menu = tk.OptionMenu(appointment_window, doctor_var, *doctors.keys())
    doctor_option_menu.pack()

    slot_label = tk.Label(appointment_window, text="Select Slot:")
    slot_label.pack()
    slot_var = tk.StringVar()
    slot_var.set(doctors[doctor_var.get()][0])  # default slot based on selected doctor
    slot_option_menu = tk.OptionMenu(appointment_window, slot_var, *doctors[doctor_var.get()])
    slot_option_menu.pack()

    date_time_label = tk.Label(appointment_window, text="Appointment Date and Time (e.g., 2023-01-01 10:00 AM):")
    date_time_label.pack()
    date_time_entry = tk.Entry(appointment_window)
    date_time_entry.pack()

    schedule_button = tk.Button(appointment_window, text="Schedule Appointment", command=schedule_appointment)
    schedule_button.pack()

    appointment_window.mainloop()

# create the main login window - e. g. patient1, password1 
login_window = tk.Tk()
login_window.title("Patient Login")

# load the image
image = Image.open("d:\Downloads\370249925_1675504379607684_9102815953664286789_n.jpg")
photo = ImageTk.PhotoImage(image)

# create a label to display the image
image_label = tk.Label(login_window, image=photo)
image_label.pack()

username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

login_window.mainloop()