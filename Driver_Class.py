
from Login import LoginPage
import Test_001_Talent_Acquisition_Guest_Service_Profile as test1
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

login = LoginTest()
# Loading and Running First Test
login.setup()
login.testusercanlogin()
login.test1()
#login.teardown()

# Loading and Running Second Test

