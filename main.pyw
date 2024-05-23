from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from datetime import date
from datetime import timedelta 

from tkinter import *
from tkinter import ttk

import os
from dotenv import load_dotenv

import pytz

def auto():
    selected_course = course_var.get()    
    service = Service(executable_path="D:\TeeTime\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    load_dotenv()
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    driver.get("https://foreupsoftware.com/index.php/booking/19765/2431#welcome")
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/p/button').click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div/div[1]/div/input").send_keys(EMAIL)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div/div[2]/div/input").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div/div[2]/div/input").send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/button[1]").click()

    time.sleep(2)
    select = Select(driver.find_element(By.ID, 'schedule_select'))
    select.select_by_visible_text(selected_course)

    select = Select(driver.find_element(By.ID, 'date-menu'))
    select.select_by_index(7)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    selected = False

    while (selected == False):
        current_time = datetime.now().strftime("%H:%M:%S")
        if (current_time == "18:59:59"):
            time.sleep(0.5)
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div[10]").click()
            selected = True
        else:
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[3]/button").click()
            time.sleep(0.25)

    time.sleep(300)
    driver.quit()

def update_time():
    now = datetime.now(pytz.timezone('America/New_York')).strftime('%m-%d-%Y %H:%M:%S')
    time_label.config(text=now)
    root.after(1000, update_time)

# Create the main window
root = Tk()
root.title("Tee Ninja")
root.geometry("300x400")

# Create the main frame
main_frame = Frame(root, padx=10, pady=10)
main_frame.pack(padx=10, pady=10)

# Create and place the title label
title_label = Label(main_frame, text="Tee Ninja", font=("Helvetica", 24))
title_label.grid(row=0, column=0, columnspan=2)

# Create and place the subheading label
subheading_label = Label(main_frame, text="By Robin Hwang", font=("Helvetica", 14))
subheading_label.grid(row=1, column=0, columnspan=2)

# Create and place the radio buttons
course_var = StringVar(value="Bethpage Black Course")
courses = ["Bethpage Black Course", "Bethpage Blue Course", "Bethpage Green Course", "Bethpage Red Course", "Bethpage Yellow Course"]

for idx, course in enumerate(courses):
    radio_button = Radiobutton(main_frame, text=course, variable=course_var, value=course)
    radio_button.grid(row=2+idx, column=0, columnspan=2, sticky="w")

# Create and place the button
select_button = Button(main_frame, text="Select Course", command=auto)
select_button.grid(row=7, column=0, columnspan=2, pady=10)

# Create and place the time label
time_label = Label(main_frame, text="", font=("Helvetica", 12))
time_label.grid(row=9, column=0, columnspan=2, pady=10)

# Start updating the time
update_time()

# Run the main loop
root.mainloop()