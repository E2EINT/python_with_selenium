import Driver

def talent_acquisition_guest_service_profile():
    print('$$$$$$$$$$$$ Start select test $$$$$$$$$$$')
    Driver.Instance.implicitly_wait(200)
    Driver.Instance.find_element_by_xpath("//b[contains(text(),'Administer Testing')]").click()
    Driver.Instance.find_element_by_xpath("//b[contains(text(),'Administer Tests')]").click()
    print(Driver.Instance.find_element_by_xpath("//input[@id='whatsthis']").is_enabled())
    Driver.Instance.implicitly_wait(30)
    #select = driver.find_element_by_xpath("//option[contains(text(),'//option[contains(text(),'Talent Acquisition - Guest Service Profile   (Toke')]')]")
    #select.click()
    Driver.Instance.find_element_by_xpath("//option[contains(text(),'Talent Acquisition - Guest Service Profile   (Toke')]").click()
    #print(driver.find_element_by_xpath("//input[@id='whatsthis']").is_enabled())
    Driver.Instance.find_element_by_xpath("//input[@name='add']").click()
    Driver.Instance.find_element_by_xpath("//input[@name='test']").click()
    Driver.Instance.find_element_by_xpath("//input[@name='txtFirstName']").send_keys("Ganesan")
    Driver.Instance.find_element_by_xpath("//body//div//div//div//input[2]").send_keys("Sivaraman")
    Driver.Instance.find_element_by_xpath("//body//input[3]").send_keys("ganesan@symphonytalent.com")
    Driver.Instance.find_element_by_xpath("//button[contains(text(),'Next')]").click()
    # ----
    Driver.Instance.find_element_by_xpath("//button[contains(text(),'START')]").click()
    Driver.Instance.find_element_by_xpath("//*[ @ id = 'button5']").click()
    #Driver.Instance.find_element_by_xpath("//div[contains(text(), 'A fast learner')]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    Driver.Instance.find_element_by_xpath("//*[ @ id = 'button5']").click()
    Driver.Instance.implicitly_wait(2)
    #Driver.Instance.find_element_by_xpath("//div[contains(text(),'Ask Francis and Juan if there is any way you can h')]").click()
    Driver.Instance.find_element_by_xpath("//*[ @ id = 'button5']").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'Next')]").click()
    # Q1
    Driver.Instance.implicitly_wait(2)
    Driver.Instance.find_element_by_xpath("//*[@id='text2']").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # Q2
    Driver.Instance.implicitly_wait(2)
    Driver.Instance.find_element_by_xpath("//*[@id='text2']").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # Q3
    Driver.Instance.implicitly_wait(2)
    Driver.Instance.find_element_by_xpath("//*[@id='text2']").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # Q4
    Driver.Instance.implicitly_wait(2)
    Driver.Instance.find_element_by_xpath("//*[@id='text2']").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    print('$$$$$$$$$$$$ end of the select test $$$$$$$$$$$$$$$')




