import json
import requests
from app import app

IAM_TOKEN = app.config['TRANSLATE_TOKEN']
folder_id = app.config['FOLDER_ID']


def translate(text, target_language):

    texts = [text]

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    if response.status_code != 200:
        return 'Error: the translation service failed.'
    return json.loads(response.content.decode('utf-8-sig'))


