# from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager # Used for selenium compatability 
import time 
import urllib.request


url = "https://boothpics.com/263G"
driver = webdriver.Chrome(ChromeDriverManager().install())

def main():
    driver.get(url)
    time.sleep(2)
    element =  driver.find_element_by_tag_name("body")
    no_of_page_downs = 50 

    while no_of_page_downs:
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        no_of_page_downs -= 1

    parent_element = driver.find_elements_by_css_selector("img")


    for photo in parent_element:
        photo_url = photo.get_attribute("src").replace(".thumb","")
        filename= photo_url.split("/")[-1]
        response = urllib.request.urlretrieve(photo_url, filename)
        print(photo_url)
        time.sleep(1)    


if __name__ == "__main__":
    main()
