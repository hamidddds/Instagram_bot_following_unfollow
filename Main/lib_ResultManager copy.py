import os
import pandas as pd


class ResultsManager:
    def __init__(self, folder_name='data', file_name='table.xlsx'):
        self.folder_path = folder_name
        self.file_path = os.path.join(self.folder_path, file_name)
        self.headers = ["Target Name", "Type Name", "Total Number of Followed",
                        "Number of Followed-Today", "Success Rate"]
        self._check_and_create_file()
        self.initiate()

    def initiate(self):
        pass

    def _check_and_create_file(self):
        # Check if the folder exists, create it if not
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
            print(f"Folder '{self.folder_path}' created.")

        # Check if the Excel file exists
        if not os.path.isfile(self.file_path):
            # Create an empty DataFrame with the specified headers
            df = pd.DataFrame(columns=self.headers)

            # Save the DataFrame to an Excel file
            df.to_excel(self.file_path, index=False, engine='openpyxl')
            print(f"Table created and saved to {self.file_path}")
        else:
            print(f"File '{self.file_path}' already exists.")
            df = pd.read_excel(self.file_path, engine='openpyxl')
        df.loc[:, 'Number of Followed-Today'] = 0
        df.to_excel(self.file_path, index=False, engine='openpyxl')

    def update(self, target_name, type_name, number_of_followed):
        # Load the existing table
        df = pd.read_excel(self.file_path, engine='openpyxl')

        # Check if the target already exists
        if target_name in df.iloc[:, 0].values:
            # Update existing row
            idx = df.index[df.iloc[:, 0] == target_name].tolist()[0]
            df.at[idx, 'Total Number of Followed'] += number_of_followed
            df.at[idx, 'Number of Followed-Today'] += number_of_followed
        else:
            # Add a new row
            new_row = pd.DataFrame([{
                "Target Name": target_name,
                "Type Name": type_name,
                "Total Number of Followed": number_of_followed,
                "Number of Followed-Today": number_of_followed,
                "Success Rate": 0  # Assuming Success Rate is 0 initially
            }])
            df = pd.concat([df, new_row], ignore_index=True)

        # Save the updated DataFrame back to the Excel file
        df.to_excel(self.file_path, index=False, engine='openpyxl')
        print(f"Row added/updated for '{target_name}'.")


# Example usage
# if __name__ == "__main__":
#     manager = TableManager()
#     for i in range(3):
#         print(i)
#         manager.add_row("Example Target", "Example Type", 5)
