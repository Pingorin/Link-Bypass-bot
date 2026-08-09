import requests
from bs4 import BeautifulSoup
import time
import base64
from urllib.parse import urlparse, parse_qs

def decode_base64_url(short_url):
    """URL se Base64 string dhoondh kar usko decode karta hai."""
    try:
        parsed_url = urlparse(short_url)
        query_params = parse_qs(parsed_url.query)
        
        for key, values in query_params.items():
            for val in values:
                if val.startswith('aHR0'):
                    padding_needed = len(val) % 4
                    if padding_needed:
                        val += '=' * (4 - padding_needed)
                    
                    decoded_bytes = base64.urlsafe_b64decode(val)
                    final_url = decoded_bytes.decode('utf-8')
                    
                    if final_url.startswith('http'):
                        return final_url
        return None
    except Exception as e:
        print(f"Base64 Decode Error: {e}")
        return None

def bypass_adlinkfly(url):
    """Adlinkfly based shorteners ko bypass karta hai (e.g., shortxlinks.in)."""
    try:
        client = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": url
        }
        client.headers.update(headers)
        
        res = client.get(url, timeout=15)
        soup = BeautifulSoup(res.content, "html.parser")
        inputs = soup.find_all("input")
        data = {inp.get("name"): inp.get("value") for inp in inputs if inp.get("name")}
        
        if not data:
            return None
        
        time.sleep(6) # 6 Sec Timer bypass
        
        headers["X-Requested-With"] = "XMLHttpRequest"
        post_res = client.post(url, data=data, headers=headers, timeout=15)
        
        try:
            json_data = post_res.json()
            if "url" in json_data:
                return json_data["url"]
        except Exception:
            pass
        return None
    except Exception as e:
        print(f"Adlinkfly Bypass Error: {e}")
        return None
