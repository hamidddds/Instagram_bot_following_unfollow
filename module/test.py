import os
import pandas as pd
from datetime import datetime


class UsersDetailManager:
    def __init__(self):
        current_directory = os.path.dirname(__file__)
        self.user_details = os.path.join(
            current_directory, '..', 'data', 'Users_detail.xlsx')
        self.check_and_create_file()

    def check_and_create_file(self):
        if not os.path.exists(self.user_details):
            # Create a new DataFrame with the required columns
            df = pd.DataFrame(columns=['User name', 'page', 'date'])
            df.to_excel(self.user_details, index=False)
            print(f"File created: {self.user_details}")
        else:
            print(f"File already exists: {self.user_details}")

    def add_new_entry(self, user_name, page, date):
        # Ensure the date is a datetime object
        if isinstance(date, datetime):
            date = date.strftime('%Y-%m-%d')

        # Load the existing Excel file
        df = pd.read_excel(self.user_details)

        # Ensure the page column is treated as a string
        df['page'] = df['page'].astype(str)

        # Create the new row as a DataFrame
        new_row = pd.DataFrame(
            {'User name': [user_name], 'page': [str(page)], 'date': [date]})

        # Check if the existing DataFrame is empty
        if df.empty:
            df = new_row
        else:
            # Concatenate the new row to the existing DataFrame
            df = pd.concat([df, new_row], ignore_index=True)

        # Save the updated DataFrame back to the Excel file
        df.to_excel(self.user_details, index=False)
        print(f"New entry added: {new_row}")


if __name__ == "__main__":
    manager = UsersDetailManager()
    current_date = datetime.now()
    # Example of adding a new entry
    manager.add_new_entry('John Doe', "Hamid",     current_date
                          )
