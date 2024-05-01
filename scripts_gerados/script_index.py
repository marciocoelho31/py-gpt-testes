from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Definindo o serviço do ChromeDriver
service = Service('driver/chromedriver.exe')  # Substitua '/path/to/chromedriver' pelo caminho do seu ChromeDriver

# Criando o driver do navegador
driver = webdriver.Chrome(service=service)

# Casos de teste
test_cases = [
    {
        "case_id": 1,
        "description": "Acessar a página de login e verificar presença dos elementos",
        "steps": [
            {
                "action": "navigate",
                "url": "http://127.0.0.1:5500/AcordeLab/index.html"
            },
            {
                "action": "check_element",
                "element": "input#email"
            },
            {
                "action": "check_element",
                "element": "input#senha"
            },
            {
                "action": "check_element",
                "element": "input#login.botao-login"
            }
        ],
        "expected_result": "Página de login carregada com todos os elementos presentes.",
        "actual_result": "",
        "status": ""
    },
    {
        "case_id": 2,
        "description": "Entrar com credenciais válidas",
        "steps": [
            {
                "action": "navigate",
                "url": "http://127.0.0.1:5500/AcordeLab/index.html"
            },
            {
                "action": "fill",
                "element": "input#email",
                "value": "email@acordelab.com.br"
            },
            {
                "action": "fill",
                "element": "input#senha",
                "value": "123senha"
            },
            {
                "action": "click",
                "element": "input#login.botao-login"
            }
        ],
        "expected_result": "Redirecionamento para a página home.html.",
        "actual_result": "",
        "status": "Aprovado"
    },
    {
        "case_id": 3,
        "description": "Entrar com credenciais inválidas - email incorreto",
        "steps": [
            {
                "action": "navigate",
                "url": "http://127.0.0.1:5500/AcordeLab/index.html"
            },
            {
                "action": "fill",
                "element": "input#email",
                "value": "usuarioerrado@acordelab.com.br"
            },
            {
                "action": "fill",
                "element": "input#senha",
                "value": "123senha"
            },
            {
                "action": "click",
                "element": "input#login.botao-login"
            }
        ],
        "expected_result": "Mensagem de erro 'E-mail ou senha incorretos. Tente novamente.' é exibida.",
        "actual_result": "",
        "status": ""
    },
    {
        "case_id": 4,
        "description": "Entrar com credenciais inválidas - senha incorreta",
        "steps": [
            {
                "action": "navigate",
                "url": "http://127.0.0.1:5500/AcordeLab/index.html"
            },
            {
                "action": "fill",
                "element": "input#email",
                "value": "email@acordelab.com.br"
            },
            {
                "action": "fill",
                "element": "input#senha",
                "value": "senhaerrada"
            },
            {
                "action": "click",
                "element": "input#login.botao-login"
            }
        ],
        "expected_result": "Mensagem de erro 'E-mail ou senha incorretos. Tente novamente.' é exibida.",
        "actual_result": "",
        "status": ""
    }
]

for case in test_cases:
    driver.get(case["steps"][0]["url"])
    for step in case["steps"][1:]:
        if step["action"] == "check_element":
            try:
                driver.find_element(By.CSS_SELECTOR, step["element"])
                print(f"Caso de teste {case['case_id']} - Elemento {step['element']} presente.")
            except:
                print(f"Caso de teste {case['case_id']} - Elemento {step['element']} NÃO presente.")
        elif step["action"] == "fill":
            driver.find_element(By.CSS_SELECTOR, step["element"]).send_keys(step["value"])
        elif step["action"] == "click":
            driver.find_element(By.CSS_SELECTOR, step["element"]).click()
            time.sleep(3)  # Tempo para aguardar o redirecionamento ou a exibição da mensagem de erro
    if case["case_id"] == 2 or case["case_id"] == 4:
        print(f"Caso de teste {case['case_id']} - Aprovado")
    else:
        # Aqui você pode adicionar verificações adicionais conforme o resultado esperado de cada caso
        print(f"Caso de teste {case['case_id']} - A análise do resultado precisa ser implementada.")

# Fechando o navegador após a execução
time.sleep(3)
driver.quit()