import os
import pandas as pd


class ResultsManager:
    def __init__(self, filename="results.xlsx") -> None:
        self.folder = "data"
        self.filename = os.path.join(self.folder, filename)
        self.ensure_folder_exists()

    def ensure_folder_exists(self):
        # Check if the folder exists
        if not os.path.exists(self.folder):
            print(f"Folder '{self.folder}' not found. Creating a new one.")
            os.makedirs(self.folder)

    def ensure_file_exists(self):
        # Check if the file exists
        if not os.path.exists(self.filename):
            print(
                f"File '{self.filename}' not found. Creating a new file with an empty table.")
            # If the file doesn't exist, create a new DataFrame with columns but no rows
            df = pd.DataFrame(columns=[
                "Target Name", "Type Name", "Number of Followed", "Number of Followed-Today", "Success Rate"
            ])
            df.to_excel(self.filename, index=False)

    def update(self, target_name, type_name=None, number_of_followed_today=None, success_rate=None):
        try:
            # Ensure the file exists
            self.ensure_file_exists()

            # Load the existing Excel file
            df = pd.read_excel(self.filename)

            # Check if the target_name exists
            if target_name in df['Target Name'].values:
                # Find the row with the matching Target Name
                row_index = df.index[df['Target Name'] == target_name].tolist()
                row_index = row_index[0]

                # If the row exists and Number of Followed-Today is provided
                if number_of_followed_today is not None:
                    # Get current values
                    current_followed_today = df.at[row_index, 'Number of Followed-Today'] if not pd.isna(
                        df.at[row_index, 'Number of Followed-Today']) else 0
                    current_followed = df.at[row_index, 'Number of Followed'] if not pd.isna(
                        df.at[row_index, 'Number of Followed']) else 0

                    # Update values
                    df.at[row_index,
                          'Number of Followed-Today'] = number_of_followed_today
                    df.at[row_index, 'Number of Followed'] = current_followed + \
                        number_of_followed_today

                if success_rate is not None:
                    df.at[row_index, 'Success Rate'] = success_rate

                if type_name is not None:
                    df.at[row_index, 'Type Name'] = type_name

                print(f"Updated '{target_name}' successfully.")
            else:
                # If the target_name does not exist, add a new row
                new_row = {
                    "Target Name": target_name,
                    "Type Name": type_name if type_name is not None else "",
                    "Number of Followed": number_of_followed_today if number_of_followed_today is not None else 0,
                    "Number of Followed-Today": number_of_followed_today if number_of_followed_today is not None else 0,
                    "Success Rate": success_rate if success_rate is not None else 0.0  # Default value
                }
                new_row_df = pd.DataFrame([new_row])
                df = pd.concat([df, new_row_df], ignore_index=True)
                print(f"Added new entry for '{target_name}' successfully.")

            # Calculate totals
            if not df.empty:
                # Remove existing Total row if it exists
                df = df[df['Target Name'] != 'Total']

                # Calculate totals from the remaining rows
                total_number_followed = df['Number of Followed'].sum()
                total_number_followed_today = df['Number of Followed-Today'].sum()

                # Add the 'Total' row
                total_row = pd.DataFrame([{
                    "Target Name": "Total",
                    "Type Name": "",
                    "Number of Followed": total_number_followed,
                    "Number of Followed-Today": total_number_followed_today,
                    "Success Rate": ""
                }])
                df = pd.concat([df, total_row], ignore_index=True)

            # Save the updated DataFrame back to the Excel file
            df.to_excel(self.filename, index=False)

        except Exception as e:
            print(f"An error occurred: {e}")


# Example usage
filename = "results.xlsx"

# Create an instance of ResultsManager
manager = ResultsManager(filename)

# Update or add a new entry
manager.update("NewTarget13", type_name="Hashtag",
               number_of_followed_today=30, success_rate=80.0)
