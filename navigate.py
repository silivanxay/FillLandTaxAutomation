from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def go_to_create_form(driver, wait):
    parcel_create_menu = wait.until((
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[2]/ul/li[1]/a'))
        ))
    driver.execute_script("window.scrollTo(0, 0);")
    parcel_create_menu.click()


def go_to_mainmenu(wait):
    parcel_menu = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[2]/a/span[1]'))
        )
    
    parcel_menu.click()
