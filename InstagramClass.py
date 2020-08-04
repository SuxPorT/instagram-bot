from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot():

    def __init__(self, username, password):
        """ Construtor da classe
        Keyword arguments:
        username -- email de login do usuário
        password -- senha de login do usuário
        """
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')

    def like_photos(self, hashtag):
        """ Função que irá curtir as fotos da página
        Keyword arguments:
        hashtag -- nome da página
        """
        if hashtag:
            default_link = "https://www.instagram.com/p/"
            self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}")
            time.sleep(5)

            for i in range(3):
                # Scroll para poder gerar as fotos da página
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)

            # Seleção de todos os elementos que são links da página
            hrefs = self.driver.find_elements_by_tag_name('a')
            picture_hrefs = [element.get_attribute("href") for element in hrefs]

            print(f"\nPágina: #{hashtag}\nNúmero de foto para curtir: {str(len(picture_hrefs))}")

            for picture_href in picture_hrefs:
                # Verificação se o link é de uma foto da página
                if default_link in picture_href:
                    self.driver.get(picture_href)

                    try:
                        self.driver.find_element_by_xpath("//span[@class='fr66n']").click()

                        # Espera para a transição de uma foto para outra
                        time.sleep(20)

                    except Exception as e:
                        time.sleep(5)
        else:
            print("Nenhuma página selecionada. Encerrando o programa")
            exit()

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)

        # Input do HTML indicando o email de login do usuário
        user_element = self.driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(1)

        # Input do HTML indicando a senha de login do usuário
        password_element = self.driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)

        # Simula a tecla 'ENTER'
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
