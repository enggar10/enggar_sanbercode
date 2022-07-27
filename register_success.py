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
url="http://barru.pythonanywhere.com/daftar"
username="engg"
email="eng@yahoo.com"
password="eng"

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #test case pertama
    def test_success_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(3)
        driver.find_element(By.ID,"name_register").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys(email) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys(password) # isi password
        time.sleep(15)
        driver.find_element(By.ID,"signup_register").click()
        time.sleep(15)


    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()