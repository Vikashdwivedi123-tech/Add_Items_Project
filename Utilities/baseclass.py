import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        # loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('logfile.log')  # code for log file
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # filehandler object used for  in which format and file the log will be print.

        # This is the order of logging
        # If I passed label name as error then all(debug, info, warning, error,critical) will execute and so on.
        # above algo is applied for all label because they are all in order.

        logger.setLevel(logging.INFO)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

