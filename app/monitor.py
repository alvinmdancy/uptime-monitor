import requests

def check_url(url: str):
    try:
        response = requests.get(url, timeout=5)
        return {
            "url": url,
            "status_code": response.status_code,
            "reachable": True
        }
    except requests.RequestException:
        return {
            "url": url,
            "status_code": None,
            "reachable": False
        }
