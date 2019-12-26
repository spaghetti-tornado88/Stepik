from flask import Flask, render_template, request

invite_string = """<h1>Привет, это Stepik Snow, портал по видео про сноубординг.</h1>
<h3>Перейдите на /about чтобы посмотреть инфрмацию.</h3>
<h3>Перейдите на /playlists/<№_плейлиста> чтобы посмотреть плейлисты. </h3> 
<h3>Перейдите на /videos/<№_видео> чтобы посмотреть видео.</h3>
<h3>Перейдите на /find/<поисковое_слово> или /search/<поисковое слово>, чтобы выполнить поиск по видео.</h3>
<h3>Перейдите на /tags/<тег>, чтобы выполнить поиск по видео.</h3>

<h1>Видео:</h1>
"""

tags_list = ["новичку", "лекции", "кино", "уроки"]

#https://img.youtube.com/vi/GSQ4iG6t-Fs/hqdefault.jpg

videos = {
    0: {"title": "Школа сноуборда. Урок 5 - подъемник и катание на склоне", "url": "bnUJW41aJOM",
        "tags": ["новичку", "уроки"]},
    1: {"title": "Школа сноуборда. Урок 4 - Первые шаги на склоне", "url": "-D7rJG5MBok",
        "tags": ["новичку", "уроки"]},
    2: {"title": "Школа сноуборда. Урок 6 - повороты с перекантовкой", "url": "R7axkU3NgkA",
        "tags": ["новичку", "уроки"]},
    3: {"title": "Бюджет поездки на горнолыжный курорт. Почему время дороже денег?", "url": "TrSvHNkyEsA",
        "tags": ["лекции"]},
    4: {"title": "Школа сноуборда. Урок 7 - базовые элементы фристайла", "url": "GSQ4iG6t-Fs",
        "tags": ["новичку", "уроки"]},
    5: {"title": "SHREDTOPIA - FULL MOVIE", "url": "FNyCrnsMlDE",
        "tags": ["кино"]},
    6: {"title": "Freeriding The Steep Mountains Of Chamonix | Frozen Mind FULL SNOWBOARD/FREESKI FILM", "url": "axNnKy-jfWw",
        "tags": ["кино"]},
    7: {"title": "Физическая подготовка перед горнолыжным сезоном", "url": "oejmKiGtXYk",
        "tags": ["лекции"]},
    8: {"title": "Как выбрать термобельё", "url": "f9RyDetowjs",
        "tags": []},
    9: {"title": "KORUA Shapes - YEARNING FOR TURNING Vol. 6 - Carve Oddity", "url": "Pn-VV8JMgiM",
        "tags": ["кино"]}, }

playlists = {0: {"title": 'Лекции', "videos": [3, 7], "img": r"\static\images\4.jpg"},
             1: {"title": "Кино про сноубординг", "videos": [5, 6, 9], "img": r"\static\images\2.jpg"},
             2: {"title": "Уроки для начинающих", "videos": [0, 1, 2, 4], "img": r"\static\images\1.jpg"},
             3: {"title": "Обзоры экиперовки", "videos": [8], "img": r"\static\images\3.jpg"}, }


def serialize_videos(item_counter, items_dict, item_id):
    """ Сериализация данных о видео. """
    return ' '.join(['<p>', str(item_counter) + '.', items_dict.get(item_id)['title'],
                                       '<br>', 'http://youtu.be/' + items_dict.get(item_id)['url'], '<br>', '</p>'])


app = Flask(__name__)


#  Совсем не знаю HTML, поэтому сверстал как смог :)

@app.route('/')
def main():
    # return_string = invite_string
    # for counter, vid_id in enumerate(videos, 1):
    #     return_string += serialize_videos(counter, videos, vid_id)
    # return_string += "<h1>Плейлисты:</h1>"
    # for counter, playlist_id in enumerate(playlists, 1):
    #     return_string += ' '.join(['<p>', str(counter) + '.', playlists.get(playlist_id)['title'],'[' +
    #                                       str(len(playlists.get(playlist_id)['videos'])),'видео]' '</p>'])
    # return_string += "<h1>Теги:"
    # return_string += ' '.join(tags_list)
    # return(return_string)
    return render_template('main.html', playlists=playlists, tags=tags_list)

@app.route('/about')
def about():
    return render_template('about.html')
    #return "<h1>Stepk Snow - портал видео, посвещенных сноубордингу</h1> Если вы видели снег - сообщите мне!"


@app.errorhandler(404)
def page_not_found(error):
   #return "Страница не найдена"
    return render_template('404.html')


#@app.route('/video/<vid_id>')
#def videos_item(vid_id):
#     vid_id = int(vid_id) - 1
#
#     if vid_id in videos:
#         return serialize_videos(vid_id + 1, videos, vid_id)
#
#     else:
#         return page_not_found(404)
    #return render_template('video.html')



@app.route('/playlist/<playlist_id>/<video_id>')
def playlist_item(playlist_id, video_id):
    # return_string = ''
    # pll_id = int(pll_id) - 1
    #
    # if pll_id in playlists:
    #     for counter, vid_id in enumerate(playlists[pll_id]['videos'], 1):
    #         return_string += serialize_videos(counter, videos, vid_id)
    #     return_string += 'Приятного просмотра!'
    #     return return_string
    #
    # else:
    #     return page_not_found(404)
    return render_template('playlist.html', playlist=playlists.get(int(playlist_id)), videos=videos,
                           video=videos.get(int(video_id)), playlist_id=playlist_id, video_id=video_id)


@app.route('/search')
def search():
    """ Поиск по слову. Ищет в названии видео или в тегах к нему"""
    # return_string = ''
    # for counter, vid_id in enumerate(videos, 1):
    #
    #     if word.lower() in videos.get(vid_id)['title'].lower() or word.lower() in videos.get(vid_id)['tags']:
    #         return_string += serialize_videos(counter, videos, vid_id)
    #
    # if return_string == '':
    #     return_string = 'Таких видео у нас нет!'
    # return return_string
    test = request.args.get('q')
    return render_template('search.html', test=test)

# Подумал над логикой в проекте и реализовал систему тегов
@app.route('/tags/<tag_title>')
def tags(tag_title):
    return_string = ''
    for counter, vid_id in enumerate(videos, 1):

        if tag_title in videos.get(vid_id)['tags']:
            return_string += ' '.join(['<p>', str(counter) + '.', videos.get(vid_id)['title'],
                                       '<br>', 'http://youtu.be/' + videos.get(vid_id)['url'], '<br>', '<p/>'])
    if return_string:
        return return_string
    else:
        return page_not_found(404)


app.run('0.0.0.0', 8888)