from flask import Flask, render_template, request

tags_list = ["новичку", "лекции", "кино", "уроки"]

videos = {
    0: {"title": "Школа сноуборда. Урок 5 - подъемник и катание на склоне", "url": "bnUJW41aJOM",
        "tags": ["новичку", "уроки"], "playlist": 2},
    1: {"title": "Школа сноуборда. Урок 4 - Первые шаги на склоне", "url": "-D7rJG5MBok",
        "tags": ["новичку", "уроки"], "playlist": 2},
    2: {"title": "Школа сноуборда. Урок 6 - повороты с перекантовкой", "url": "R7axkU3NgkA",
        "tags": ["новичку", "уроки"], "playlist": 2},
    3: {"title": "Бюджет поездки на горнолыжный курорт. Почему время дороже денег?", "url": "TrSvHNkyEsA",
        "tags": ["лекции"], "playlist": 0},
    4: {"title": "Школа сноуборда. Урок 7 - базовые элементы фристайла", "url": "GSQ4iG6t-Fs",
        "tags": ["новичку", "уроки"], "playlist": 2},
    5: {"title": "SHREDTOPIA - FULL MOVIE", "url": "FNyCrnsMlDE",
        "tags": ["кино"], "playlist": 1},
    6: {"title": "Freeriding The Steep Mountains Of Chamonix | Frozen Mind FULL SNOWBOARD/FREESKI FILM", "url": "axNnKy-jfWw",
        "tags": ["кино"], "playlist": 1},
    7: {"title": "Физическая подготовка перед горнолыжным сезоном", "url": "oejmKiGtXYk",
        "tags": ["лекции"], "playlist": 0},
    8: {"title": "Как выбрать термобельё", "url": "f9RyDetowjs",
        "tags": [], "playlist": 3},
    9: {"title": "KORUA Shapes - YEARNING FOR TURNING Vol. 6 - Carve Oddity", "url": "Pn-VV8JMgiM",
        "tags": ["кино"], "playlist": 1}, }

playlists = {
    0: {"title": 'Лекции', "videos": [3, 7], "img": r"\static\images\4.jpg",
        "description": "Теория, которая пригодится каждому сноубордисту 📚"},
    1: {"title": "Кино про сноубординг", "videos": [5, 6, 9], "img": r"\static\images\2.jpg",
        "description": "Лучшие фильмы и клипы, посвященные сноубордингу 🤘"},
    2: {"title": "Уроки для начинающих", "videos": [0, 1, 2, 4], "img": r"\static\images\1.jpg",
        "description": "Подборка уроков, которые помогут вам встать на доску 🏂"},
    3: {"title": "Обзоры экиперовки", "videos": [8], "img": r"\static\images\3.jpg",
        "description": "Экиперовка - важная составляющая хорошей каталки! ⚙"},}

app = Flask(__name__)


@app.route('/')
def main():
    """Главная страница. Реализован поиск, выведен список плейлистов"""
    search_word = request.args.get('q')
    return render_template('main.html', playlists=playlists, tags=tags_list, search_word=search_word)


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@app.route('/playlist/<playlist_id>/<video_id>')
def playlist_item(playlist_id, video_id):
    """Вывод информации о плейлисте, списка видео в нем и текущего ролика из этого плейлиста"""
    videos_list = playlists.get(int(playlist_id)).get('videos')  # Сохранил в переменную для оптимизации
    # Если переданный номер видео занимает последнюю позицию в плейлисте
    # то по кнопке будет переход на первое видео
    if videos_list.index(int(video_id))+1 == len(videos_list):
        next_video = videos_list[0]
    # Иначе кнопка примет ссылку на следующий ролик в плейлисте
    else:
        next_video = videos_list[videos_list.index(int(video_id))+1]
    return render_template('playlist.html', playlist=playlists.get(int(playlist_id)), videos=videos,
                           video=videos.get(int(video_id)), playlist_id=playlist_id, video_id=video_id,
                           next_video=next_video)


@app.route('/search')
def search():
    """ Поиск - ищет в названии видео или в тегах к нему"""
    search_word = request.args.get('q')
    search_results = {}

    if search_word:
        for video_id, video in videos.items():

            if search_word.lower() in videos.get(video_id)['title'].lower() or search_word.lower() in videos.get(video_id)['tags']:
                search_results.update({video_id: video})

    return render_template('search.html', search_word=search_word, tags=tags_list, search_results=search_results)


app.run('0.0.0.0', 8888)