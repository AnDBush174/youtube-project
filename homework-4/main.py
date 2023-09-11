# main.py
from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса с реальными данными
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
    video2 = PLVideo(
        '4fObz_qw9u4',
        'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
    )
    print(f"Название видео: {video1}")
    print(f"Ссылка на видео: {video1.link}")
    print(f"Количество просмотров: {video1.views}")
    print(f"Количество лайков: {video1.likes}")
    print()
    print(f"Название видео: {video2}")
    print(f"Ссылка на видео: {video2.link}")
    print(f"Количество просмотров: {video2.views}")
    print(f"Количество лайков: {video2.likes}")
    print(f"ID плейлиста: {video2.playlist_id}")
