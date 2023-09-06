import os
import requests


class Channel:
    def __init__(self, url):
        self.url = url
        self.subscribers = self.get_subscribers()  # Получение количества подписчиков при создании объекта

    def get_subscribers(self):
        api_key = os.environ.get('YT_API_KEY')
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.url}&key={api_key}')  # Получение информации о канале
        data = response.json()
        if 'items' in data:
            subscribers = int(
                data['items'][0]['statistics']['subscriberCount'])  # Извлечение количества подписчиков из данных
            return subscribers
        return 0

    def __str__(self):
        api_key = os.environ.get('YT_API_KEY')
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={self.url}&key={api_key}')  # Получение информации о канале
        data = response.json()
        if 'items' in data:
            channel_title = data['items'][0]['snippet']['title']  # Извлечение названия канала из данных
            channel_url = f"https://www.youtube.com/channel/{self.url}"
            return f"{channel_title} ({channel_url})"
        return self.url

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.subscribers + other.subscribers  # Сложение количества подписчиков двух каналов
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Channel' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self.subscribers - other.subscribers  # Вычитание количества подписчиков двух каналов
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Channel' and '{}'".format(type(other).__name__))

    def __gt__(self, other):
        if isinstance(other, Channel):
            return self.subscribers > other.subscribers  # Проверка, имеет ли текущий канал больше подписчиков, чем другой канал
        else:
            raise TypeError("Unsupported operand type(s) for >: 'Channel' and '{}'".format(type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Channel):
            return self.subscribers >= other.subscribers  # Проверка, имеет ли текущий канал больше или равное количество подписчиков, чем другой канал
        else:
            raise TypeError("Unsupported operand type(s) for >=: 'Channel' and '{}'".format(type(other).__name__))

    def __lt__(self, other):
        if isinstance(other, Channel):
            return self.subscribers < other.subscribers  # Проверка, имеет ли текущий канал меньше подписчиков, чем другой канал
        else:
            raise TypeError("Unsupported operand type(s) for <: 'Channel' and '{}'".format(type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Channel):
            return self.subscribers <= other.subscribers  # Проверка, имеет ли текущий канал меньшее или равное количество подписчиков, чем другой канал
        else:
            raise TypeError("Unsupported operand type(s) for <=: 'Channel' and '{}'".format(type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, Channel):
            return self.subscribers == other.subscribers  # Проверка, имеет ли текущий канал равное количество подписчиков, как и другой канал
        else:
            raise TypeError("Unsupported operand type(s) for ==: 'Channel' and '{}'".format(type(other).__name__))




