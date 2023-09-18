# src/video.py
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = None
        self.like_count = None

        if self.video_id:
            try:
                self._load_data()  # загрузка данных о видео
            except (IndexError, HttpError):
                pass

    def _load_data(self):
        api_key = os.getenv('YT_API_KEY')  # получение ключа API из переменной окружения

        if not api_key:
            return

        youtube = build('youtube', 'v3', developerKey=api_key)  # создание объекта YouTube API

        try:
            response = youtube.videos().list(part='snippet,statistics',
                                             id=self.video_id).execute()  # выполнение запроса к API для получения данных о видео
            video = response['items'][0]  # получение первого видео в ответе
            snippet = video['snippet']  # получение данных о видео
            statistics = video['statistics']  # получение статистики о видео
            self.title = snippet['title']  # установка названия видео
            self.link = f"https://youtu.be/{self.video_id}"  # установка ссылки на видео
            self.views = int(statistics['viewCount'])  # установка количества просмотров
            self.likes = int(
                statistics['likeCount']) if 'likeCount' in statistics else 0  # установка количества лайков, если есть
        except (IndexError, KeyError, HttpError):
            pass

    def __str__(self):
        return self.title or ''
