from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import random

#Inserting our user details
chrome_webdriver_path = "/Your complete folder path"
bing_email_address = ""
bing_password = ""

#get the browser
browser = webdriver.Chrome(chrome_webdriver_path)
#load the login screen
browser.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1563130781&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253d1B39D6E50827401881165767AF42E1D4%2526wlexpsignin%253d1%26sig%3d0651AC2328BB60D32AD5A1BA293361CF&lc=1033&id=264960&CSRFToken=b34a6229-88ed-47e6-83f3-dd676bd5591b&aadredir=1")
#wait for the page to load a little longer due to cold start
time.sleep(4)

#generate random strings and load into the browser
def loadSearches():
    for x in range(30):

        root = "https://bing.com/search?q="
        letters = string.ascii_letters

        searchString = "".join(random.choice(letters) for x in range(10))

        browser.get(root+searchString)
        time.sleep(1) #wait for the page to load

#sign into your bing account by pressing on the textfields and buttons on the screen
def signIntoBing():
    email = browser.find_element_by_id("i0116")
    email.send_keys(bing_email_address)

    submit_button = browser.find_element_by_id("idSIButton9")
    submit_button.click()
    time.sleep(2)

    password = browser.find_element_by_id("i0118")
    password.send_keys(bing_password)

    submit_button = browser.find_element_by_id("idSIButton9")
    submit_button.click()
    time.sleep(2)

    loadSearches()


signIntoBing()

#close the browser once finished
browser.close()
