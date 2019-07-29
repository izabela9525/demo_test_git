import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    def test_demo_login(self):
        driver = webdriver.Chrome(executable_path="C:\TestFiles\chromedriver.exe")
        driver.get('https://demobank.jaktestowac.pl/logowanie_prod.html ')
        title = driver.title
        print(title)
        assert 'Demobank - Strona główna - Logowanie' == title
        driver.quit()