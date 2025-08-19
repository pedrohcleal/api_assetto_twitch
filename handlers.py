from pyaccsharedmemory import accSharedMemory
import os
import json
import re


AC_BASE_PATH = r"S:\Steam\steamapps\common\assettocorsa\content\cars"
AC_TRACKS_PATH = r"S:\Steam\steamapps\common\assettocorsa\content\tracks"


def get_track_name_raw():
    asm = accSharedMemory()
    sm = asm.read_shared_memory()
    pista_atual = sm.Static.track
    cleaned = pista_atual.split('\x00')[0].strip()
    return cleaned

def get_info_pista():
    track_folder = get_track_name_raw()
    json_path = os.path.join(AC_TRACKS_PATH, track_folder, "ui", "ui_track.json")

    if not os.path.exists(json_path):
        return f"Arquivo não encontrado para a pista '{track_folder}'."

    with open(json_path, encoding="utf-8") as f:
        raw_data = f.read()

    cleaned_data = re.sub(r'[\x00-\x1F]+', ' ', raw_data)
    data = json.loads(cleaned_data)

    try:
        length_km = round(float(data.get("length", "0").replace('"','')) / 1000, 3)
    except:
        length_km = "N/D"

    resumo = (
        f"{data.get('name', 'Pista desconhecida')} - {data.get('description', '')}\n,"
        f"País: {data.get('country', 'N/D')}, Cidade: {data.get('city', 'N/D')}, "
        f"Comprimento: {length_km} km"
    )
    return resumo

def get_car_model_raw():
    """Pega o nome cru do carro (ex: 'ferrari_458_gt2')."""
    asm = accSharedMemory()
    sm = asm.read_shared_memory()
    carro_atual = sm.Static.car_model
    cleaned = carro_atual.split('\x00')[0].strip()
    return cleaned  # sem formatação

def get_car_model():
    """Pega o nome formatado do carro (ex: 'FERRARI 458 GT2')."""
    cleaned = get_car_model_raw()
    formatted = cleaned.replace('_', ' ').upper()
    return formatted

def get_track_name():
    asm = accSharedMemory()
    sm = asm.read_shared_memory()
    pista_atual = sm.Static.track
    cleaned = pista_atual.split('\x00')[0].strip()
    formatted = cleaned.replace('_', ' ').upper()
    return formatted

def get_info_carro():
    car_folder = get_car_model_raw()
    json_path = os.path.join(AC_BASE_PATH, car_folder, "ui", "ui_car.json")

    if not os.path.exists(json_path):
        return {"erro": f"Arquivo não encontrado: {json_path}"}

    with open(json_path, encoding="utf-8") as f:
        raw_data = f.read()

    cleaned_data = re.sub(r'[\x00-\x1F]+', ' ', raw_data)

    data = json.loads(cleaned_data)

    specs = data.get("specs", {})

    cavalos = specs.get("bhp", "").replace("bhp", "").strip()
    torque = specs.get("torque", "").replace("Nm", "").strip()
    peso = specs.get("weight", "").replace("kg", "").strip()
    velocidade_max = specs.get("topspeed", "").replace("km/h", "").strip().replace("+", "")
    pwratio = specs.get("pwratio", "").replace("kg/hp", "").strip()
    aceleracao = specs.get("acceleration", "").replace("s 0-100", "").replace("--", "").strip()

    resumo = (
        f"{data.get('name', 'Carro desconhecido')} ({data.get('brand', 'Marca desconhecida')}) — "
        f"{cavalos} Cavalos, {torque} Nm de Torque, Peso:{peso} kg, "
        f"0–100 km/h em {aceleracao or 'N/D'}s, "
        f"Relação peso/potência: {pwratio} kg/cv, "
        f"Velocidade máxima: {velocidade_max} km/h."
    )

    return resumo