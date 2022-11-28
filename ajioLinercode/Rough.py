import time

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
d = webdriver.Chrome(executable_path=r"C:\Users\SunnyPatil\Downloads\chromedriver_win32\chromedriver.exe")

d.get("https://www.ajio.com/")
time.sleep(2)
d.close()