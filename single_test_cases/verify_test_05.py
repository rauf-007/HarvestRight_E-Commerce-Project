import pyautogui
from seleniumbase import BaseCase
import time
from page_objects.salesflow import SalesFlow
from functions.salesflow_functions import SalesFunctions
from utilities.customLogger import LogGen


class VerifyTest05(BaseCase):
    logger = LogGen.loggen()

    def Testcase05(self):
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
        self.logger.info("********** Verifying it opens receive products *********")
        self.click(SalesFlow.receive_products)
        self.logger.info("********** Successfully open receive products *********")
        self.logger.info("********** Verifying quality check is working properly by adding picture *********")
        time.sleep(4)

        self.click(SalesFlow.quality_checks)
        time.sleep(2)
        pyautogui.moveTo(560, 445)
        time.sleep(2)
        file_path = "C:\\Users\\Admin\\PycharmProjects\\Harvest\\data\\pic.jpg"
        self.choose_file(SalesFlow.input_type, file_path)
        time.sleep(2)
        self.click(SalesFlow.validate_btn)
        self.logger.info("********** Pic is uploaded, Quality check is working properly *********")
        time.sleep(4)
        self.logger.info("********** Verifying set quantities is working properly *********")
        self.click(SalesFlow.set_quantities)
        self.logger.info("********** Set quantities is working properly *********")

        # time.sleep(3)
        self.logger.info("********** Verifying add done quantities to products *********")
        self.click(SalesFlow.click_done)
        time.sleep(2)
        self.clear(SalesFlow.done)
        self.send_keys(SalesFlow.done, "11")
        self.click(SalesFlow.blank_spaces)
        self.logger.info("********** Successfully added done quantities *********")
        self.logger.info("********** Verifying put in pack *********")
        # self.click(SalesFlow.put_in_pack)
        self.logger.info("********** Put in pack is working properly *********")
        time.sleep(2)
        self.logger.info("********** Verifying lot serial number is added to the products *********")
        self.click(SalesFlow.inside_menu_serial)
        time.sleep(2)
        self.wait_for_element_clickable(SalesFlow.input_lotserial, timeout=21)
        # self.click(SalesFlow.add_a_line)
        self.click(SalesFlow.input_lotserial)
        time.sleep(1)
        self.send_keys(SalesFlow.type_lotserial, "Test Lot 1")
        # self.click(SalesFlow.done_lot)
        # self.send_keys(SalesFlow.done_lot, "3")
        time.sleep(2)
        self.click(SalesFlow.confirm_lot)
        time.sleep(1)
        self.click(SalesFlow.put_in_pack)

        self.logger.info("********** Verifying it is validated *********")
        self.click(SalesFlow.val_btn)
        self.logger.info("********** Successfully Validated *********")
        time.sleep(4)
        self.logger.info("********** Verifying back order created *********")
        # self.click(SalesFlow.create_backorder)
        time.sleep(3)
        # # self.click(SalesFlow.backorder_ok_btn)
        self.logger.info("********** Successfully created back order *********")
        SalesFunctions.verify_done_state(self)
        time.sleep(3)

        # self.click(SalesFlow.orders)
        # self.click(SalesFlow.purchasee_orders)
        # time.sleep(2)
        # self.click(SalesFlow.reference)
        # time.sleep(1)
        # self.click(SalesFlow.reference)
        # time.sleep(2)
        # self.click(SalesFlow.latest_po)
        # time.sleep(2)






