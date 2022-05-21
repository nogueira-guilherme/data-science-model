"""""""""""""""""""""""""""""""""""
        TÍTULO DO PROJETO
"""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""
          IMPORTAÇÕES
"""""""""""""""""""""""""""""""""
import os
import numpy as np
import pandas as pd
import datetime as date
import matplotlib.pyplot as plt

from tabulate import tabulate


"""""""""""""""""""""""""""""""""
       PROGRAMA PRINCIPAL
"""""""""""""""""""""""""""""""""

print("Hello, World!")

# Links para os dados
uri_ratings = 'https://raw.githubusercontent.com/nogueira-guilherme/model-data-science/master/Data/ratings.csv'
uri_movies  = 'https://raw.githubusercontent.com/nogueira-guilherme/model-data-science/master/Data/movies.csv'

# Armazenando os dados em DataFrame
movies = pd.read_csv(uri_movies)
movies.columns = ["moviesId", "titles", "genres"]
movies.head()

# Armazenando os dados em DataFrame
ratings = pd.read_csv(uri_ratings)
ratings.columns = ["userId", "movieId", "rating", "timestamp"]
ratings.head()


# Manipulações
print(f'\n{ratings["rating"]}')

print(f'\nValores Únicos: {ratings["rating"].unique()}\n')

print(f'\nMédia das Notas: {ratings["rating"].mean():.2f}\n')

print(f'\nMenor Nota: {ratings["rating"].min()}\n')

print(f'\nDescrição:\n {ratings.describe()}\n')

print(f'\n{tabulate(ratings.describe(), headers=["userId", "movieId", "rating", "timestamp"], tablefmt="psql", floatfmt=".2f")}')






