import os
from googleapiclient.discovery import build

class Channel:
    def __init__(self, channel_id):
        # Получение API-ключа из переменной окружения
        api_key = os.getenv('YT_API_KEY')
        # Переменная channel_id обозначена в конструкторе класса
        self.channel_id = channel_id
        # Создание объекта YouTube Data API с использованием api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def print_info(self):
        # Выполнение запроса к YouTube Data API для получения информации о канале
        channel_info = self.youtube.channels().list(
            part='snippet',
            id=self.channel_id
        ).execute()

        if channel_info['items']:
            # Извлечение информации о канале из ответа
            channel_snippet = channel_info['items'][0]['snippet']
            channel_title = channel_snippet['title']
            channel_description = channel_snippet['description']

            # Вывод информации о канале
            print("Channel information:")
            print(f"Title: {channel_title}")
            print(f"Description: {channel_description}")
        else:
            # Вывод сообщения об ошибке, если информацию о канале не удалось получить
            print("Unable to fetch channel information.")

