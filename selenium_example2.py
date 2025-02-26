from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurações do navegador
options = Options()
options.add_argument("--headless")  # Executar sem abrir a interface do navegador
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Inicializa o navegador com as opções configuradas
driver = webdriver.Chrome(options=options)

# Acessa o Google
driver.get("https://www.google.com")

# Aguarda um tempo para garantir que a página carregou
time.sleep(2)

# Encontra o campo de pesquisa
search_box = driver.find_element(By.NAME, "q")

# Digita "Selenium Python" e pressiona Enter
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Aguarda um tempo para carregar os resultados
time.sleep(3)

# Salva o título da página para verificar se funcionou
print("Título da página:", driver.title)

# Fecha o navegador
driver.quit()
