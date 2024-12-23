from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from lib import (
    find_zone_by_village,
    get_road_type_value,
    get_land_type,
    get_land_subtype,
    get_land_zone,
    get_village,
    get_village_zone
)


def select_land_village(driver, wait, row):
    try:
        # Wait for the village dropdown to be visible and click it
        land_village_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="village_chosen"]'))
        )
        land_village_dropdown.click()

        # Wait for the village options to become visible
        land_village_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="village_chosen"]/div/ul'))
        )

        # Scroll the dropdown into view
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              land_village_select)

        village_name = get_village(row)

        # Dynamically construct the XPath to find the village option
        select_xpath = f'//li[@class="active-result"\
            and text()="{village_name}"]'

        # Wait until the specific village option is clickable
        select = wait.until(
            EC.element_to_be_clickable((By.XPATH, select_xpath))
        )

        # Scroll the selected element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", select)
        driver.execute_script("window.scrollBy(0, -200);")

        # Click the selected village option
        select.click()

        print(f"Successfully selected land village: {village_name}")
    except Exception as e:
        # Handle errors and provide feedback
        print(f"Error selecting land village '{village_name}': {e}")
        print("Please manually select the village.")

        # Optional: Wait for the user to select manually (useful for debugging)
        wait.until(
            lambda driver: "chosen-with-drop" not in land_village_dropdown.
            get_attribute("class")
        )
        print("Manual selection completed. Proceeding...")


def select_village(driver, wait, row):
    try:
        # Scroll up to ensure the dropdown is visible
        driver.execute_script("window.scrollBy(0, -200);")

        # Wait for the village dropdown to be visible
        village_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="searchvill_chosen"]'))
        )
        village_dropdown.click()

        # Wait for the village options to be visible
        village_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="searchvill_chosen"]/div/ul'))
        )

        # Ensure the options are scrolled into view
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              village_select)

        # Retrieve the village name from the row
        village_name = get_village(row)

        # Construct the XPath dynamically to find the village option
        select_xpath = f'//li[@class="active-result"\
            and text()="{village_name}"]'

        # Wait for the specific village option to be clickable
        select = wait.until(
            EC.element_to_be_clickable((By.XPATH, select_xpath))
        )

        # Ensure the element is in view and not blocked by other elements
        driver.execute_script("arguments[0].scrollIntoView(true);", select)
        driver.execute_script("window.scrollBy(0, -200);")

        # Click the village option
        select.click()

        print(f"Selected village: {village_name}")
    except Exception as e:
        print(f"Error selecting village '{village_name}': {e}")
        print("Please select the village manually.")

        wait.until(
            lambda driver: "chosen-with-drop" not in village_dropdown.
            get_attribute("class")
        )
        print("Manual selection completed. Proceeding...")


def select_address_village(driver, wait, row):
    try:
        # Scroll up to ensure the dropdown is in view
        driver.execute_script("window.scrollBy(0, -200);")

        # Wait for the village dropdown to be visible and clickable
        village_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_village_chosen"]'))
        )
        village_dropdown.click()

        # Wait for the village options to appear
        village_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_village_chosen"]/div/ul'))
        )

        # Ensure the options are in view
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              village_select)

        # Get the village name from the row data
        village_name = get_village(row)

        # Construct XPath dynamically for the village name
        select_xpath = f'//li[@class="active-result" \
            and text()="{village_name}"]'

        # Wait for the specific village option to be clickable
        select = wait.until(
            EC.element_to_be_clickable((By.XPATH, select_xpath))
        )

        # Scroll the selected village option into view and click it
        driver.execute_script("arguments[0].scrollIntoView(true);", select)
        driver.execute_script("window.scrollBy(0, -200);")
        select.click()

        print(f"Selected village: {village_name}")
    except Exception as e:
        print(f"Error selecting village '{village_name}': {e}")
        print("Please select the village manually.")
        
        wait.until(
            lambda driver: "chosen-with-drop" not in village_dropdown.
            get_attribute("class")
        )
        print("Manual selection completed. Proceeding...")


def select_district(driver, wait):
    try:
        # Wait for the district dropdown to be located and click it
        district_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="district_chosen"]')
            )
        )
        district_dropdown.click()

        # Wait for the district options list to be visible
        district_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="district_chosen"]/div/ul')
            )
        )
        # Scroll the dropdown options into view
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              district_select)
        driver.execute_script("window.scrollBy(0, -200);")

        # Define the district name to be selected
        district_name = "ໄຊພູທອງ"

        # Construct the XPath for the specific district option
        select_xpath = f'//li[@class="active-result" \
            and text()="{district_name}"]'

        # Wait for the district option to be clickable
        select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, select_xpath)
            )
        )

        # Scroll the district option into view and click it
        driver.execute_script("arguments[0].scrollIntoView(true);", select)
        driver.execute_script("window.scrollBy(0, -200);")
        select.click()

    except Exception as e:
        print(f"Error selecting district '{district_name}': {e}")
        print("Please select the district manually.")

        # Optionally wait for the user to select manually
        wait.until(
            lambda driver: "chosen-with-drop" not in district_dropdown.
            get_attribute("class")
        )
        print("Manual selection completed. Proceeding...")


