
from Login import LoginPage
import Test_001_Talent_Acquisition_Guest_Service_Profile as test1
import Test_002_Accounting_Financial_Statements as test2
import T




import Driver

class LoginTest:
    def setup(self):
        Driver.initialize_chrom_driver()
    def testusercanlogin(self):
        LoginPage.GoToURL()
        LoginPage.Login()
    def teardown(self):
        Driver.close_chrom_driver()
    def test1(self):
        test1.talent_acquisition_guest_service_profile()
    def test2(self):
        test2.accounting_financial_statements()
    def test3(self):
        test3.typing_test()
    def test4(self):


login = LoginTest()
# Loading and Running First Test
##login.setup()
##login.testusercanlogin()
##login.test1()
#login.teardown()

# Loading and Running Second Test
##login.setup()
##login.testusercanlogin()
##login.test2()
#login.teardown()

# Loading and Running Third Test
login.setup()
login.testusercanlogin()
login.test3()
#login.teardown()
