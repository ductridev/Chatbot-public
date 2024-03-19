import requests
import os
from dotenv import load_dotenv
load_dotenv()

def stt(mp3):
    url = 'https://api.fpt.ai/hmi/asr/general'
    payload = open(f'{mp3}', 'rb').read()
    api_key = os.getenv('TTS_API_KEY')
    headers = {
        'api-key': api_key,
    }

    response = requests.post(url=url, data=payload, headers=headers)

    print(response.json())
