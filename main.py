
from flask import Flask
from handlers import get_track_name, get_info_pista, get_car_model, get_info_carro

app = Flask(__name__)


@app.get("/carro_atual")
def carro():
    try:
        car = get_car_model()
    except:
        return 'sem nenhum carro no momento'
    return car

@app.get("/pista_atual")
def pista():
    try:
        track = get_track_name()
    except:
        return 'sem pista no momento'
    return track

@app.get("/info_carro")
def info_carro():
    try:
        info_carr = get_info_carro()
    except:
        return 'sem carro no momento'
    return info_carr


@app.get("/info_pista")
def info_pista():
    try:
        info_track = get_info_pista()
    except:
        return 'sem pista no momento'
    return info_track

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
