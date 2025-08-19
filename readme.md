# Assetto Corsa API 🚗🏁

API em Flask para expor informações em tempo real do **Assetto Corsa**, como carro atual, pista atual e especificações detalhadas.
A leitura é feita via [`pyaccsharedmemory`](https://pypi.org/project/pyaccsharedmemory/), que acessa a memória compartilhada do simulador.

## 📂 Estrutura do Projeto

```
.
├── main.py        # Arquivo principal com a definição das rotas Flask
├── handlers.py    # Funções auxiliares para extrair e formatar dados
└── requirements.txt
```

## ⚙️ Requisitos

* Python 3.10+
* Assetto Corsa instalado (com `shared memory` habilitado)
* Pacotes Python listados em `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

## 🚀 Como rodar

No terminal:

```bash
python main.py
```

Por padrão, a API sobe em:

```
http://0.0.0.0:5000
```

## 📌 Endpoints

### 🔹 Carro Atual

`GET /carro_atual`
Retorna o modelo do carro atualmente selecionado.

Exemplo de resposta:

```
FERRARI 458 GT2
```

---

### 🔹 Pista Atual

`GET /pista_atual`
Retorna o nome da pista atual.

Exemplo:

```
MONZA
```

---

### 🔹 Informações do Carro

`GET /info_carro`
Retorna informações detalhadas sobre o carro atual (extraídas de `ui_car.json`).

Exemplo:

```
Ferrari 458 GT2 (Ferrari) — 470 Cavalos, 520 Nm de Torque, Peso:1245 kg, 0–100 km/h em 3.4s, Relação peso/potência: 2.65 kg/cv, Velocidade máxima: 310 km/h.
```

---

### 🔹 Informações da Pista

`GET /info_pista`
Retorna informações detalhadas sobre a pista atual (extraídas de `ui_track.json`).

Exemplo:

```
Monza - Autodromo di Monza,
País: Italy, Cidade: Monza (MI), Comprimento: 5.793 km
```

---

## 🛠️ Observações

* Os caminhos padrão de instalação do Assetto Corsa estão definidos em `handlers.py`:

  ```python
  AC_BASE_PATH = r"S:\Steam\steamapps\common\assettocorsa\content\cars"
  AC_TRACKS_PATH = r"S:\Steam\steamapps\common\assettocorsa\content\tracks"
  ```

  Se o jogo estiver instalado em outro diretório, ajuste essas variáveis.
* Se não houver carro/pista carregados, a API retorna mensagens como:

  ```
  sem nenhum carro no momento
  sem pista no momento
  ```

---

## 📜 Licença

Projeto para uso pessoal/educacional. Sem afiliação oficial com a Kunos Simulazioni.

---

👉 Quer que eu já monte também um **`requirements.txt`** baseado no teu código (Flask + pyaccsharedmemory) pra complementar o projeto?
