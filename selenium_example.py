from selenium import webdriver

# Inicializa o navegador (Chrome)
driver = webdriver.Chrome()

# Abre o Google
driver.get("https://www.google.com")

# Mantém o navegador aberto até que o usuário pressione Enter
input("Pressione Enter para fechar o navegador...")

# Fecha o navegador
driver.quit()
