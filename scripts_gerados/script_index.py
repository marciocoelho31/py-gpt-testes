from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='driver/chromedriver.exe')  # Caminho para o driver do Chromium

# Instancia o navegador
driver = webdriver.Chrome(service=service)

# Acessar a página de login da AcordeLab
driver.get("http://127.0.0.1:5500/AcordeLab/index.html")  # Substitua 'URL da Plataforma AcordeLab' pela URL correta

# Preencher e enviar o formulário de login
try:
    # Encontra o campo de e-mail e digita o e-mail
    email_input = driver.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys("email@acordelab.com.br")  # Inserir um e-mail válido

    # Encontra o campo de senha e digita a senha
    password_input = driver.find_element(By.ID, "senha")
    password_input.clear()
    password_input.send_keys("123senha")  # Substitua '123senha' pela senha correta

    # Clicar no botão de login para enviar o formulário
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()

    # Aguarda 3 segundos para finalizar o teste (Para visualizar a página após o login)
    time.sleep(3)

    # Verifica se o login foi bem-sucedido verificando a URL
    assert "home.html" in driver.current_url, "O login falhou ou não redirecionou corretamente"

    print("Teste de login bem-sucedido!")
except Exception as e:
    print(f"Ocorreu um erro durante o teste: {e}")
finally:
    # Fecha o navegador ao final do teste
    driver.quit()

# Este script realiza um teste de login na plataforma AcordeLab. Inicia-se abrindo o navegador em modo headless (opção que não abre a janela do navegador, para economizar recursos), acessa a página de login, preenche os campos de e-mail e senha e clica no botão de login.

# Para o correto funcionamento do script, é necessário substituir a 'URL da Plataforma AcordeLab' pela URL real da plataforma, assim como ajustar o caminho para o driver do Chromium ('/path/to/chromedriver') de acordo com o ambiente de desenvolvimento.

# Após a tentativa de login, o script aguarda 3 segundos antes de verificar a URL atual para confirmar se o login foi bem-sucedido, e ao final, fecha o navegador.
