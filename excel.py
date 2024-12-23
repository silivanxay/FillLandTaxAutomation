import pandas as pd


def import_excel_rows(file_path, sheet_name, first_row, last_row):
    """
    Import specified rows from an Excel file and convert
    them into objects (dictionaries).

    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to read from.
        first_row (int): First row to include (1-based index).
        last_row (int): Last row to include (1-based index).

    Returns:
        list: List of row data as dictionaries.
    """
    try:
        # Always read the column headers from the first row of the sheet
        header_row = 0
        skip_rows = list(range(header_row + 1,
                               first_row - 1)) if first_row > 2 else None
        nrows = last_row - first_row + 1

        # Read the data from the file
        data = pd.read_excel(
            file_path,
            engine='openpyxl',
            sheet_name=sheet_name,
            header=header_row,  # Read column headers from the first row
            skiprows=skip_rows,
            nrows=nrows  # Limit to the required number of rows
        )

        # Convert each row to a dictionary
        objects = [row.to_dict() for _, row in data.iterrows()]

        print("\nSelected rows converted to objects:")
        return objects
    except Exception as e:
        print(f"An error occurred: {e}")
        return None