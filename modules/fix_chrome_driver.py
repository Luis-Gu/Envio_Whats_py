# [X] - Coletar a versão do chrome
# [X] - Fazer uma requisição da versão
# [X] - Extrair o arquivo de dentro da pasta baixada(.zip)
# [X] - Mover o arquivo para a pasta do bot (.\assets)
# [X] - Gerar uma recursividade no código do SetupSelenium
import re
import os
import requests
import zipfile

class FixWebDriver:
    """TODO"""
    def __init__(self) -> None:
        pass
# founded_itens = os.listdir(r'C:\Program Files\Google\Chrome\Application')
# founded_itens = os.listdir(r'C:\Program Files (x86)\Google\Chrome\Application')

    def verify_google_version(self) -> None:
        """TODO"""
        unidade = os.path.splitdrive(os.getcwd())[0]
        founded_itens = (os.listdir(unidade + r'\Program Files\Google\Chrome\Application')
                        if os.path.exists(unidade + r'\Program Files\Google\Chrome\Application')
                        else os.listdir(unidade + r'\Program Files (x86)\Google\Chrome\Application'))
        current_version = None
        for item in founded_itens:
            if re.match(r'^[\d\.]+$', item):  # Verifica se o item corresponde a um formato de versão
                if current_version is None or item < current_version:  # Compara com a maior versão encontrada
                    current_version = item
        if current_version:  # Verifica se uma versão válida foi encontrada
            print(f'Maior versão encontrada: {current_version}')
            return current_version

    def get_last_stable_version(self) -> str:
        """TODO"""
        url_chrome = 'https://googlechromelabs.github.io/chrome-for-testing/'
        page_html = requests.get(url_chrome, timeout=10).text
        version = re.findall(r'Stable\<\/a\>\<td\>\<code\>([\d\.]+)', page_html)[0]
        return version

    def version_request_download_and_select_folder(self, version: str) -> str:
        """TODO"""
        url_chrome = f'https://storage.googleapis.com/chrome-for-testing-public/{version}/win64/chromedriver-win64.zip'
        print(f"URL de download: {url_chrome}")

        try:
            response = requests.get(url_chrome, timeout=10)

            if response.status_code == 200:
                current_directory = os.getcwd()
                folder = os.path.join(current_directory, 'assets')
                if folder:
                    file_path = os.path.join(folder, "chromedriver-win64.zip")
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"Arquivo salvo com sucesso em: {file_path}")
                    return file_path
                else:
                    print("Nenhuma pasta selecionada. O download foi cancelado.")
            else:
                print(f"Erro ao baixar o arquivo. Código de status: {response.status_code}")
        except requests.exceptions.Timeout:
            print("Erro: A requisição ao servidor excedeu o tempo limite de 10 segundos.")

    def extract_file_from_zip(self, path: str) -> None:
        """TODO"""
        with zipfile.ZipFile(path, 'r') as zip_ref:
            print(path)
            zip_ref.extract(member='chromedriver-win64/chromedriver.exe',
                            path=os.path.join(os.getcwd(),
                                              "assets"))
        if os.path.exists(os.path.join(os.getcwd(),r'assets\chromedriver.exe')):
            os.remove(os.path.join(os.getcwd(),r'assets\chromedriver.exe'))

        os.rename(os.path.join(os.getcwd(),r'assets\chromedriver-win64\chromedriver.exe'),
            os.path.join(os.getcwd(),r'assets\chromedriver.exe'))
        os.removedirs(os.path.join(os.getcwd(),r'assets\chromedriver-win64'))
        os.remove(os.path.join(os.getcwd(),r'assets\chromedriver-win64.zip'))

if __name__ == "__main__":
    # FixWebDriver().get_last_stable_version()
    print("iniciando")
    current_version = FixWebDriver().get_last_stable_version()
    web_driver_path = FixWebDriver().version_request_download_and_select_folder(current_version)
    FixWebDriver().extract_file_from_zip(web_driver_path)
