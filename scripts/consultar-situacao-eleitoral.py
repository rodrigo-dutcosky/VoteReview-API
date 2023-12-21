from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

def consultar_situacao(cpf:str):

    ### definindo o navegador utilizado (google chrome)
    chrome = Service(ChromeDriverManager().install())

    ### definindo os parametros da sessao (tamanho da tela)
    opcoes = Options()
    opcoes.add_argument('--window-size=900,900')
    
    ### criando a instancia Chrome, representando uma nova sessao
    driver = webdriver.Chrome(service = chrome, options = opcoes)
    sleep(5)
    
    ### navegando ate o website da url
    driver.get("https://www.tse.jus.br/servicos-eleitorais/titulo-e-local-de-votacao/copy_of_consulta-por-nome")
    sleep(5)

    ### interagindo com elemento html (inserindo o texto)
    driver.find_element(By.ID, "SE_NomeTituloCPF").send_keys(cpf)
    sleep(5)

    ### interagindo com elemento html (clicando no botao)
    driver.find_element(By.ID, "consulta-situacao-eleitoral-form-submit").click()

    ### condicional para aguardar o tempo necessario da consulta
    waiter = WebDriverWait(driver, 20)
    
    ### tempo de espera = 20s, ou caso a condicao seja atendida
    try:
        
        ### coletando o resultado referenciando a tag html atraves do valor do seu ID
        result = waiter.until(expected_conditions.visibility_of_element_located((By.ID, "return-form-situacao-eleitoral")))
        status = result.text.split("\n")[3]
        
    ### determinando o status = ERRO caso ocorra algum erro durante a execucao do codigo acima
    except:
        status = "ERRO"
        
    ### fechando a conexao da sessao Chrome antes de retornar o valor encontrado
    driver.quit()
    
    return status

