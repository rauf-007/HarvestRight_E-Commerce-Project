from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import BaseCase
from selenium.webdriver import Keys
import time
from page_objects.salesflow import SalesFlow
from functions.salesflow_functions import SalesFunctions
from utilities.customLogger import LogGen


class VerifyTest03(BaseCase):
    logger = LogGen.loggen()

    def Testcase03(self):
        self.logger.info("********** Verifying HarvestRight Website Opens *********")
        self.open(SalesFlow.quotation_url)
        self.logger.info("********** HarvestRight Website Opens Successfully *********")
        self.logger.info("********** Verifying Login *********")
        SalesFunctions.login_page(self)
        self.logger.info("********** Login is Successful *********")
        self.logger.info("********** Verifying it opens the latest quotation *********")
        time.sleep(1)
        self.wait_for_element_clickable(SalesFlow.first_quot_rcord, timeout=21)
        self.click(SalesFlow.first_quot_rcord)
        self.logger.info("********** Latest quotation opens Successfully *********")
        self.logger.info("********** Verifying Quotation is downloaded *********")
        time.sleep(1)
        self.wait_for_element_clickable(SalesFlow.download_btn, timeout=10)
        self.click(SalesFlow.download_btn)
        self.wait_for_element_clickable(SalesFlow.download_QO, timeout=10)
        self.click(SalesFlow.download_QO)
        self.logger.info("********** Quotation is downloaded Successfully *********")
        self.logger.info("********** Verifying Timesheet is downloaded *********")
        time.sleep(1)
        self.wait_for_element_clickable(SalesFlow.download_btn, timeout=10)
        self.click(SalesFlow.download_btn)
        self.wait_for_element_clickable(SalesFlow.timesheets, timeout=10)
        self.click(SalesFlow.timesheets)
        self.logger.info("********** Timesheet is downloaded Successfully *********")
        self.logger.info("********** Verifying it redirects to the purchase *********")
        self.wait_for_element_clickable(SalesFlow.purchase, timeout=19)
        self.click(SalesFlow.purchase)
        self.logger.info("********** Successfully redirected to the purchase *********")
        time.sleep(3)
        self.logger.info("********** Verifying RFQ send by email *********")
        self.wait_for_element_clickable(SalesFlow.send_by_email, timeout=10)
        self.click(SalesFlow.send_by_email)
        time.sleep(3)
        self.wait_for_element_clickable(SalesFlow.send_btn, timeout=21)
        self.click(SalesFlow.send_btn)
        self.logger.info("********** Successfully send RFQ by email *********")
        time.sleep(1)
        SalesFunctions.verify_rfq_send(self)
        self.logger.info("********** Verifying RFQ is printed *********")
        self.wait_for_element_clickable(SalesFlow.print_rfq, timeout=10)
        self.click(SalesFlow.print_rfq)
        self.logger.info("********** RFQ printed Successfully *********")
        self.logger.info("********** Verifying Purchase order is confirmed *********")
        self.wait_for_element_clickable(SalesFlow.confirm_order, timeout=10)
        self.click(SalesFlow.confirm_order)
        self.logger.info("********** Successfully confirmed purchase order *********")
        self.logger.info("********** Verifying Purchase order is send by email *********")
        self.wait_for_element_clickable(SalesFlow.send_po_email, timeout=21)
        self.click(SalesFlow.send_po_email)
        self.wait_for_element_clickable(SalesFlow.send_po, timeout=21)
        self.click(SalesFlow.send_po)
        self.logger.info("********** Successfully send purchase order by email *********")
        SalesFunctions.verify_purchaseorder(self)
        SalesFunctions.verify_receipt(self)

