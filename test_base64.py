import base64
from urllib.parse import urlparse, parse_qs

def decode_base64_url(short_url):
    """
    Kisi bhi URL se Base64 string dhoondh kar usko decode karta hai.
    """
    try:
        parsed_url = urlparse(short_url)
        query_params = parse_qs(parsed_url.query)
        
        for key, values in query_params.items():
            for val in values:
                if val.startswith('aHR0'):
                    # Padding Fix Karna 
                    padding_needed = len(val) % 4
                    if padding_needed:
                        val += '=' * (4 - padding_needed)
                    
                    decoded_bytes = base64.urlsafe_b64decode(val)
                    final_url = decoded_bytes.decode('utf-8')
                    
                    if final_url.startswith('http'):
                        return final_url
        return None 
    except Exception as e:
        print(f"Decode Error: {e}")
        return None

if __name__ == "__main__":
    print("🧪 Testing Base64 Decoder...\n")
    test_link_1 = "https://short.com/?link=aHR0cHM6Ly90Lm1lL01vZEFwa1NoYXJlQm90"
    test_link_2 = "https://rocklinks.net/?url=aHR0cHM6Ly9nb29nbGUuY29t" # Padding missing
    
    print("Test 1 Result:", decode_base64_url(test_link_1))
    print("Test 2 Result:", decode_base64_url(test_link_2))