def select_address_district(driver, wait):
    try:
        # Wait for the district dropdown to be located
        district_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_district_chosen"]')
            )
        )

        # Scroll the dropdown into view
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              district_dropdown)
        driver.execute_script("window.scrollBy(0, -200);")

        # Click the dropdown to open it
        district_dropdown.click()

        # Wait for the list of districts to be visible
        district_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_district_chosen"]/div/ul')
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              district_select)

        # District name to select
        district_name = "ໄຊພູທອງ"

        # Construct XPath for the target district
        select_xpath = f'//li[@class="active-result" \
            and text()="{district_name}"]'

        # Wait for the target district option to be clickable
        select = wait.until(EC.element_to_be_clickable(
            (By.XPATH, select_xpath)))

        # Scroll the option into view and click it
        driver.execute_script("arguments[0].scrollIntoView(true);", select)
        driver.execute_script("window.scrollBy(0, -200);")
        select.click()

    except Exception as e:
        print(f"Error while selecting district '{district_name}': {e}")
        print("Please select the district manually.")

        # Wait for the user to manually select and close the dropdown
        wait.until(
            lambda driver: "chosen-with-drop" not in district_dropdown.
            get_attribute("class")
        )
        print("Manual selection completed. Proceeding...")


def select_province(driver, wait):
    try:
        # Wait for the province dropdown to be located
        province_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="province_chosen"]')
            )
        )

        # Scroll the dropdown into view
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              province_dropdown)
        driver.execute_script("window.scrollBy(0, -200);")

        # Click the dropdown to open it
        province_dropdown.click()

        # Wait for the list of provinces to be visible
        province_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="province_chosen"]/div/ul')
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              province_select)

        # Province name to select
        province_name = "ສະຫວັນນະເຂດ"

        # Construct XPath for the target province
        select_xpath = f'//li[@class="active-result" \
            and text()="{province_name}"]'

        # Wait for the target province option to be clickable
        select = wait.until(EC.element_to_be_clickable(
            (By.XPATH, select_xpath)))

        # Scroll the option into view and click it
        driver.execute_script("arguments[0].scrollIntoView(true);", select)
        driver.execute_script("window.scrollBy(0, -200);")
        select.click()

    except Exception as e:
        print(f"Error while selecting province '{province_name}': {e}")
        print("Please select the province manually.")

        # Wait for the user to manually select and close the dropdown
        wait.until(
            lambda driver: "chosen-with-drop" not in province_dropdown.
            get_attribute("class")
        )
        print("Manual selection completed. Proceeding...")


def select_address_province(driver, wait):
    try:
        # Wait for the province dropdown to be located
        province_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_province_chosen"]')
            )
        )

        # Scroll the dropdown into view to ensure it's visible
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              province_dropdown)
        driver.execute_script("window.scrollBy(0, -200);")

        # Click the dropdown to open it
        province_dropdown.click()

        # Wait for the province options to be visible
        province_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="own_province_chosen"]/div/ul')
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              province_select)

        # Specify the province name to select
        province_name = "ສະຫວັນນະເຂດ"

        # Construct the XPath for the province option
        select_xpath = f'//li[@class="active-result" \
            and text()="{province_name}"]'

        # Wait for the province option to be clickable
        select = wait.until(EC.element_to_be_clickable(
            (By.XPATH, select_xpath)))

        # Click the selected province option
        select.click()

    except Exception as e:
        print(f"Error selecting province '{province_name}': {str(e)}")
        print("Please select the province manually.")

        # Wait for the user to manually close the dropdown
        wait.until(
            lambda driver: province_dropdown.get_attribute("class").
            find("chosen-with-drop") == -1
        )
        print("Manual selection completed. Proceeding...")


def select_zone(driver, wait, row):
    try:
        # Wait for the zone dropdown to be located
        zone_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zonecode_chosen"]')
            )
        )
        # Scroll the dropdown into view to ensure it's visible
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              zone_dropdown)
        driver.execute_script("window.scrollBy(0, -200);")

        # Click the dropdown to open it
        zone_dropdown.click()

        # Wait for the village options to be visible
        village_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="zonecode_chosen"]/div/ul')
            )
        )

        # Scroll the village options into view
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              village_select)

        # Get the zone based on the village name
        village_name = get_village_zone(row)
        zone = find_zone_by_village(village_name)
        print("zone:", zone)

        # Construct the XPath for the zone option
        select_xpath = f'//li[@class="active-result" and text()="{zone}"]'

        # Wait for the zone option to be clickable
        select = wait.until(
            EC.element_to_be_clickable((By.XPATH, select_xpath)))

        # Ensure element is in view and not blocked by other elements
        driver.execute_script("arguments[0].scrollIntoView(true);", select)
        driver.execute_script("window.scrollBy(0, -200);")

        # Hover over the element to ensure it's focused
        ActionChains(driver).move_to_element(select).perform()
        select.click()

    except Exception:
        print(f"Zone '{zone}' not found or not clickable. \
            Please select manually.")
        # Wait for the user to manually close the dropdown
        wait.until(
            lambda driver: zone_dropdown.get_attribute("class").
            find("chosen-with-drop") == -1
        )
        print("Manual selection completed. Proceeding...")


