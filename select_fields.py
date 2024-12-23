from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from lib import (
    find_zone_by_village,
    get_road_type_value,
    get_land_type,
    get_land_subtype,
    get_land_zone,
)


def select_land_village(driver, wait, row):
    land_village_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="village_chosen"]'))
        )
    land_village_dropdown.click()
    land_village_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="village_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          land_village_select)
    village_name = row.get("village", "")
    select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{village_name}"]'))
        )
    select.click()


def select_village(driver, wait, row):
    driver.execute_script("window.scrollBy(0, -200);")
    village_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="searchvill_chosen"]'))
        )
    village_dropdown.click()
    village_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="searchvill_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          village_select)
    village_name = row.get("village", "")
    select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{village_name}"]'))
        )
    select.click()


def select_address_village(driver, wait, row):
    driver.execute_script("window.scrollBy(0, -200);")
    village_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_village_chosen"]'))
        )
    village_dropdown.click()
    village_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_village_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          village_select)
    village_name = row.get("village", "")
    select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{village_name}"]'))
        )
    select.click()


def select_district(driver, wait):
    district_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="district_chosen"]'))
        )
    district_dropdown.click()
    district_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="district_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          district_select)
    district_name = "ໄຊພູທອງ"
    select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{district_name}"]'))
        )
    select.click()


def select_address_district(driver, wait):
    district_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_district_chosen"]'))
        )
    district_dropdown.click()
    district_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_district_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          district_select)
    district_name = "ໄຊພູທອງ"
    select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{district_name}"]'))
        )
    select.click()


def select_province(driver, wait):
    province_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="province_chosen"]'))
        )
    province_dropdown.click()
    province_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="province_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          province_select)
    province_name = "ສະຫວັນນະເຂດ"
    select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{province_name}"]'))
        )
    select.click()


def select_address_province(driver, wait):
    province_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_province_chosen"]'))
        )
    province_dropdown.click()
    province_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_province_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          province_select)
    province_name = "ສະຫວັນນະເຂດ"
    select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{province_name}"]'))
        )
    select.click()


def select_zone(driver, wait, row):
    # Wait for the zone dropdown to be located
    zone_dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="zonecode_chosen"]'))
    )
    # Scroll the dropdown into view to ensure it's visible
    driver.execute_script("arguments[0].scrollIntoView(true);", zone_dropdown)
    driver.execute_script("window.scrollBy(0, -200);")

    # Click the dropdown to open it
    zone_dropdown.click()

    # Wait for the village options to be visible
    village_select = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="zonecode_chosen"]/div/ul'))
    )

    # Scroll the village options into view
    driver.execute_script("arguments[0].scrollIntoView(true);", village_select)
    # Adjust the scroll again to ensure it's not under the navbar

    village_name = row.get("village", "")
    zone = find_zone_by_village(village_name)
    print("zone:", zone)

    # Construct the XPath for the zone option
    select_xpath = f'//li[@class="active-result" and text()="{zone}"]'

    # Wait for the zone option to be clickable
    select = wait.until(EC.element_to_be_clickable((By.XPATH, select_xpath)))

    # Ensure element is in view and not blocked by other elements
    driver.execute_script("arguments[0].scrollIntoView(true);", select)
    driver.execute_script("window.scrollBy(0, -200);")

    # Hover over the element to ensure it's focused
    ActionChains(driver).move_to_element(select).perform()
    select.click()


def select_road_type(driver, wait, row):
    road_type_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="roadtype_chosen"]'))
        )
    road_type_dropdown.click()
    road_type_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="roadtype_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          road_type_select)
    road_name = row.get("road", "")
    road_type = get_road_type_value(road_name)
    select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{road_type}"]'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);", select)
    driver.execute_script("window.scrollBy(0, -200);")
    select.click()


def select_land_type(driver, wait, row):
    # Ensure the dropdown is in view by scrolling the page if necessary
    dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="cat_chosen"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    driver.execute_script("window.scrollBy(0, -200);")

    # Click the dropdown to open the list
    dropdown.click()

    # Extract the land type from the row data
    name = row.get("landusetype", "")
    index = get_land_type(name)

    # Adjust the XPath to select the option by index
    select_option_xpath = f'//*[@id="cat_chosen"]/div/ul/li[{index}]'

    # Wait for the option to be clickable
    select_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, select_option_xpath))
    )

    # Scroll the selected option into view to avoid any overlap with the header
    driver.execute_script("arguments[0].scrollIntoView(true);", select_option)
    driver.execute_script("window.scrollBy(0, -200);")
    select_option.click()


def select_land_subtype(driver, wait, row):
    dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="subcat_chosen"]'))
        )
    dropdown.click()
    select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="subcat_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          select)
    name = row.get("landusetype", "")
    index = get_land_subtype(name)
    select_option_xpath = f'//*[@id="subcat_chosen"]/div/ul/li[{index}]'

    # Wait for the option to be clickable
    select_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, select_option_xpath))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", select_option)
    driver.execute_script("window.scrollBy(0, -200);")
    select_option.click()


def select_land_kind(driver, wait):
    dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="kind_chosen"]'))
        )
    dropdown.click()
    select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="kind_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          select)
    index = 1
    select_option_xpath = f'//*[@id="kind_chosen"]/div/ul/li[{index}]'

    # Wait for the option to be clickable
    select_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, select_option_xpath))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", select_option)
    driver.execute_script("window.scrollBy(0, -200);")
    select_option.click()


def select_land_zone(driver, wait, row):
    dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zone_chosen"]'))
        )
    dropdown.click()
    select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zone_chosen"]/div/ul'))
        )
    driver.execute_script("arguments[0].scrollIntoView(true);",
                          select)
    name = row.get("landusetype", "")
    index = get_land_zone(name)
    select_option_xpath = f'//*[@id="zone_chosen"]/div/ul/li[{index}]'

    # Wait for the option to be clickable
    select_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, select_option_xpath))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", select_option)
    driver.execute_script("window.scrollBy(0, -200);")
    select_option.click()
