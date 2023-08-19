# module : chromedriver_autoinstaller
# visit for source code 
# https://github.com/yeongbin-jo/python-chromedriver-autoinstaller/tree/master/chromedriver_autoinstaller


import os
import shutil
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
                                      


# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
