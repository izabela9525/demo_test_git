from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\TestFiles\chromedriver.exe")
driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
title = driver.title
print(title)
assert 'Demobank - Bankowość Internetowa - Logowanie' == title
driver.quit()