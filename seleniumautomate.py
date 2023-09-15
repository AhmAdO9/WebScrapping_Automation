# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# import csv

# browzer = webdriver.Edge()
# browzer.implicitly_wait(3)
# browzer.get("https://google.com")
# browzer.maximize_window()
# # browzer.find_element(By.XPATH, "//textarea[@class='gLFyf']").click()
# browzer.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys("latest news")
# browzer.find_element(By.XPATH, "//div[@class='o3j99 LLD4me yr19Zb LS8OJ']").click()
# browzer.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc'] //input[@class='gNO89b'] ").click()
# browzer.find_element(By.XPATH, "//div[@class='yuRUbf'] //h3[@class='LC20lb MBeuO DKV0Md'] ").click()
# content = browzer.find_elements(By.XPATH, "//div[@class='news_Itm-cont'] // a")

# file = open("names.csv", "w")
# for i in content:
#     file.write(i.text)
#     file.write("\n")

# file.close()
