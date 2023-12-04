from utilities.customLogger import LogGen
from Pages.Zoobook import VerifyTest07

class SalesTest(VerifyTest07):
    logger = LogGen.loggen()

    def test_01(self):
        self.Login()
        self.Email()
        self.Password()
        self.LoginBtn()
        self.AddClient()
        self.FirstName()
        self.LastName()
        self.Dob()
        self.MartialStatus()
        self.Status()
        self.SSN()
        self.SelectGender()
        self.RequestedServices()
        self.PrimaryRace()
        self.SecRace()
        self.SaveBtn()
        self.YesBtn()
        self.ViewClient()
        self.ClickName()
        self.StatusPending()
        self.SaveBtn()
        self.PendingClt()
        self.VerifyClickName()















