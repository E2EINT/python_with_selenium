from selenium import webdriver

Instance = None

def initialize_chrom_driver():
    global Instance
    Instance = webdriver.Chrome()
    Instance.implicitly_wait(5)
    return Instance

def close_chrom_driver():
    global Instance
    Instance.quit()

