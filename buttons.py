from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def click_submit(wait):
    submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="btnAdd"]'))
        )
    submit_button.click()
    print("Submit button clicked!")


def click_save(wait):
    submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))
        )
    submit_button.click()
    print("save button clicked!")


def click_confirm(wait):
    submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[6]/div/div[4]/div[2]/button'))
        )
    submit_button.click()
    print("confirm button clicked!")


def click_okay(wait):
    submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[6]/div/div[4]/div/button'))
        )
    submit_button.click()
    print("okay button clicked!")