def select_road_type(driver, wait, row):
    try:
        # Locate and click the road type dropdown
        road_type_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="roadtype_chosen"]')
            )
        )
        road_type_dropdown.click()

        # Locate the dropdown options container
        road_type_select = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="roadtype_chosen"]/div/ul')
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              road_type_select)

        # Get the road name from the row and determine the road type
        road_name = row.get("road", "")
        road_type = get_road_type_value(road_name)

        # Construct XPath for the desired road type option
        select = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//li[@class="active-result" and text()="{road_type}"]')
            )
        )

        # Scroll to and click the desired option
        driver.execute_script("arguments[0].scrollIntoView(true);", select)
        driver.execute_script("window.scrollBy(0, -200);")
        select.click()
    except Exception:
        print(f"Road type '{road_name}' not found or not clickable.\
            Please select manually.")
        # Wait for the user to manually select an option
        wait.until(
            lambda driver: road_type_dropdown.get_attribute("class").
            find("chosen-with-drop") == -1
        )
        print("Manual selection completed. Proceeding...")


def select_land_type(driver, wait, row):
    # Ensure the dropdown is in view by scrolling the page if necessary
    dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="cat_chosen"]')
        )
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

    try:
        # Wait for the option to be clickable and click it
        select_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, select_option_xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              select_option)
        driver.execute_script("window.scrollBy(0, -200);")
        select_option.click()
    except Exception:
        print(f"Land type '{name}' not found. Please select manually.")
        # Wait for the user to manually select an option
        wait.until(
            lambda driver: dropdown.get_attribute("class").
            find("chosen-with-drop") == -1
        )
        print("Selection completed by user. Proceeding...")


def select_land_subtype(driver, wait, row):
    # Locate and click the dropdown menu
    dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="subcat_chosen"]')
        )
    )
    dropdown.click()

    # Locate the list of options
    select = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="subcat_chosen"]/div/ul')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", select)

    # Get the desired subtype name and corresponding index
    name = row.get("landusetype", "")
    index = get_land_subtype(name)
    select_option_xpath = f'//*[@id="subcat_chosen"]/div/ul/li[{index}]'

    try:
        # Try to locate and click the specified option
        select_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, select_option_xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              select_option)
        driver.execute_script("window.scrollBy(0, -200);")
        select_option.click()
    except Exception:
        print(f"Subtype '{name}' not found. Please select manually.")
        # Wait for the user to manually select an option
        wait.until(
            lambda driver: dropdown.get_attribute("class").
            find("chosen-with-drop") == -1
        )
        print("Selection completed by user. Proceeding...")


def select_land_kind(driver, wait):
    # Locate and click the dropdown menu
    dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="kind_chosen"]')
        )
    )
    dropdown.click()

    # Locate the list of options
    select = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="kind_chosen"]/div/ul')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", select)

    # Select the first option (index = 1)
    index = 1
    select_option_xpath = f'//*[@id="kind_chosen"]/div/ul/li[{index}]'

    try:
        # Try to locate and click the option
        select_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, select_option_xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              select_option)
        driver.execute_script("window.scrollBy(0, -200);")
        select_option.click()
    except Exception:
        print("Option not found. Please select manually.")
        # Wait for the user to manually select an option
        wait.until(
            lambda driver: dropdown.get_attribute("class").
            find("chosen-with-drop") == -1
        )
        print("Selection completed by user. Proceeding...")


def select_land_zone(driver, wait, row):
    dropdown = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="zone_chosen"]')
        )
    )
    dropdown.click()

    select = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="zone_chosen"]/div/ul')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", select)

    name = row.get("landusetype", "")
    index = get_land_zone(name)
    select_option_xpath = f'//*[@id="zone_chosen"]/div/ul/li[{index}]'

    try:
        # Try to find and click the desired option
        select_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, select_option_xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              select_option)
        driver.execute_script("window.scrollBy(0, -200);")
        select_option.click()
    except Exception:
        print(f"Option '{name}' not found. Please select manually.")
        # Wait for the user to manually select an option
        wait.until(
            lambda driver: dropdown.get_attribute("class").
            find("chosen-with-drop") == -1
        )
        print("Selection completed by user. Proceeding...")
