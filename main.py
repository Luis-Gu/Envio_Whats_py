"""
Class to automate sending messages on WhatsApp using
data extracted from a Google Sheets spreadsheet.
"""
import os
import time
import urllib.parse
from pandas import DataFrame
from selenium.common.exceptions import TimeoutException
from modules.setup_selenium import SetupWebDriver
from modules.sheets_python import SheetsPython
from modules.loading_dec import loading_decorator


class WhatsappBot:
    """
    Class to automate sending messages on
    WhatsApp using spreadsheet data.
    """
    def __init__(self) -> None:
        self.chrome_web_driver : str = os.path.join(os.getcwd(),r"assets\chromedriver.exe")
        self.id_sheets : str = 'Spreadsheet ID'  # Replace with the actual ID of your Google Sheets.
        self.range_sheets : str = 'Sheet Tab!A:Z'  # Replace with the correct tab and data range.


    def extract_data_from_sheets(self) -> DataFrame:
        """
        Extracts data from a Google Sheets spreadsheet.
        Returns:
            DataFrame: A pandas DataFrame containing the spreadsheet data.
        """
        data = SheetsPython().get_data_from_sheets(id_sheets=self.id_sheets,
                                                   range_sheets=self.range_sheets,
                                                   with_headers=True)
        return data

    @loading_decorator
    def login_in_whatsapp(self) -> SetupWebDriver:
        """
        Logs into WhatsApp Web using Selenium.
        Returns:
            SetupWebDriver: A custom Selenium WebDriver instance configured for the automation.
        """
        custom_selenium = SetupWebDriver(download_path= "Downloads_selenium",
                                         web_driver_path=self.chrome_web_driver,
                                         headless=False)
        custom_selenium.web_driver.get("https://web.whatsapp.com/")
        try:
            custom_selenium.easy_wait_and_click("//div[normalize-space(text())='Tudo']", 40)
            return custom_selenium
        except TimeoutException:
            return None

    @loading_decorator
    def make_message_whatsapp_and_send(self, infos_sheet : str) -> None:
        """
        Creates and sends WhatsApp messages based on the spreadsheet data.
        Args:
            infos_sheet (DataFrame): DataFrame containing the information to send messages.
        """
        selenium = self.login_in_whatsapp()

        for _, row in infos_sheet.iterrows():
            if row['Status'] == 'Devendo':
                nome = row['Nome']
                numero = row['Número']

                mensagem = (f"Oi, {nome}! Tudo bem? 😊\n\n"
                            "Passando só pra lembrar que tem um pagamento pendente com a gente. "
                            f"Se você já fez, pode desconsiderar essa mensagem, ok?\n\n"
                            "Qualquer coisa, é só me chamar! 👍")

                mensagem_codificada = urllib.parse.quote(mensagem)
                link_whatsapp = (f"https://web.whatsapp.com/send?phone={numero}"
                                 f"&text={mensagem_codificada}")
                self.send_message_in_whatsapp(link_whatsapp, selenium)

        selenium.easy_wait_and_click("//span[@aria-hidden='true' and @data-icon='menu']", 5)
        selenium.easy_wait_and_click("//div[@aria-label='Desconectar' and contains(text(), 'Desconectar')]", 5)
        selenium.easy_wait_and_click("//div[contains(text(), 'Desconectar') and contains(@class, 'x1c4vz4f')]", 5)
        selenium.easy_wait_and_click("//div[contains(text(), 'Acessar WhatsApp Web') and contains(@class, 'x579bpy')]", 5)

    def send_message_in_whatsapp(self, link : str, selenium : SetupWebDriver) -> None:
        """
        Sends a message via WhatsApp using the provided link.
        Args:
            link (str): The WhatsApp Web URL with the pre-filled message.
            selenium (SetupWebDriver): The Selenium WebDriver instance for automation.
        """
        selenium.web_driver.get(link)
        selenium.easy_wait_and_click("//span[@aria-hidden='true' and @data-icon='send']", 5)
        time.sleep(1.5)

if __name__ == "__main__":
    app = WhatsappBot()
    infos_sheets = app.extract_data_from_sheets()
    app.make_message_whatsapp_and_send(infos_sheets)
