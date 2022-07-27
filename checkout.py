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
url="https://www.saucedemo.com/"
email="standard_user"
password="secret_sauce"
FN="eng"
LN="eng"
kpos="65162"

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #test case pertama
    def test_success_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.NAME,"login-button").click()
        time.sleep(1)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.ID,"shopping_cart_container").click()
        time.sleep(1)
        driver.find_element(By.ID,"checkout").click()
        time.sleep(1)
        driver.find_element(By.NAME,"firstName").send_keys(FN) 
        time.sleep(1)
        driver.find_element(By.NAME,"lastName").send_keys(LN) 
        time.sleep(1)
        driver.find_element(By.NAME,"postalCode").send_keys(kpos) 
        time.sleep(1)
        driver.find_element(By.ID,"continue").click()
        time.sleep(1)
        driver.find_element(By.ID,"finish").click()
        time.sleep(1)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()