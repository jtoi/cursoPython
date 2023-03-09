import requests
from ejemplo10_generadorHtml_Peliculas import generarDocumentoHtml as generador

API_KEY = "1fec0e7"
URL = 'https://www.omdbapi.com/?apikey=' + API_KEY + '&t=' 


def getMovie(url, apikey, titulo):
    urlLlamada = URL + titulo
    respuesta = requests.get(urlLlamada)
    if respuesta.status_code == 200:
        movie_info = respuesta.json()
    else:
        movie_info = None

    return movie_info

if __name__ == '__main__':
    titulo = input("Ingrese el titulo del peli: ")
    
    movie_info = getMovie(URL, API_KEY, titulo)
    if movie_info is not None:
        generador(movie_info.get("Title"), movie_info.get("Poster"), movie_info.get("Director") )
    else:
        print("Ha ocurrido un error")

    #getMovie(URL, API_KEY, 'The Godfather')
    #getMovie(URL, API_KEY, 'The Shawshank Redemption')