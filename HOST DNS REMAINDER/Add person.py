import json
from datetime import datetime, timedelta

today = datetime.today().date()
name = input("Name of customer: ")
email = input("email: ")
phone = input("phone: ")
website = input("website: ")

new = {"name": name,
     "email": email,
     "phone": phone,
     "website": website,
     "date": str(today)
     }

def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["customer"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

    # python object to be appended




write_json(new)