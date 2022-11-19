import re
import requests
import nltk
import math
import numpy as np
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')

sentencas = []
sentencas2 = []
BZ = []
BOW = []
TF = []
IDF = []
conclusao = []
TFIDF = []

paginas = [
  "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP",
  "https://hbr.org/2022/04/the-power-of-natural-language-processing",
  "https://en.wikipedia.org/wiki/Natural_language_processing",
  "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html",
  "https://monkeylearn.com/natural-language-processing/"
]

for site in paginas:
  pagina = requests.get(site)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  paragrafos = soup.find_all(['p'])

  regex = re.compile(
    r'''([A-Z][ ]?([("]?[\w][")]?[,]?[ ]?[-]?[']?){20,}[.])''')

  for i in range(0, len(paragrafos)):
    texto = paragrafos[i].get_text()
    check = regex.finditer(texto)
    for i in check:
      sentencas.append(i[0])

regex = re.compile(r'''([\w][']?[-]?)+''')
for i in range(0, len(sentencas)):
  palavras = regex.finditer(sentencas[i])
  for palavra in palavras:
    sentencas2.append(palavra[0])

palavrasSeparadas = set(sentencas2)
#print(palavrasSeparadas)

for n in range(0, len(palavrasSeparadas)):
  BZ.append(0)

for x in range(0, len(sentencas)):

  BOW.append(BZ.copy())
  palavras = regex.finditer(sentencas[x])
  for palavra in palavras:
    p = palavra[0]
    n = 0
    for palavra in palavrasSeparadas:
      if (palavra == p):
        BOW[x][n] += 1
        break
      n += 1

# TF
for i in BOW:
  print(i)
