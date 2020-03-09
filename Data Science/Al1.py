import pandas as pd

uri="https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
uri2="https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
filmes = pd.read_csv(uri)
filmes.columns = ["filmeId","titulo","generos"]
notas = pd.read_csv(uri2)
notas.columns = ["usuarioId","filmeId","nota","momento"]
filmes.head()
notas["nota"].head()
notas["nota"].unique()
notas.describe()

