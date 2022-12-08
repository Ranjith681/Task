from selenium import webdriver

import warnings
warnings.simplefilter('ignore')

driver = webdriver.Chrome(r"C:\Users\hp\Desktop\chromedriver.exe")
url ='https://ful.io/'
driver.get(url)
driver.maximize_window()
Social_media=driver.find_elements('xpath','//*[@id="__next"]/div[1]/div[5]/footer/div/div[1]/div[2]/a')
for Social_media_links in Social_media:
    print("Social_media : ",Social_media_links.get_attribute('href'))
    
Email=driver.find_element('xpath','//*[@id="__next"]/div[1]/div[5]/footer/div/div[2]/div[4]/div/a')
print("Email :",Email.text)
Contact=driver.find_element('xpath','//*[@id="__next"]/div[1]/div[5]/footer/div/div[2]/div[4]/div/p/a')
print("Contact :",Contact.text)
