import time
import allure
from allure_commons.types import AttachmentType
from seleniumbase import BaseCase
from page_objects.salesflow import SalesFlow
from utilities.customLogger import LogGen


class SalesFunctions(BaseCase):
    logger = LogGen.loggen()

    def login_page(self):
        self.send_keys(SalesFlow.email, "admin")
        self.send_keys(SalesFlow.pswrd, "12345678")
        self.click(SalesFlow.login)
        self.maximize_window()

    def verify_quotationSent(self):
        time.sleep(10)
        element = self.find_element(SalesFlow.verify_quotation_send)
        aria_checked_value = element.get_attribute("aria-checked")
        if aria_checked_value == "true":
            self.logger.info("********** It is in quotation send state *******")
            assert True
        else:
            self.logger.info("********** It is in quotation state *******")
            allure.attach(self.driver.get_screenshot_as_png(), name="testScreen", attachment_type=AttachmentType.PNG)
            assert False

    def payment_verification(self):
        a = self.get_text(SalesFlow.payment_verify)
        if a == "Your payment has been successfully processed. Thank you!":
            self.logger.info("********** Payment Successfully Processed *******")
            assert True
        else:
            self.logger.info("********** Something went wrong! Payment cannot be Processed *******")
            allure.attach(self.driver.get_screenshot_as_png(), name="testScreen", attachment_type=AttachmentType.PNG)
            assert False

    def verify_saleOrder(self):
        time.sleep(1)
        self.wait_for_element_visible(SalesFlow.sale_order_status, timeout=21)
        element = self.find_element(SalesFlow.verify_sales_order)
        sale_checked_value = element.get_attribute("aria-checked")
        if sale_checked_value == "true":
            self.logger.info("********** It is in SALES ORDER  state *******")
            assert True
        else:
            self.logger.info("********** It is not in SALES ORDER state *******")
            allure.attach(self.driver.get_screenshot_as_png(), name="testScreen", attachment_type=AttachmentType.PNG)
            assert False

    def verify_po_mo_tp(self):
        time.sleep(5)
        a = self.get_text(SalesFlow.verify_po)
        b = self.get_text(SalesFlow.verify_projects)
        c = self.get_text(SalesFlow.verify_tasks)
        d = self.get_text(SalesFlow.verify_mo)

        if a == "Purchase" and b == "Projects" and c == "Tasks" and d == "Manufacturing":
            self.logger.info("********** Successfully created Purchase Order by Test Product 1  *******")
            self.logger.info("********** Successfully created Manufacture Order by Test Product 2  *******")
            self.logger.info("********** Successfully created Tasks and Projects by Test Product 3  *******")
            assert True
        else:
            self.logger.info("********** Failed! Purchase order, manufacture order, task and project does not created by Test Product 1, Test Product 2 ,Test Product 3 respectively *******")
            allure.attach(self.driver.get_screenshot_as_png(), name="testScreen", attachment_type=AttachmentType.PNG)
            assert False

    def verify_rfq_send(self):
        time.sleep(1)
        self.wait_for_element_visible(SalesFlow.pic_pdf, timeout=35)
        element = self.find_element(SalesFlow.rfq_send)
        sale_checked_value = element.get_attribute("aria-checked")
        if sale_checked_value == "true":
            self.logger.info("********** It is in RFQ send state *******")
            assert True
        else:
            self.logger.info("********** It is not in RFQ send state *******")
            allure.attach(self.driver.get_screenshot_as_png(), name="testScreen", attachment_type=AttachmentType.PNG)
            assert False

    def verify_purchaseorder(self):
        time.sleep(10)
        # self.wait_for_element(SalesFlow.rfq_send, timeout=20)
        element = self.find_element(SalesFlow.purchase_order)
        sale_checked_value = element.get_attribute("aria-checked")
        if sale_checked_value == "true":
            self.logger.info("********** It is in purchase order state *******")
            assert True
        else:
            self.logger.info("********** It is not in purchase order state *******")
            allure.attach(self.driver.get_screenshot_as_png(), name="testScreen", attachment_type=AttachmentType.PNG)
            assert False

    def verify_receipt(self):
        a = self.get_text(SalesFlow.receipt)
        if a == "Receipt":
            self.logger.info("********** Successfully created receipt *******")
            assert True
        else:
            assert False

    def verify_done_state(self):
        time.sleep(5)
        element = self.find_element(SalesFlow.verify_done_state)
        done_checked_value = element.get_attribute("aria-checked")
        if done_checked_value == "true":
            self.logger.info("********** It is in Done State *******")
            assert True
        else:
            self.logger.info("********** It is not in Done State *******")
            allure.attach(self.driver.get_screenshot_as_png(), name="testScreen",
                          attachment_type=AttachmentType.PNG)
            assert False






# self.click(SalesFlow.input_email)
        # self.send_keys(SalesFlow.input_email, "muhammadrauf271@gmail.com")
        # self.click(SalesFlow.input_phone)
        # self.send_keys(SalesFlow.input_phone, "03341153725")
        # self.click(SalesFlow.input_mobile)
        # self.send_keys(SalesFlow.input_mobile, "03341153778")
        # self.click(SalesFlow.save_close_btn)


