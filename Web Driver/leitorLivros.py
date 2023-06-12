links = ['https://edisciplinas.usp.br/pluginfile.php/4135364/mod_resource/content/1/TEXTO%20DA%20PE%C3%87A%20O%20REI%20DA%20VELA%20DE%20OSWALD%20DE%20ANDRADE.pdf','https://www.gutenberg.org/cache/epub/57895/pg57895-images.html', 'https://www.gutenberg.org/cache/epub/61653/pg61653-images.html', 'https://www.gutenberg.org/cache/epub/68541/pg68541-images.html', 'https://www.gutenberg.org/cache/epub/31347/pg31347-images.html', 'https://www.gutenberg.org/cache/epub/28526/pg28526-images.html', 'https://www.gutenberg.org/cache/epub/29997/pg29997-images.html', 'https://www.gutenberg.org/cache/epub/23620/pg23620.html', 'https://www.gutenberg.org/cache/epub/23621/pg23621.html', 'https://www.gutenberg.org/cache/epub/41293/pg41293-images.html', 'https://www.gutenberg.org/cache/epub/31657/pg31657-images.html', 'https://www.gutenberg.org/cache/epub/17610/pg17610-images.html', 'https://www.gutenberg.org/cache/epub/68691/pg68691-images.html','https://www.gutenberg.org/cache/epub/55797/pg55797-images.html', 'https://caleufscar.files.wordpress.com/2016/07/as-meninas-lygia-fagundes-telles.pdf','https://edisciplinas.usp.br/pluginfile.php/4135364/mod_resource/content/1/TEXTO%20DA%20PE%C3%87A%20O%20REI%20DA%20VELA%20DE%20OSWALD%20DE%20ANDRADE.pdf', 'https://www.revistas.usp.br/rieb/article/view/70471/73245', 'https://www.scielo.br/j/rh/a/FvkRjJxPkjF4Kpbbr63qSfC/?format=pdf&lang=pt']

tempo = input('Por quanto tempo você deseja acessar o site? Lembre-se que temos 15 livros a serem lidos e 280 segundos de leitura equivale a cerca de 1 hora no total')
tempo = int(tempo)

# Abrir arquivo CSV com as atualizações de leitura

for link in links:
 
    # Importar as bibliotecas necessárias
    from selenium import webdriver
    import time

    # Iniciar o navegador
    driver = webdriver.Chrome()

    # Abrir o site 
    driver.get(link)
    time.sleep(tempo)

# Atualizar arquivo CSV

