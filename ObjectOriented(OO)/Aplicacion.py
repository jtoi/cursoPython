import TraductorFactory
from ITraductor import ITraductor

if __name__ == "__main__":
    traductor = TraductorFactory.get_traductor()
    if isinstance(traductor, ITraductor):
        traductor.traducir("Patata")
    else:
        print("ERROR")
