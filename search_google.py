#from dbm.ndbm import library
import dbm
import unittest
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#variable
url="https://www.google.com/"
cari ="quality assurance"


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #test case pertama
    def test_success_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"q").send_keys(cari)
        time.sleep(3)
        driver.find_element(By.NAME,"btnK").click()
        time.sleep(15)
        
        

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()