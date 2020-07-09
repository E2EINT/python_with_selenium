import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\webdrivers\Chrom\chromedriver.exe")
driver = webdriver.Chrome()
#driver=webdriver.Firefox(executable_path="C:\webdrivers\Firefox\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\webdrivers\IE\IEDriverServer.exe")
#driver.get("https://www.fadvassessments.com/onlinetesting/gamma.html")
driver.get("https://gamma.skillcheck.com/onlinetesting/adminPortal/flashassets/login?returnUrl=%2Fhome%2Fdashboard")
driver.maximize_window() # to Maximize window
# Python explicit waits
delay=2 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@id='mat-input-0']")))
    #  By.XPATH, "//*[@id='mat-input-0']" you can mention //* aslo instaead //input but check it is working or not
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
    driver.close()

print(driver.title)
print(driver.find_element_by_xpath("//input[@id='mat-input-0']").is_displayed()) # find this elememnt is displayed
print(driver.find_element_by_xpath("//input[@id='mat-input-0']").is_enabled()) # find this element is eanbled
driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("qatest")
print(driver.find_element_by_xpath("//input[@id='mat-input-1']").is_displayed()) # find this elememnt is displayed
print(driver.find_element_by_xpath("//input[@id='mat-input-1']").is_enabled()) # find this element is eanbled
driver.find_element_by_xpath("//input[@id='mat-input-1']").send_keys("")
driver.find_element_by_xpath("//input[@id='mat-input-2']").send_keys("")

driver.find_element_by_xpath("//span[contains(text(),'Sign In')]").click()
print(driver.current_url)
#driver.implicitly_wait(100)
delay = 10 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Legacy View')]")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//span[contains(text(),'Legacy View')]").click()
#driver.implicitly_wait(10)
#driver.find_element_by_xpath("//a[contains(text(),'Privacy Policy')]").click()
#driver.back() # press back button on the browser page
#time.sleep(100)
#driver.forward() # press forward button on the browser page
#driver.close() # it will close only active window
#driver.quit() # it will close all of the windows
driver.find_element_by_xpath("//b[contains(text(),'Administer Testing')]").click()
driver.find_element_by_xpath("//b[contains(text(),'Administer Tests')]").click()
print(driver.find_element_by_xpath("//input[@id='whatsthis']").is_enabled())
driver.implicitly_wait(100)
#select = driver.find_element_by_xpath("//option[contains(text(),'//option[contains(text(),'Talent Acquisition - Guest Service Profile   (Toke')]')]")
#select.click()
driver.find_element_by_xpath("//option[contains(text(),'Talent Acquisition - Guest Service Profile   (Toke')]").click()
#print(driver.find_element_by_xpath("//input[@id='whatsthis']").is_enabled())
driver.find_element_by_xpath("//input[@name='add']").click()
#driver.find_element(By.XPATH,"//input[@name='add']").click() # this another approach to find elelemt usinf By class

# Python list box select element in the list
#item = driver.find_elements_by_name("req_name")
#dr=Select(item)
#dr.select_by_visible_text("GanesanTst ")

driver.find_element_by_xpath("//input[@name='test']").click()




