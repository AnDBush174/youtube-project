import json
import os
from googleapiclient.discovery import build

from helper.youtube_api_manual import channel_id


class Channel:
    """Класс для YouTube-канала"""

    def __init__(self, channel_id: str) -> None:
        """Инициализирует экземпляр класса с указанным ID канала"""
        self.channel_id = channel_id
        self.title = ""
        self.description = ""
        self.url = ""
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0
        self.update_channel_info()

    def update_channel_info(self) -> None:
        """Обновляет информацию о канале"""
        service = self.get_service()
        request = service.channels().list(part="snippet,statistics", id=self.channel_id)
        response = request.execute()
        channel = response["items"][0]
        snippet = channel["snippet"]
        statistics = channel["statistics"]
        self.title = snippet["title"]
        self.description = snippet["description"]
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(statistics["subscriberCount"])
        self.video_count = int(statistics["videoCount"])
        self.view_count = int(statistics["viewCount"])

    @staticmethod
    def get_service():
        """Возвращает объект для работы с YouTube API"""
        api_key = os.getenv('YT_API_KEY')
        return build("youtube", "v3", developerKey=api_key)

    def to_json(self, file_path: str) -> None:
        """Сохраняет информацию о канале в файл JSON"""
        data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def print_info(self) -> None:
        """Выводит информацию о канале на консоль"""
        print("Название:", self.title)
        print("Описание:", self.description)
        print("Ссылка:", self.url)
        print("Количество подписчиков:", self.subscriber_count)
        print("Количество видео:", self.video_count)
        print("Количество просмотров:", self.view_count)

# Создание экземпляра класса Channel и обновление информации о канале
channel = Channel(channel_id)
channel.update_channel_info()

# Вывод информации о канале
channel.print_info()

# Сохранение информации о канале в файл JSON
channel.to_json("channel_info.json")

