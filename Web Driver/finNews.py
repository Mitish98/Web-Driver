links = ['https://www.infomoney.com.br/', 'https://valor.globo.com/', 'https://www.investing.com/', 'https://exame.com/', 'https://www.istoedinheiro.com.br/', 'https://br.tradingview.com/']

tempo = input('Por quanto tempo você deseja acessar o site?')
tempo = int(tempo)

for link in links:
 
    # Importar as bibliotecas necessárias
    from selenium import webdriver
    import time

    # Iniciar o navegador
    driver = webdriver.Chrome()

    # Abrir o site do Google Trends e aguardar 15 segundos
    driver.get(link)
    time.sleep(tempo)