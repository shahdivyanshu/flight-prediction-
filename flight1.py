from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import smtplib


date_1 = "2020-08-10"
date_2= "2020-08-13"

a= int(date_1[8:10])
b = int(date_2[8:10])

if a > b:
    m = a - b
    t = b

else:
    m = b - a
    t = a
print(t)

low_price = ""
url_final = 'https://paytm.com/flights'
data = {}

for i in range(t, t + m + 1):
    url = 'https://paytm.com/flights/flightSearch/VNS-Varanasi/DEL-Delhi/1/0/0/E/2020-08-' + str(i)
    print(url)

    date = "2020-08-" + str(i)

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")

    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path='C:/bin/chromedriver_win32/chromedriver',
                              options=chrome_options)

    driver.implicitly_wait(20)
    driver.get(url)

    g = driver.find_element_by_xpath("//div[@class='_2gMo']")
    price = g.text

    x = price[0]
    y = price[2:5]
    z = str(x) + str(y)
    p = int(z)
    print(p)

    prices = []
    if p <= 7000:
        data[date] = p

for i in data:
    low_price += str(i) + ": Rs." + str(data[i]) + "\n"

print(low_price)

if len(data) != 0:
    dp = 7000
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    
    #insert your email id and passsword with which you want to send email down below
    server.login('email id ', 'password')
    subject = "Flight price for VNS-DEL has fallen\
    below Rs. " + str(dp)

    body = "Hey Divyanshu! \n The price of varanasi-delhi flight  on PayTm \
    has fallen down below Rs." + str(dp) + ".\n So, \
            hurry up & check: " + url_final + "\n\n\n The prices of \
            flight below Rs.7000 for the following days are \
            :\n\n" + low_price

    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        'shahanupriya1@gmail.com',
        'divyanshushah66@gmail.com',
        msg
    )

    print("HEY,EMAIL HAS BEEN SENT SUCCESSFULLY.")

    server.quit()
