#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import time


# Soax Residential proxy connection
# PROXY = "proxy.soax.com:10000" 

#specify the path to chromedriver.exe (download and save on your computer)
PATH = "./chromedriver"
# options = webdriver.ChromeOptions()
# options.add_argument('proxy.soax.com'.format(PROXY))

# chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options = Options()
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(service=Service(PATH), options=options)


#opening facebook's login page
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("")
password.clear()
password.send_keys("")

#logging in to the facebook
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)
images = [] 

#itterate over both uploaded and tagged images respectively
for i in ["photos_all", "photos_of"]:
    #Scraping Mark Zuckerburg profile for all photos
    driver.get("https://www.facebook.com/zuck/" + i + "/")
    time.sleep(5)
    
    #scrolling down the screen
    for j in range(0,1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

    #targeting all the link elements on the page
    anchors = driver.find_elements(By.TAG_NAME, 'a')
    anchors = [a.get_attribute('href') for a in anchors]
    #filtering out image links only
    anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
    
    print('Found ' + str(len(anchors)) + ' links to images')
    
    for a in anchors:
        # print(a)
        # driver.get(a) #Navigating to each image being iterated
        time.sleep(5)
        img = driver.find_elements(By.TAG_NAME, "img")
        images.append(img[1].get_attribute("src")) #Can change in future to img[?]

print('Scraped '+ str(len(images)) + ' images!')
# print(images)
driver.get(images[0])
