import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import PySimpleGUI as sg
import os
class bot:
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Email')],
            [sg.Input(key='login')],
            [sg.Text('Senha')],
            [sg.Input(key='senha', password_char='*')],
            [sg.Text('Link da WebSala')],
            [sg.Input(key='websala')],
            [sg.OK()]
        ]
        
        self.janela = sg.Window('Abrir Sala Mconf',layout)

        while True:
            self.evento, self.valores = self.janela.Read()
            if self.evento == sg.WIN_CLOSED:
                break
            if self.evento == 'OK':
                self.autenticar()
            
       

    def autenticar(self):
        #chrome_options = Options()
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Edge(executable_path=os.getcwd() + os.sep + 'msedgedriver.exe')
        self.driver.get(self.valores['websala'])
        time.sleep(5)
        
        print('Clicando em conta não federada..')
        conta_nao_federada = self.driver.find_element_by_xpath('//*[@class="local-sign-in-trigger"]')
        conta_nao_federada.click()
        time.sleep(3)

        print('Digitando email..')
        email = self.driver.find_element_by_xpath('//input[@id="user_login"]')
        email.send_keys(self.valores['login'])
        time.sleep(1)

        print('Digitando senha..')
        senha = self.driver.find_element_by_xpath('//input[@id="user_password"]')
        senha.send_keys(self.valores['senha'])
        time.sleep(1)

        print('Entrando..')
        entrar = self.driver.find_element_by_xpath('//input[@name="commit"]')
        entrar.click()
        time.sleep(3)

        confirmar = self.driver.find_element_by_xpath('//input[@class="btn btn-submit"]')
        confirmar.click()
        print('Autenticado com sucesso!')
        time.sleep(5)

        print('Definindo opção somente ouvir..')
        somente_ouvir = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[2]')
        somente_ouvir.click()
        time.sleep(5)

        print('Definindo reunião para até 75 pessoas..')
        pequena = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/button')
        pequena.click()
        time.sleep(5)

        gerenciar = self.driver.find_element_by_xpath('//button[@class="button--Z2dosza sm--Q7ujg primary--1IbqAO ghost--Z136aiN optionsButton--ZcRNoL"]')
        gerenciar.click()
        time.sleep(2)

        print('Definindo politicas de convidados..')
        politica_convidados = self.driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/div/div/div[3]/div[1]/div/div/div/ul/li[5]/span[1]')
        politica_convidados.click()
        time.sleep(2)

        print('Permitindo que todos convidados consigam entrar..')
        permitir_todos = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/button[2]/span')
        permitir_todos.click()
        time.sleep(1)
        print('Sala aberta com sucesso!')

bot = bot()
