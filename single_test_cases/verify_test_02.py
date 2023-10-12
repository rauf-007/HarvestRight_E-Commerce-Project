from seleniumbase import BaseCase
import time
from page_objects.salesflow import SalesFlow
from functions.salesflow_functions import SalesFunctions
from utilities.customLogger import LogGen


class VerifyTest02(BaseCase):
    logger = LogGen.loggen()

    def Testcase02(self):
        self.logger.info("********** Verifying HarvestRight Website Opens *********")
        self.open(SalesFlow.quotation_url)
        self.logger.info("********** HarvestRight Website Opens Successfully *********")
        self.logger.info("********** Verifying Login *********")
        SalesFunctions.login_page(self)
        self.logger.info("********** Login is Successful *********")
        self.logger.info("********** Verifying it opens the latest quotation *********")
        self.click(SalesFlow.first_quot_rcord)
        self.logger.info("********** Latest quotation opens Successfully *********")
        time.sleep(4)
        # self.wait_for_element_clickable(SalesFlow.send_by_email, timeout=10)

        self.logger.info("********** Verifying quotation send by e-mail *********")
        self.click(SalesFlow.send_by_email)
        time.sleep(2)
        self.wait_for_element_clickable(SalesFlow.send_btn, timeout=21)
        self.click(SalesFlow.send_btn)
        self.logger.info("********** Quotation Successfully send by e-mail *********")
        # self.wait_for_element_present(SalesFlow.send_btn, timeout=20)
        # time.sleep(9)
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SalesFlow.send_btn))
        # self.wait_for_element_clickable(SalesFlow.send_btn)
        time.sleep(6)
        SalesFunctions.verify_quotationSent(self)
        # def test_verify_customer_preview_sign_n_pay_credit_card_info_and_payment_verification(self):
        #     self.test_verify_send_by_email_and_it_changes_it_state_to_quotation_send_state()
        self.logger.info("********** Verifying it redirects to the Customer Preview *********")
        self.click(SalesFlow.customer_preview)
        self.logger.info("********** Redirects to the Customer Preview Successfully *********")
        self.logger.info("********** Verifying sign and pay is working *********")
        self.wait_for_element_present(SalesFlow.sign_n_pay_iframe, timeout=25)
        self.switch_to_frame(SalesFlow.sign_n_pay_iframe)
        self.click(SalesFlow.sign_n_pay)
        self.logger.info("********** Sign and pay is successful *********")
        time.sleep(1)
        self.logger.info("********** Verifying accept sign is working *********")
        self.wait_for_element_clickable(SalesFlow.accept_n_sign, timeout=21)
        self.click(SalesFlow.accept_n_sign)
        self.logger.info("********** Accept and sign is Successful *********")
        # self.wait_for_element_clickable(SalesFlow.stripe_terminal, timeout=20)
        self.logger.info("********** Verifying Credit card information entered *********")
        self.click(SalesFlow.creditcard, timeout=27)
        self.click(SalesFlow.cardnmbr)
        time.sleep(1)
        self.send_keys(SalesFlow.cardnmbr, "5200828282828210")
        time.sleep(1)
        self.send_keys(SalesFlow.expiration_month, "09")
        time.sleep(1)
        self.send_keys(SalesFlow.expiration_year, "28")
        time.sleep(1)
        self.send_keys(SalesFlow.card_code, "123")
        time.sleep(1)
        self.click(SalesFlow.pay)
        self.logger.info("********** Credit card information entered successfully *********")
        # time.sleep(25)
        self.wait_for_element_visible(SalesFlow.payment_verify, timeout=47)
        SalesFunctions.payment_verification(self)
        # def test_verify_download_functionalities_rfq_send_state_purchase_order_state(self):
        # self.test_verify_customer_preview_sign_n_pay_credit_card_info_and_payment_verification()
        self.logger.info("********** Verifying Quotation Download Functionality *******")
        self.click(SalesFlow.download)
        self.logger.info("********** Quotation is Downloaded Successfully *******")
        self.logger.info("********** Verifying it redirects to edit mode *******")
        self.click(SalesFlow.edit_mode)
        self.logger.info("********** Successfully redirects to edit mode *******")
        SalesFunctions.verify_saleOrder(self)
        SalesFunctions.verify_po_mo_tp(self)
        time.sleep(1)

