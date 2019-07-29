import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    def test_demo_login(self):
        driver = webdriver.Chrome(executable_path="C:\TestFiles\chromedriver.exe")
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title
        driver.quit()

    def test_demo_accounts(self):
        driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        driver.get('https://demobank.jaktestowac.pl/konta.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Konta' == title
        driver.quit()

    def test_demo_pulpit(self):
        driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
        driver.get('https://demobank.jaktestowac.pl/pulpit.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Pulpit' == title
        driver.quit()

class MainTests2(unittest.TestCase):
    def test_demo_login(self):
        driver = webdriver.Chrome(executable_path="C:\TestFiles\chromedriver.exe")
        driver.get('https://demobank.jaktestowac.pl/logowanie_prod.html ')
        title = driver.title
        print(title)
        assert 'Demobank - Strona główna - Logowanie' == title
        driver.quit()