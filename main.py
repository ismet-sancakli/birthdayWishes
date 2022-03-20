import datetime as dt
import random
import pandas
import smtplib

MY_EMAIL = "isancakli5@gmail.com"
MY_PASSWORD ="i.Snckl#1473695"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")


"""
import smtplib
import datetime as dt
import random

MY_EMAIL = "youremailaddress@gmail.com"
MY_PASSWORD ="yourpassword"
now = dt.datetime.now()
weekday = now.weekday() # Each week has 7 days but weekday module is starting from 0 to 6.
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # starttls for the email security.
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Sunday Motivation\n\n{quote}")

"""

