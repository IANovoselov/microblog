import json
from typing import Dict

import requests
from flask import current_app


def translate(text: str, target_language: str) -> Dict:
    """
    Запрос API Яндекс переводчика
    :param text: Текст, который переводим
    :param target_language: Язык, на который переводим
    :return:
    """

    # Настройки из Яндекс облака
    iam_token = current_app.config['TRANSLATE_TOKEN']
    folder_id = current_app.config['FOLDER_ID']

    texts = [text]

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(iam_token)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    if response.status_code != 200:
        return 'Error: the translation service failed'
    return json.loads(response.content.decode('utf-8-sig'))
