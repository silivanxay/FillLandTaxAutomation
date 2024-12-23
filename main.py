from selenium.webdriver.support.wait import WebDriverWait

from form import fill_form
from excel import import_excel_rows
from session import get_driver_with_session, authenticate
from navigate import go_to_create_form, go_to_mainmenu


def main():
    # Step 1: Import data from Excel
    folder_path = "./data/"
    file_name = input("Enter the filename (e.g., data.xlsx): ").strip()
    file_path = f"{folder_path}{file_name}"
    sheet_name = input("Enter the sheet name (e.g., bounthavy): ").strip()

    try:
        first_row = int(input(
            "Enter the first row number to read (1-based index): ").strip())
        last_row = int(input(
            "Enter the last row number to read (1-based index): ").strip())

        if first_row > last_row:
            print("Error: First row number cannot be \
                greater than the last row number.")
            return

        # Import rows from the Excel file
        rows = import_excel_rows(file_path, sheet_name, first_row, last_row)
        if not rows:
            print("No data found or an error occurred.")
            return
    except ValueError:
        print("Invalid input. Please enter numeric \
            values for the row numbers.")
        return

    # Step 2: Automate form filling
    driver = get_driver_with_session()
    driver.get("http://str.mof.gov.la/landtax/login")

    try:
        wait = WebDriverWait(driver, 10)

        # Authenticate the session
        authenticate(driver, wait)

        # Navigate to the create form page
        go_to_mainmenu(wait)

        # Iterate through each row and fill the form
        count = 0
        for row in rows:
            go_to_create_form(driver, wait)
            fill_form(driver, wait, row)
            print(f"Form filled successfully for row: {first_row+count}")
            count += 1
            # go_to_create_form(wait)
        print("All forms have been filled successfully.")
    except Exception as e:
        print(f"An error occurred during automation: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
