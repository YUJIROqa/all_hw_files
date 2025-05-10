import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from POM.pages.sale_page import SalePage
from time import sleep

def test_header_title(driver2):
    sale_page = SalePage(driver2)
    sale_page.open_page()
    sale_page.check_page_header_title_is('Sale')
    sleep(3)
