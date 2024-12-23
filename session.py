from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def login(wait):
    user_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="login"]/div[2]/div[1]/input'))
        )
    user_input.send_keys('TAX2131400-01')
    password_input = wait.until(
            EC.presence_of_element_located((By.XPATH, ' //*[@id="password"]'))
        )
    password_input.send_keys('Boun@xt01')
    submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))
        )
    submit_button.click()
    print("Submit button clicked!")


def authenticate(driver, wait):
    if "login" in driver.current_url:
        print("Logging in for the first time...")
        login(wait)
    else:
        print("Already logged in!")


def get_driver_with_session():
    # Define a custom directory for the browser session to persist
    session_dir = "./browser_session"

    # Ensure the session directory exists
    os.makedirs(session_dir, exist_ok=True)

    # Set up Chrome options with a persistent session
    chrome_options = Options()
    chrome_options.add_argument(
        f"--user-data-dir={os.path.abspath(session_dir)}")

    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)
    return driver
