from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Configurando o serviço do driver do Chromium
service = Service('driver/chromedriver.exe')
service.start()

# Abrindo o navegador
driver = webdriver.Chrome(service=service)

time.sleep(3)

# URL da plataforma AcordeLab
url = "http://127.0.0.1:5500/AcordeLab/index.html"

try:
    # Acessando a URL da plataforma AcordeLab
    driver.get(url)
    
    # Verificando se a página foi carregada corretamente
    assert "AcordeLab" in driver.title
    
    # Clicando no botão "Entrar"
    #entrar_button = driver.find_element(By.XPATH, "//button[text()='Entrar']")
    #entrar_button.click()
    
    # Verificando se a página de login foi carregada
    assert "Index - AcordeLab" in driver.title
    
    # Preenchendo o campo de nome de usuário ou e-mail
    username_field = driver.find_element(By.ID, "email")
    username_field.send_keys("email@acordelab.com.br")
    
    # Preenchendo o campo de senha
    password_field = driver.find_element(By.ID, "senha")
    password_field.send_keys("123senha")
    
    # Clicando no botão "Entrar" para efetuar o login
    login_button = driver.find_element(By.CLASS_NAME, "botao-login")
    login_button.click()
    
    # Verificando se o login foi realizado com sucesso

    assert "Home - AcordeLab" in driver.title
    
    # Verificando se Ana foi redirecionada para a página inicial logada
    # assert "Bem-vinda, Ana!" in driver.page_source
    
    # Verificando se todos os recursos da plataforma estão acessíveis para Ana
    # assert "Recursos Disponíveis" in driver.page_source

    print("Teste de login na plataforma AcordeLab realizado com sucesso!")

finally:
    # Aguardando 3 segundos antes de fechar o navegador
    time.sleep(3)
    driver.quit()
    service.stop()
