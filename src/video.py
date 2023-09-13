# src/video.py
import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = None  # название видео
        self.link = None  # ссылка на видео
        self.views = 0  # количество просмотров
        self.likes = 0  # количество лайков
        self._load_data()  # загрузка данных о видео

    def _load_data(self):
        api_key = os.getenv('YT_API_KEY')  # получение ключа API из переменной окружения
        youtube = build('youtube', 'v3', developerKey=api_key)  # создание объекта YouTube API
        response = youtube.videos().list(part='snippet,statistics', id=self.video_id).execute()  # выполнение запроса к API для получения данных о видео
        video = response['items'][0]  # получение первого видео в ответе
        snippet = video['snippet']  # получение данных о видео
        statistics = video['statistics']  # получение статистики о видео
        self.title = snippet['title']  # установка названия видео
        self.link = f"https://youtu.be/{self.video_id}"  # установка ссылки на видео
        self.views = int(statistics['viewCount'])  # установка количества просмотров
        self.likes = int(statistics['likeCount']) if 'likeCount' in statistics else 0  # установка количества лайков, если есть

    def __str__(self):
        return self.title if self.title else ''  # возвращение названия видео если оно есть, иначе пустую строку


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)  # вызов конструктора родительского класса
        self.playlist_id = playlist_id  # установка идентификатора плейлиста для видео














