import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def fill_owner_name(wait, row):
    owner_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="owner"]'))
        )
    owner_input_value = row.get("owner_check", "?")
    if pd.isna(owner_input_value):
        owner_input_value = "?"
    owner_input.send_keys(owner_input_value)


def fill_issue_date(wait, row):
    issuedate_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="issuedate"]'))
        )
    issuedate_value = row.get("valid_from", "")
    formatted_date = issuedate_value.strftime('%d/%m/%Y')
    issuedate_input.send_keys(formatted_date)


def fill_parcel_no(wait, row):
    parcelno_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="parcelno"]'))
        )
    parcelno_value = row.get("parcelno", "")
    parcelno_input.send_keys(parcelno_value)


def fill_map_no(wait, row):
    mapno_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="mapno"]'))
        )
    mapno_value = row.get("cadastremapno", "")
    mapno_input.send_keys(mapno_value)


def fill_area(wait, row):
    area_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="total_area"]'))
        )
    area_value = row.get("area", "")
    area_input.send_keys(area_value)


def fill_latitude(wait, row):
    latitude_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="lat"]'))
        )
    latitude_value = row.get("y", "")
    latitude_input.send_keys(latitude_value)


def fill_longtitude(wait, row):
    longtitude_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="lng"]'))
        )
    longtitude_value = row.get("y", "")
    longtitude_input.send_keys(longtitude_value)
    

def fill_subarea(wait, row):
    input_field = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="subarea"]'))
        )
    value = row.get("area", "")
    input_field.send_keys(value)
