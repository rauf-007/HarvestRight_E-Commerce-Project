import time
from seleniumbase import BaseCase
from page_objects.salesflow import SalesFlow
from functions.salesflow_functions import SalesFunctions
from utilities.customLogger import LogGen


class VerifyTest06(BaseCase):
    logger = LogGen.loggen()

    def Testcase06(self):
        self.logger.info("********** Verifying HarvestRight Website Opens *********")
        self.open(SalesFlow.puchaseorders_url)
        self.logger.info("********** HarvestRight Website Opens Successfully *********")
        self.logger.info("********** Verifying Login *********")
        time.sleep(1)
        SalesFunctions.login_page(self)
        self.logger.info("********** Login is Successful *********")
        self.logger.info("********** Verifying it opens the latest purchase order *********")
        time.sleep(1)
        self.click(SalesFlow.reference)
        time.sleep(1)
        self.click(SalesFlow.reference)
        time.sleep(2)
        self.click(SalesFlow.latest_po)
        self.logger.info("********** Latest purchase order opens successfully *********")
        time.sleep(3)
        self.logger.info("********** Verify it creates bill *********")
        self.click(SalesFlow.create_bill)
        time.sleep(2)
        self.click(SalesFlow.bill_date)
        self.send_keys(SalesFlow.bill_date, "12/12/2023")
        time.sleep(2)
        self.click(SalesFlow.confirm_bill)
        self.logger.info("********** Successfully created bill  *********")
        time.sleep(5)
        self.logger.info("********** Verify payment registered  *********")
        self.click(SalesFlow.register_payment)
        time.sleep(2)
        self.click(SalesFlow.create_payment)
        self.logger.info("********** Successfully registered Payment *********")
        time.sleep(7)

