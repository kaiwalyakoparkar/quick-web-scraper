# Import Dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

PATH = "./chromedriver"
options = Options() 

PROXY = "proxy.soax.com:10000" 
options = webdriver.ChromeOptions()
options.add_argument('proxy.soax.com'.format(PROXY))  
driver = webdriver.Chrome(service=Service(PATH), options=options)

driver.get("https://twitter.com/login")

subject = "Kaiwalya Koparkar"


# Setup the log in
sleep(5)
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys('bot65463')
next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()

sleep(5)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys('scraperBot')
log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
sleep(5)
search_box = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(5)
people = driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
people.click()

sleep(5)
profile = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/a/div/div[1]/span/span")
profile.click()

UserTags = []
TimeStamps = []
Tweets = []
Replys = []
reTweets = []
Likes = []

articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

while True:
    for article in articles:
        UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Names']").text
        UserTags.append(UserTag)
        
        TimeStamp = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        
        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)
        
        Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        Replys.append(Reply)
        
        reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)
        
        Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        Likes.append(Like)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 5:
        break

print("Tweet: ",Tweets[0], "\nReplys: ", Replys[0], "\nRetweets: ", reTweets[0], "\nLikes: ", Likes[0])
