from selenium import webdriver

Instance: None = None

def initialize_chrom_driver(): # Initialize the Chrome drive
    global Instance # this is the global instance 
    Instance = webdriver.Chrome() # creating chrome driver instance
    Instance.implicitly_wait(5)
    return Instance

def close_chrom_driver():
    global Instance
    Instance.quit()

