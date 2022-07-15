# error in gmail. did not fix.

import smtplib

my_email = "tempudemy111@gmail.com"
password = "python888"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs="tempudemy111@yahoo.com",
                    msg="Subject:Test test\n\nThis is a test email from python."
                    )
connection.close()

