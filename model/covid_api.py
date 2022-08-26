import httpx

URL_BASE = 'https://covid19-brazil-api.vercel.app/api/report/v1/'

def getTodosEstados():
    """Retorna os casos por todos estados brasileiros"""
    return api(URL_BASE)


def getEstado(uf: str):
    """Retorna casos por estado brasileiro
        uf:str - o estado solicitado pelo usuário
    """
    url = f"{URL_BASE}brazil/uf/{uf}"
    dados = api(url)
    return dados


def api(url):
    """Requisição à API"""
    request = httpx.get(url)
    response = request.json()
    return response