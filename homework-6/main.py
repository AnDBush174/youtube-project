from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    if broken_video.title is None:
        print("Тест пройден: title is None")
    if broken_video.like_count is None:
        print("Тест пройден: like_count is None")
