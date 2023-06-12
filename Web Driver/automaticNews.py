# Importar as bibliotecas necessárias
from selenium import webdriver
import time

# Iniciar o navegador
tempo = input('Digite o tempo de navegação em cada site: ')
tempo = int(tempo)
driver = webdriver.Chrome()


# Abrir o site do Google Trends e aguardar 15 segundos
driver.get('https://trends.google.com.br/home?geo=BR&hl=pt-BR')
time.sleep(tempo)

# Trocar para a página do blog da Humanizae e aguardar mais 15 segundos
driver.get('https://techcrunch.com/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.gatesnotes.com/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.newyorker.com/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.theatlantic.com/world/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.chronicle.com/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.revistas.usp.br/eav')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://pll.harvard.edu/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.unicamp.br/unicamp/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://blogdagestao.ufsc.br/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www5.usp.br/tag/blog/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://sites.usp.br/techlaw/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://bigthink.com/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.cartacapital.com.br/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.dw.com/pt-br/not%C3%ADcias/s-7111')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://dasartes.com.br/resenhas/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://cafecomsociologia.com/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.responsabilidadesocial.com/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.psicologiamsn.com/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.politize.com.br/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.abralin.org/site/noticias/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://gpte.ai/')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://www.cloudskillsboost.google/paths/118')
time.sleep(tempo)

# Acessar a proxima página
driver.get('https://vercel.com/templates?framework=next.js')
time.sleep(tempo)

# Fechar o navegador
driver.quit()
