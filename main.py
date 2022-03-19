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
        print(type(all_quotes))
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Sunday Motivation\n\n{quote}")



