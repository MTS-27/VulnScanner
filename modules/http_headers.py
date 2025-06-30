import requests

def get_headers(host):
    try:
        url = f"http://{host}"
        response = requests.get(url, timeout=3)
        return dict(response.headers)
    except Exception as e:
        print(f"[!] Could not retrieve HTTP headers: {e}")
        return {}

