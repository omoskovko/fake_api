import requests


def get_request(url: str, params: dict | None = None) -> dict:
    if not params:
        params = {}
    resp = requests.get(url, params=params)
    if resp.ok:
        return {"status": "OK", "result": resp.json()}
    else:
        return {"staus": "ERROR", "result": resp.text}


def post_request(url: str, data: dict) -> dict:
    resp = requests.post(url, data)
    if resp.ok:
        return {"status": "OK", "result": resp.json()}
    else:
        return {"staus": "ERROR", "result": resp.text}
