import Driver

def talent_acquisition_guest_service_profile():
    print('$$$$$$$$$$$$ Start select test $$$$$$$$$$$')
    Driver.Instance.implicitly_wait(200)
    Driver.Instance.find_element_by_xpath("//b[contains(text(),'Administer Testing')]").click()
    Driver.Instance.find_element_by_xpath("//b[contains(text(),'Administer Tests')]").click()
    print(Driver.Instance.find_element_by_xpath("//input[@id='whatsthis']").is_enabled())
    Driver.Instance.implicitly_wait(100)
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
    Driver.Instance.find_element_by_xpath("//button[contains(text(),'START')]").click()
    # sample Question 1
    Driver.Instance.find_element_by_xpath("//body//button[3]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # sample Question 2
    Driver.Instance.find_element_by_xpath("//body//button[3]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Click on Next button
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'Next')]").click()
    # Q1
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # Q2
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # Q3
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # Q4
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # Q5
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Q6
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Q7
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Q8
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Q9
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Q10
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Q11
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Q12
    Driver.Instance.find_element_by_xpath("//body//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()
    # Q 13 to 40
    for i in range(41):
        # Q13 to 40
        Driver.Instance.find_element_by_xpath("//body//button[2]").click()
        Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Test Complete page click on Continue Button
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//div//button[contains(text(),'CONTINUE')]").click()

    # Test Finished page click on Exit Button
    Driver.Instance.find_element_by_xpath("//button[contains(text(),'Exit')]").click()

    print('$$$$$$$$$$$$ end select test $$$$$$$$$$$')




