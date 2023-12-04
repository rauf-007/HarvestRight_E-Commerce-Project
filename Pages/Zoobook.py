import time
import pyautogui
from seleniumbase import BaseCase
from utilities.customLogger import LogGen
from selenium.webdriver import Keys


class VerifyTest07(BaseCase):
    logger = LogGen.loggen()

    def Login(self):
        self.open("https://staging.zoobooksystems.com/")
        self.logger.info("Successfully login")
        self.maximize_window()

    def Email(self):
        self.click("//input[@name='zb-username']")
        self.send_keys("//input[@name='zb-username']", "AAAdmin")

    def Password(self):
        self.click("//input[@name='zb-password']")
        self.send_keys("//input[@name='zb-password']", "@zb1234!")

    def LoginBtn(self):
        self.click("//button[@class='btn btn-lg btn-success btn-block login-button']")
        time.sleep(7)

    def AddClient(self):
        pyautogui.moveTo(300, 245)
        self.click("//a[@target='_self'][normalize-space()='Add Client']")
        time.sleep(4)

    def FirstName(self):
        self.click("//input[@placeholder='First Name']")
        self.send_keys("//input[@placeholder='First Name']" ,"Haroon")

    def LastName(self):
        self.click("//input[@placeholder='Last Name']")
        self.send_keys("//input[@placeholder='Last Name']","Jamal")

    def Dob(self):
        self.click("//input[@id='birth_Date']")
        self.send_keys("//input[@id='birth_Date']", "11/28/1998")
        time.sleep(2)

    def MartialStatus(self):
        self.click("//span[@id='select2-maritalStatus-container']")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", "Never")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", Keys.ENTER)

    def Status(self):
        self.click("//span[@id='select2-statusId-container']")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", "Active")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", Keys.ENTER)
        time.sleep(3)

    def SSN(self):
        self.click("//input[@id='SSN']")
        self.send_keys("//input[@id='SSN']", "033151925")
        time.sleep(7)

    def SelectGender(self):
        self.click("//span[@id='select2-gender-container']")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", "Male")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", Keys.ENTER)
        time.sleep(5)

    def RequestedServices(self):
        self.click("//input[@data-text='Substance Abuse Assessment' or @data-text='Mental Health' or @ data - text = 'Sober Housing' or @data-text='Intensive Outpatient']")
        time.sleep(5)

    def PrimaryRace(self):
        self.click("//span[@id='select2-primaryRace-container']")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", "Decli")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", Keys.ENTER)

    def SecRace(self):
        self.click("//span[@id='select2-secondaryRace-container']")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", "Decli")
        self.send_keys("//body/span[3]/span[1]/span[1]/input[1]", Keys.ENTER)

    def SaveBtn(self):
        self.scroll_to_bottom()
        self.click("//div[@id='details']//div[@class='panel-footer']//button[1]")
        time.sleep(3)

    def YesBtn(self):
        self.click("//button[normalize-space()='Yes']")
        time.sleep(3)

    def ViewClient(self):
        self.open("https://staging.zoobooksystems.com/Clients/ViewClients")
        time.sleep(4)

    def ClickName(self):
        self.click("//a[contains(text(),'Jamal , Haroon')]")

        time.sleep(5)

    def StatusPending(self):
        self.click("//span[@id='select2-statusId-container']")
        self.send_keys("//input[@role='textbox']", "Pending")
        self.send_keys("//input[@role='textbox']", Keys.ENTER)
        # self.click("//div[@class='row pending-status-panel']")
        time.sleep(3)

    def PendingClt(self):
        self.open("https://staging.zoobooksystems.com/Clients/ViewClients/3")
        time.sleep(2)

    def VerifyClickName(self):
        a = "//a[contains(text(),'Jamal , Haroon')]"
        b = self.get_text(a)
        if b == "Jamal , Haroon":
            assert True
            self.logger.info("Haroon is present in the list")
        else:
            self.logger.info("Haroon is not present in the list")
            assert False
        time.sleep(5)


