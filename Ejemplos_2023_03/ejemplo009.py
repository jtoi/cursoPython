#Cliente http para consumir un json
import requests
import ejemplo10_generadorHtml_Peliculas as generador

URL = "https://www.omdbapi.com/?apikey=1fec0e7&t="

peli = input("Ingrese la pelicula a buscar: ")
url = URL+peli

x = requests.get(url)

if x.status_code == 200:
    pelicula = x.json()
    print(x.json())
    generador.generarDocumentoHtml(pelicula)