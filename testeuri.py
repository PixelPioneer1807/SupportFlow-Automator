import requests

def generate_completion():
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer euri-8624578c4c7770aefd377c87f950807302a17d37512765e52f10999a65d8c333"
    }
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Write a poem about artificial intelligence"
            }
        ],
        "model": "gpt-4.1-nano",
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print(data)

generate_completion()