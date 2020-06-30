import Driver

def accounting_financial_statements():
    print('$$$$$$$$$$$$ Start select test $$$$$$$$$$$')
    Driver.Instance.implicitly_wait(200)
    Driver.Instance.find_element_by_xpath("//b[contains(text(),'Administer Testing')]").click()
    Driver.Instance.find_element_by_xpath("//b[contains(text(),'Administer Tests')]").click()
    print(Driver.Instance.find_element_by_xpath("//input[@id='whatsthis']").is_enabled())
    Driver.Instance.implicitly_wait(100)
    #select = driver.find_element_by_xpath("//option[contains(text(),'//option[contains(text(),'Talent Acquisition - Guest Service Profile   (Toke')]')]")
    #select.click()
    Driver.Instance.find_element_by_xpath("//option[contains(text(),'Accounting - Financial Statements   (Tokens: 1)')]").click()
    #print(driver.find_element_by_xpath("//input[@id='whatsthis']").is_enabled())

    Driver.Instance.find_element_by_xpath("//input[@name='add']").click()
    Driver.Instance.find_element_by_xpath("//input[@name='test']").click()
    print('$$$$$$$$$$$$ end select test $$$$$$$$$$$')

    print('$$$$$$$$$$$$ input user details $$$$$$$$$$$')
    Driver.Instance.find_element_by_xpath("//input[@name='txtFirstName']").send_keys("Ganesan")
    Driver.Instance.find_element_by_xpath("//body//div//div//div//input[2]").send_keys("Sivaraman")
    Driver.Instance.find_element_by_xpath("//body//input[3]").send_keys("ganesan@symphonytalent.com")
    Driver.Instance.find_element_by_xpath("//button[contains(text(),'Next')]").click()
    Driver.Instance.find_element_by_xpath("//button[contains(text(),'START')]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'CONTINUE')]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'Next')]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'Start Test')]").click()

    print('$$$$$$$$$$$$ Start first qiestion $$$$$$$$$$$')
    # Sample Question 1
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample Question 2
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 3
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 4
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 5
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 6
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 7
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 8
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 9
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 10
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 11
    Driver.Instance.find_element_by_xpath("//body//div//div//div//div//div//div//button[2]").click()
    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    # Sample question 12 to 24
    for i in range(14):
        Driver.Instance.implicitly_wait(1000)
        Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//div//div//div//input").send_keys("1200")
        Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//button[contains(text(),'ANSWER COMPLETE')]").click()

    Driver.Instance.find_element_by_xpath("//html//body//div//div//div//div//div//div//div//button[contains(text(),'CONTINUE')]").click()
    Driver.Instance.find_element_by_xpath("//button[contains(text(),'Exit')]").click()
