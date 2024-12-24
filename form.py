import time

from select_fields import (
    select_province,
    select_district,
    select_village,
    select_land_village,
    select_address_province,
    select_address_district,
    select_address_village,
    select_zone,
    select_road_type,
    select_land_type,
    select_land_subtype,
    select_land_kind,
    select_land_zone
)
from input_fields import (
    fill_map_no,
    fill_parcel_no,
    fill_issue_date,
    fill_owner_name,
    fill_area,
    fill_latitude,
    fill_longtitude,
    fill_subarea
)
from buttons import click_submit, click_save, click_confirm, click_okay


def fill_form(driver, wait, row):
    """
    Fill out the form on the website using data from the given row.

    Parameters:
        driver: Selenium WebDriver instance.
        wait: Selenium WebDriverWait instance.
        row: Dictionary containing the row data.
    """
    try:
        select_province(driver, wait)
        print("Selecting province...")
        select_district(driver, wait)
        print("Selecting district...")
        time.sleep(1)
        select_village(driver, wait, row)
        print("selecting village...")
        fill_map_no(wait, row)
        print("Filling map no...")
        fill_parcel_no(wait, row)
        print("Filling parcel no...")
        fill_issue_date(wait, row)
        print("Filling issue date...")
        select_land_village(driver, wait, row)
        print("Selecting land village...")
        fill_owner_name(wait, row)
        print("Filling owner name...")
        time.sleep(1)
        select_address_province(driver, wait)
        print("Selecting address province...")
        select_address_district(driver, wait)
        print("Selecting address district...")
        select_address_village(driver, wait, row)
        print("Selecting address village...")
        fill_area(wait, row)
        print("Filling area...")
        fill_latitude(wait, row)
        print("Filling latitude...")
        fill_longtitude(wait, row)
        print("Filling longtitude...")
        select_zone(driver, wait, row)
        print("Selecting zone...")
        select_road_type(driver, wait, row)
        print("Selecting road type...")
        time.sleep(1)
        select_land_type(driver, wait, row)
        print("Selecting land type...")
        select_land_subtype(driver, wait, row)
        print("Selecting land subtype...")
        select_land_kind(driver, wait)
        print("Selecting land kind...")
        select_land_zone(driver, wait, row)
        print("Selecting land zone...")
        fill_subarea(wait, row)
        print("Filling subarea...")
        # click_submit(wait)
        # click_save(wait)
        # click_confirm(wait)
        time.sleep(3)
        # click_okay(wait)
        # Simulate saving or submitting the form here if needed
        time.sleep(100)  # Pause to simulate user interaction
    except Exception as e:
        print(f"An error occurred while filling the form: {e}")
