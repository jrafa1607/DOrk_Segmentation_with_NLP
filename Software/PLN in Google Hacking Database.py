# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 18:45:01 2019
@author: JoãoRafael
"""

''' Descrição do Experimento 

- Divisão da Dork por Palavras (Token NLP);
- Divisão dos Tokens por Caracter;
- Remoção das Stopwords;
- Conversão dos Caracteres para Ascii;
'''

'''------Importando as bibliotecas e Atualizando os scripts para NLP--------'''
import pandas as pd
import numpy as np
import nltk

dataframe = pd.read_csv("C:/Endereço do Arquivo/Ghdb.csv", 
delimiter=";", error_bad_lines=False, engine='python')
'Endereço da Base de Dados'

dataframe.isnull().sum()
'Exibindo a quantidade de valores nulos no dataframe'

dataframe.fillna(' ', inplace=True)
'Substituindo os valores nulos por "missing".'

stopwords = [',', ':', ';', '"', '-', '=', "’", '!', '?', '”', "'", "''",'(',
')', '``', '@', '~', '/', '|', ' *', '*', '* ', '[,', '],', ',[', ',]', ',[,',
',],', '[', ']', '__', '_', '...', '+', '/\\', '\\', '****', '.', '\/', '$',
'#', '%', '¨', '¬', '&', '`', './', '/.', './', '/.', '||', '/*', '©']
'Stopwords do NLTK definidas para o experimento'

'''-- Algoritmo para contar a quantidade de atributos na base -------------'''

linhas = np.size(dataframe,0)
colunas = np.size(dataframe,1)
X = dataframe
'''Verifica-se a quantidade de linhas e colunas da base, e em seguida
faz uma cópia da base para a variável X'''

maior = 0
'inicia-se a varável que receberá a quantidade máxima de parametros'

for n in range (linhas):
    'Iniciando em 0, a cada linha faça:'
    
    token = X.iloc[n]['Dork']
    'A variável Operador recebe a Dork inteira de cada linha'

    token = nltk.word_tokenize(token)
    'A variável Operador é divida por Espaços'
    
    token = [c for c in token if not c in stopwords]
    'Remove todas as stopwords definidas na lista Stopwords'
    
    token = ''.join(token)
    'Unifica todos os Caracteres da Base'
    
    token = [c for c in token if not c in stopwords]
    'Remove todas as stopwords definidas na lista Stopwords'
    
    token = ''.join(token)
    'Unifica todos os Caracteres da Base'

    Tamanho = int(len(token))
    'A variável tamanho recebe a quantidade de parametros que a Dork possui'

    if Tamanho > maior:
        'Se a variável tamanho for maior que o máximo atual'
    
        maior = Tamanho
        'Atribui um novo valor máximo'
        
        print(X.iloc[n]['Dork'])
        print(maior)
        'Sempre que o algoritmo encontrar um novo valor máximo, ele exibe'
        'no Console a Dork e sua quantidade de caracteres.'
    
print(maior)
'Exibe o resultado Final'
'Resultado = 84'

'''------------------------- Execução do Algoritmo ------------------------ '''

c = -1
'''Ajusta a variável C para qual atributo será recebido o valor;
Escolheu-se -1 para que o laço de repetição 
consiga receber os valores de posição [0]'''

for i in range(maior):
    'Iniciando em 0, para cada coluna faça:'
    
    for n in range (linhas):
        'Iniciando em 0, a cada linha faça:'
            
        if X.iloc[n,i] == 'Missing':
            'Se o valor da célula for igual a missing, faça:'
                
            Dork = X.iloc[n]['Dork']
            'A variável Dork recebe a dork da linha N'
                
            Dork = nltk.word_tokenize(Dork)
            'A dork é tokenizada = Dividida em Corpus'
            
            Dork = [c for c in Dork if not c in stopwords]
            'Remove todas as stopwords definidas na lista Stopwords'
                        
            Dork = ''.join(Dork)
            'A String Dork recebe a lista tokenizada'
            'e a unifica em uma única variável'
            
            Dork = [c for c in Dork if not c in stopwords]
            'Remove todas as stopwords definidas na lista Stopwords'
                        
            Dork = ''.join(Dork)
            'A String Dork recebe a lista tokenizada'
            'e a unifica em uma única variável'

            DorkL = ""
            'Inicia-se uma nova variável com valor vazio.'
            
            if len(Dork) > c:
                
                DorkL = str(ord(str(Dork[c])))
                'Faz a Concatenação do Valor Ascii'
            
                X.iloc[n,i] = int(DorkL)
                'Atribui o valor'
                
            else:
                
                X.iloc[n,i] = 1
                'X.iloc[n,i] = 0'
                'Caso a Dork seja menor que o atributo informado,' 
                'não faz nada e atribui um valor nulo para a célula'
                    
    c = c + 1
    'A cada laço de repetição, aumenta o valor do contador' 
    'para ir ao próximo atributo'
    
'''---------------------Escrita da Variável no CSV--------------------------'''
    
X.to_csv('DorkDb_Final.csv', encoding='utf-8', index=False) 

'''UTF8 - Codificação UTF-8 binária do documento compatível com ASCII, 
permite que seu documento não tenha problemas com palavras acentuadas 
e outras particularidades de formatação. 

index=False Retira o index ao exportar os dados'''
