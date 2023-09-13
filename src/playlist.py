# playlist.py
import os
from datetime import timedelta
from googleapiclient.discovery import build
import pprint


class PlayList:
    def __init__(self, playlist_id, api_key=None):
        self.playlist_id = playlist_id
        self.api_key = api_key
        self.title = None
        self.url = None

        if self.api_key is None:
            self.api_key = os.getenv('YT_API_KEY')

            if self.api_key is None:
                raise EnvironmentError("API ключ YouTube не найден в переменных окружения.")

    def get_playlist_info(self):
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        playlist_data = youtube.playlists().list(part='snippet', id=self.playlist_id).execute()
        pprint.pprint(playlist_data)
        print(playlist_data)

        self.title = playlist_data['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

        print(self.title)
        print(self.url)

        # Проверка названия плейлиста
        assert self.title == "Moscow Python Meetup №81"
        # Проверка URL плейлиста
        assert self.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

        self.print_playlist_info()

    @property
    def total_duration(self):
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        playlist_items = []
        next_page_token = None

        while True:
            pl_request = youtube.playlistItems().list(part='contentDetails', playlistId=self.playlist_id,
                                                      maxResults=50, pageToken=next_page_token)
            pl_response = pl_request.execute()

            playlist_items += pl_response['items']
            next_page_token = pl_response.get('nextPageToken')

            if not next_page_token:
                break

        total_duration = timedelta()

        for item in playlist_items:
            video_duration = item['contentDetails']['duration']
            duration = timedelta()
            if 'H' in video_duration:
                duration += timedelta(hours=int(video_duration.split('H')[0]))
                video_duration = video_duration.split('H')[1]
            if 'M' in video_duration:
                duration += timedelta(minutes=int(video_duration.split('M')[0]))
                video_duration = video_duration.split('M')[1]
            if 'S' in video_duration:
                duration += timedelta(seconds=int(video_duration.split('S')[0]))
            total_duration += duration

        return total_duration

    def show_best_video(self):
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        playlist_items = []
        next_page_token = None

        while True:
            pl_request = youtube.playlistItems().list(part='snippet', playlistId=self.playlist_id,
                                                      maxResults=50, pageToken=next_page_token)
            pl_response = pl_request.execute()

            playlist_items += pl_response['items']
            next_page_token = pl_response.get('nextPageToken')

            if not next_page_token:
                break

        videos = []

        for item in playlist_items:
            video_info = item['snippet']['resourceId']['videoId']
            videos.append(video_info)

        video_info = []

        for video in videos:
            video_request = youtube.videos().list(part='statistics', id=video)
            video_response = video_request.execute()
            video_info.append(video_response['items'][0])
        video_info.sort(key=lambda x: int(x['statistics']['likeCount']), reverse=True)

        best_video_id = video_info[0]['id']
        best_video_url = f"https://youtu.be/{best_video_id}"

        return best_video_url

    def print_playlist_info(self):
        print(f"Название плейлиста: {self.title}")
        print(f"Ссылка на плейлист: {self.url}")
        print(f"Общая продолжительность: {self.total_duration}")
