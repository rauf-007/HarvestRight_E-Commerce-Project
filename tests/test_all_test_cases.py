from utilities.customLogger import LogGen
from page_objects.salesflow import SalesFlow
from single_test_cases.verify_test_01 import VerifyTest01
from single_test_cases.verify_test_02 import VerifyTest02
from single_test_cases.verify_test_03 import VerifyTest03
from single_test_cases.verify_test_04 import VerifyTest04
from single_test_cases.verify_test_05 import VerifyTest05
from single_test_cases.verify_test_06 import VerifyTest06
from functions.salesflow_functions import SalesFunctions


class SalesTest(SalesFlow, SalesFunctions, VerifyTest01, VerifyTest02, VerifyTest03, VerifyTest04, VerifyTest05, VerifyTest06):
    logger = LogGen.loggen()

    def test_01(self):
        self.Testcase01()
        """
        This Test Case Verify all below points:
        1) Sale module opens ,and it redirects to the sale module.
        2) It redirects to the new quotation.
        3) Then it selects the customer and entered data in new quotation and verify data successfully entered in new quotation.
        4) Then it add 3 products and verify all 3 products added to new quotation.
        5) First product is of MTO and buy, second is of MTO and Manufacture, third is of Project and task.
        6) Then it verifies this new quotation is saved with all the above data.
        """

    def test_02(self):
        self.Testcase02()
        """
        This Test Case Verify all below points:
        1) First it opens the quotation which was created by above Test_01.
        2) Then it send this quotation by send by email button and verify email send successfully.
        3) Then it verify that this quotation is in quotation send state.
        4) Then it go to the customer preview and sign and pay the quotation then it accept the sign.
        5) Then it entered the credit card information and verify payment successfully processed and it also verify it is downloaded.
        6) Then it go back to edit mode and verify sale order created successfully and checks it is in sale order state after payment is processed.
        7) Then it verify that the purchase order, manufacture order and task project are created successfully by the 3 products which was added in Test_01.
        """

    def test_03(self):
        self.Testcase03()
        """
        This Test Case Verify all below points:
        1) First it opens the sale order which was created by above test_02.
        2) Then it clicks on download button and download Quotation/Order and timesheet.
        3) Then it go to purchase and send this order by email.
        4) After sending email it verifies that it is in rfq send state.
        5) Then it print the rfq.
        6) After that it confirms the order and send PO by email and verify that it is in purchase order state.
        7) Then it verify that the receipt is created successfully by this purchase order.
        """

    def test_04(self):
        self.Testcase04()
        """
         This Test Case Verify all below points:
         1) First it opens the purchase order which was created by above test_03.
         2) Then it downloads PO, RFQ, Picking Operations, Delivery Slip, Packages respectively.
         3) Then it click on print labels and print all the 6 labels with price and without price.
         """

    def test_05(self):
        self.Testcase05()
        """
        This Test Case Verify all below points:
        1) First it opens the purchase order which was created by above test_03.
        2) Then it receive products and quality check this by add any image to it.
        3) Then it set quantities and add done quantities to the available product.
        4) Then it put in pack and add random lot serial number to the available products.
        5) Then it validate and create backorder for that.
        6) After that it verify that it is in the Done State.
        """

    def test_06(self):
        self.Testcase06()
        """
        This Test Case Verify all below points:
        1) First it opens the  order which was created by above test_05.
        2) Then it creates bill.
        3) Then it registers payment.
        """









