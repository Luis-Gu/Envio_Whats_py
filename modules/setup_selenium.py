"""
    Module responsible for creating an instance
    for a WebDriver (Chrome )and configuring it.
    As an additional feature, it has some functions
    that facilitate Selenium interactions with some elements.
"""
# ---- BASE PYTHON LIBS ----◹
import json
import time
import os
from typing import Any
# --------------------------◿

# ------------------------ IMPORTED LIBS -----------------------◹
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, ElementClickInterceptedException, SessionNotCreatedException
from undetected_chromedriver import Chrome as UnChrome
from undetected_chromedriver import ChromeOptions as UnChromeOptions
from modules.fix_chrome_driver import FixWebDriver

# --------------------------------------------------------------◿

class SetupWebDriver:
    """
        Configuration for a base selenium.
        Allows you to define the download path and the
        "headless" option, but it is not recommended
        for the testing phase.
    """
    def __init__(self,
                 download_path : str,
                 web_driver_path : str,
                 headless : bool = False,
                 local_user : bool = False,
                 undetected : bool = False) -> None:
        self.download_path   : str = os.path.join(os.getcwd(),download_path)
        self.web_driver_path : str = web_driver_path
        self.headless : bool = headless or False
        self.profile_path : str = os.path.join(os.path.expanduser("~"),r'\AppData\Local\Google\Chrome\User Data\Profile 5')[2:]
        self.local_user : bool = local_user
        self.undetected = undetected
        self.web_driver : Chrome = self.__config_and_start_a_webdriver()

    def __config_and_start_a_webdriver(self) -> Chrome:
        """
            Configure selenium and start a webdriver

        Returns:
            Chrome: Selenium driver ready to operate
        """
        if self.undetected:
            options : UnChromeOptions = UnChromeOptions()
        else:
            options : ChromeOptions = ChromeOptions()
        app_state : dict[str,str|int|list[dict[str,str]]] = {
            "recentDestinations": [
                {
                    "id": "Save as PDF",
                    "origin": "local" 
                }
            ],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }


        prefs : dict[str,Any]= {'printing.print_preview_sticky_settings.appState': json.dumps(app_state),
                                'savefile.default_directory':self.download_path,
                                'download.prompt_for_download': False,
                                'download.directory_upgrade': True,
                                'plugins.always_open_pdf_externally': True,
                                'download.default_directory' : self.download_path}
        options.add_experimental_option("prefs",prefs)
        options.add_argument('--kiosk-printing')
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        if self.local_user:
            options.add_argument(f"user-data-dir={self.profile_path}")
        if self.headless:
            options.add_argument("--headless=new")
        # options.add_argument('--disable-print-preview')
        # options.add_argument('--disable-printer-selection')
        # options.add_argument('--disable-popup-blocking')
        # options.add_argument('--disable-infobars')
        try:
            if self.undetected:
                chrome = UnChrome(service=Service(executable_path=self.web_driver_path,
                                                log_output='SELENIUM_LOGS'),
                                options=options,
                                driver_executable_path=self.web_driver_path)
            else:
                chrome = Chrome(service=Service(self.web_driver_path,log_output='SELENIUM_LOGS'),
                                options=options)
        except SessionNotCreatedException:
            self.fix_chrome_driver()
            self.__config_and_start_a_webdriver()

        return chrome

    def accept_alert(self, search_time : float) -> str:
        """
            Search for a Alert in WebDriver instace
            and accept it.
            Sometime the alet is important, so i get
            it every time.

        Args:
            search_time (float): How long the search time needs to be

        Returns:
            str: Text present in alert body
        """
        while search_time >= 0:
            try:
                alert_text : str = Alert(self.web_driver).text
                Alert(self.web_driver).accept()
                break
            except NoAlertPresentException:
                time.sleep(0.1)
                search_time -= 0.1
        return alert_text

    def easy_wait_and_click(self, xpath : str, search_time : float = 5) -> None:
        """
            Wait for an element to appear and be clickable,
            after that clicks on the element

        Args:
            xpath (str): Web element xpath
            search_time (float): How long the search time needs to be
        """
        WebDriverWait(self.web_driver, search_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.web_driver.find_element('xpath', xpath).click()

    def easy_wait_and_click_greed_version(self, xpath : str, search_time : float = 10) -> None:
        """
            Wait for an element to appear and be clickable,
            after that keep trying to click.
            But 

        Args:
            xpath (str): Web element xpath
            search_time (float): How long the search time needs to be
        """
        while True:
            try:
                WebDriverWait(self.web_driver, search_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                self.web_driver.find_element('xpath', xpath).click()
                break
            except ElementClickInterceptedException:
                pass

    def easy_wait_and_send_keys(self, xpath  : str, keys : str, clear: bool = True, search_time : float = 5) -> None:
        """
            Wait for an element to appear and be clickable,
            after which Selenium cleans the element, if necessary,
            and sends the information

        Args:
            xpath (str): Web element xpath
            keys (str): keys to be inserted in element
            clear (bool, optional): Clear element before insertion?. Defaults to False.
            search_time (float): How long the search time needs to be
        """
        WebDriverWait(self.web_driver, search_time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        if clear:
            self.web_driver.find_element('xpath', xpath).clear()
        self.web_driver.find_element('xpath', xpath).send_keys(keys)

    # def download(self, download_xpath : str, file_extension : list[str])  -> str:
    #     """
    #         Click on download button, by the xpath in arguments,
    #         then wait it ends

    #     Args:
    #         download_xpath (str): Web element xpath

    #     Returns:
    #         str: last download path
    #     """
    #     previous_folder_state : list = os.listdir(self.download_path)
    #     self.easy_wait_and_click(xpath=download_xpath,
    #                              search_time=10)
    #     after_folder_state : list = os.listdir(self.download_path)
    #     while previous_folder_state == after_folder_state:
    #         time.sleep(0.5)
    #         after_folder_state = os.listdir(self.download_path)
    #     last_download : str = self.__most_recent_file()
    #     while not  f'.{last_download.split('.')[-1]}' in file_extension:
    #         time.sleep(0.5)
    #         last_download = self.__most_recent_file()
    #     time.sleep(1)
    #     last_download = self.__most_recent_file()
    #     return last_download

    def __most_recent_file(self) -> str:
        """
            Read download path and look for
            the most rescent file

        Returns:
            str: Most recent file of a folder path as a string 
        """
        files = os.listdir(self.download_path)
        paths = [os.path.join(self.download_path, basename) for basename in files]
        return max(paths, key=os.path.getctime)

    def refresh_page(self) -> None:
        """Refresh Page"""
        Chrome().refresh()
        time.sleep(1.5)

    def fix_chrome_driver(self) -> None:
        """Update Chrome Drive"""
        current_version = FixWebDriver().get_last_stable_version()
        web_driver_path = FixWebDriver().version_request_download_and_select_folder(current_version)
        FixWebDriver().extract_file_from_zip(web_driver_path)
