# Tee Ninja

## Overview
**Tee Ninja** is a Python application designed to automate the process of booking a tee time at Bethpage State Park Golf Course on Long Island (in the New York City metropolitan area). It leverages Selenium in Python for web automation and Tkinter for a user-friendly GUI. 

## Features
- Automated login and course selection
- Supports multiple courses at Bethpage
- Real-time clock display
- Simple and intuitive graphical interface

## Prerequisites
Before running Tee Ninja, ensure you have the following installed:
- Python 3.x
- Selenium
- Tkinter
- dotenv
- pytz

## Installation
1. **Install Python packages:**
    ```bash
    pip install selenium python-dotenv pytz
    ```
2. **Download Chromedriver:**
    - Download Chromedriver from [here](https://developer.chrome.com/docs/chromedriver/) and place it in a suitable directory. Update the `executable_path` in the script accordingly.
    - Make sure your Google Chrome browser is up to date and that you download the corresponding version of ChromeDriver. This means that you should check and make sure the version numbers match between your Google Chrome and ChromeDriver.

3. **Set up environment variables:**
    - Create a `.env` file in the same directory as the script and add your email and password for the booking site:
    ```plaintext
    EMAIL=your_email@example.com
    PASSWORD=your_password
    ```

## Usage
1. **Run the script:**
    ```bash
    python main.pyw
    ```
2. **Using the GUI:**
    - Select the desired course from the list.
    - Click "Select Course" to start the automation process.

## Code Explanation
- **Dependencies:**
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.keys import Keys
    import time
    from datetime import datetime
    from tkinter import *
    from dotenv import load_dotenv
    import os
    import pytz
    ```

- **Automation Function (`auto`):**
    - This function logs in to the booking site, selects the course and date, and attempts to book a tee time at 18:59:59.
    
- **GUI Setup:**
    - `Tkinter` is used to create the GUI, including course selection radio buttons and a real-time clock.

## Notes
- Adjust the `executable_path` in `Service` to point to the location of your `chromedriver.exe`.
- The booking time is set to 18:59:59. Modify this in the `while` loop if needed.
- The script assumes the booking time is in the Eastern Time Zone. Adjust the `pytz.timezone` parameter if necessary.
- This code is designed to work in Python 3.6 and above. Make sure that you have the correct version of Python installed.

## License
This project is not licensed. Please reach out to me if you would like to utilize this work for commericial use.

---

Please be safe when using and developing bots to automate tasks!
