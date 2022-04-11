import json
import os
import pprint
import smtplib

from datetime import datetime, timedelta
today = datetime.today().date()
expiry_7 = datetime.today().date() + timedelta(days=359)
expiry_6 = datetime.today().date() + timedelta(days=360)
expiry_5 = datetime.today().date() + timedelta(days=361)
expiry_4 = datetime.today().date() + timedelta(days=362)
expiry_3 = datetime.today().date() + timedelta(days=363)
expiry_2 = datetime.today().date() + timedelta(days=364)
expiry_1 = datetime.today().date() + timedelta(days=365)

with open("data.json", "r") as read_json:
    data = json.load(read_json)


print(today)


USER_NAME = os.environ["Alex_dev_gmail"]
PASSWORD = os.environ["password"]

for i in data["customer"]:

    if i["date"] == str(expiry_7) or i["date"] == str(expiry_6) or i["date"] == str(expiry_5) or i["date"] == str(expiry_4) or i["date"] == str(expiry_3) or i["date"] == str(expiry_2) or i["date"] == str(expiry_1):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # layer of encryption
            connection.login(USER_NAME, PASSWORD)
            connection.sendmail(
                from_addr=USER_NAME,
                to_addrs= (i["email"],USER_NAME),
                msg=f"Subject:'Host for {i['website']} about to expire'\n\n hi {i['name']} Your last yearly host was paid on {i['date']}"
                    f" If you wish to maintain {i['website']} please make payment: \nBarclays\nMR AA GOGEV\nAccount: 205851\nSort Code: 00896071\nAdd reference your site name\nHost + domain name = 110 pounds per year\n"
                    f"\nAfter you made payment please replay to this email I will confirm the transaction and proceed with reserving your host and domain for next year! "
                    f"\nYou can also contact me by phone 07714443119"
                    f"\n\nIf you already payed for next year please ignore this email"

                )
            connection.close()
            print("sent")
            with open("keep_eye.txt", "a") as check:
                check.write(f'\n{today} \ncheck for payment: Name: {i["name"]}, Web: {i["website"]}, Phone: {i["phone"]}, Last payed: {i["date"]}    \n')
