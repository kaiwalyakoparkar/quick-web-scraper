
#imports here
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# Soax Residential proxy connection
PROXY = "proxy.soax.com:10002" 

PATH = "./chromedriver"
options = webdriver.ChromeOptions()
options.add_argument('proxy.soax.com'.format(PROXY))
driver = webdriver.Chrome(service=Service(PATH), options=options)

#open the webpage
driver.get("http://www.instagram.com/login")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("")
password.clear()
password.send_keys("")

#target the login button and click it
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#search for the hashtag cat
keyword = "#cat"
searchbox.send_keys(keyword)

# Wait for 5 seconds
time.sleep(3)
searchbox.send_keys(Keys.ENTER)
time.sleep(3)
searchbox.send_keys(Keys.ENTER)
time.sleep(3)

#scroll down to scrape more images
driver.execute_script("window.scrollTo(0, 4000);")

#target all images on the page
time.sleep(5)
images = driver.find_elements(By.TAG_NAME,'img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]

# No of image links scraped
print('Number of scraped images: ', len(images))

# Displaying one of the scrapped links --> Can be downloaded too
print("Displaying image: ", images[4])
driver.get(images[4])