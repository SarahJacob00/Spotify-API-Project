from selenium import webdriver
from secret_spotify import username,pw
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
chrome_path=r"C:\Users\jacob\chromedriver_win32\chromedriver.exe"
#/html/body/div[2]/div/header/div/nav/ul/li[6]/a -> xpath of the login button
#/html/body/div[1]/div[4]/div/div[1]/header/div/div[1]/a/span/svg

def access_spotify(user,pw):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver=webdriver.Chrome(executable_path=chrome_path)
    driver.get("https://www.spotify.com/") 
    sleep(2)      
    driver.find_element_by_xpath("//a[contains(text(),'Log in')]").click()
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/div/input").send_keys(user)#//input[@name=\"username\"]
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/div/input").send_keys(pw)#//input[@name=\"password\"]
    driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()
    sleep(4)
    #driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/header/div/div[1]/a").click()

    #-------------removed a page by spotify
    #driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/header/div/div[1]/a").click()
    #sleep(3)
    #driver.find_element_by_xpath("//a[contains(text(),'Launch Web Player')]").click()
    #while(True):
    #    sleep(6)
    #-------------------

#access_spotify(username,pw)
