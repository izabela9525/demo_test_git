import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    def test_Lessons_page(self):
        driver = self.driver
        driver.get('https://www.typing.com/student/lessons')
        title = driver.title
        print(title)
        assert 'Typing Lessons | Learn Touch Typing - Typing.com' == title

    def test_Tests_page(self):
        driver = self.driver
        driver.get('https://www.typing.com/student/tests')
        title = driver.title
        print(title)
        assert 'Take a Typing Test - Typing.com' == title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()