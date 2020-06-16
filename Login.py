
import Driver
class LoginPage:
    @staticmethod
    def GoToURL():
        print("&&&&&&&&&&&&&&& Launch The URL  &&&&&&&&&&&&&")
        #Driver.Instance.get("https://gamma.skillcheck.com/onlinetesting/adminPortal/flashassets/login")
        Driver.Instance.get("https://gamma.skillcheck.com/onlinetesting/adminPortal/flashassets/login?returnUrl=%2Fhome%2Fdashboard")
        Driver.Instance.maximize_window()  # to Maximize window
        print("&&&&&&&&&&&&&&& End of launching Login &&&&&&&&&&&&&")

    @staticmethod
    def Login():
        print(Driver.Instance.title)
        print("%%%%%%%%%%%% Start Login %%%%%%%%%%%")
        Driver.Instance.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("qatest")
        Driver.Instance.find_element_by_xpath("//input[@id='mat-input-1']").send_keys("administrator")
        Driver.Instance.find_element_by_xpath("//input[@id='mat-input-2']").send_keys("Sk1llCheck!")
        Driver.Instance.find_element_by_xpath("//span[contains(text(),'Sign In')]").click()
        Driver.Instance.implicitly_wait(100)
        print('-------------------------------')
        Driver.Instance.find_element_by_xpath("//span[contains(text(),'Legacy View')]").click()
        print('%%%%%%%%%%%%%% end login %%%%%%%%%%')
