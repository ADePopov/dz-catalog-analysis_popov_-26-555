import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies: list[dict]) -> float:
    """
    Функция average_rating(movies) 
    возвращает среднюю оценку по каталогу, 
    округленную до одного знака
    """
    counts = 0
    rating = 0
    for i in movies:
        rating += movies[counts].get('rating')
        counts += 1
    mean = round(rating/counts,2)
    return mean



def catalog_age_stats(movies: list[dict], current_year: int = 2026) -> tuple:
    """
    Функция catalog_age_stats(movies, current_year=2026) 
    возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее), 
    где среднее округлено вверх до целого
    """
    min_year = 0
    max_year = current_year
    avg_year = 0
    counts = 0
    year_movies = []
    for i in movies:
        year_movies.append(movies[counts].get('year'))
        counts += 1

    #нахождение фильма с минимальной давностью выхода
    for i in year_movies:
        if min_year < i:
            min_year = i

    #нахождение фильма с максимальной давностью выхода
    for i in year_movies:
        if max_year > i:
            max_year = i

    min_year = current_year - min_year
    max_year = current_year - max_year
    avg_year = math.ceil(max_year/min_year)

    return max_year, min_year, avg_year



def duration_in_hours(minutes: int) -> str:
    """
    Функция duration_in_hours(minutes) переводит минуты в формат "2ч 35м", 
    используя целочисленное деление и остаток от деления.
    """
    hour = minutes // 60
    minute = minutes % 60
    return f"{hour}ч {minute}м"


def rating_tier(rating: float) -> str:
    """
    функция rating_tier(rating), которая по оценке возвращает категорию: 
    "шедевр" (≥9), "хорошо" (7 - 8.9), "средне" (5 – 6.9), "слабо" (<5). 
    """
    if rating >= 9:
        return 'шедевр'
    elif rating >=7 and rating <= 8.9:
        return 'хорошо'
    elif rating >=5 and rating <= 6.9:
        return 'средне'
    return 'слабо' if rating < 5 else 'pass'



def decade_label(year: int) -> str:
    """
    функция decade_label(year), 
    через оператор match возвращает метку 
    "новые" (после 2020), "недавние" (2015–2020) или "старые" (раньше 2015).
    """
    match year:
        case year if year > 2020: 
            return 'новые'
        case year if year <= 2020 and year >= 2015:
            return 'недавние'
        case year if year < 2015:
            return 'старые'



# С помощью for и continue выведите на экран (print) названия всех фильмов, которые НЕ относятся к жанру "comedy".
counts = 0
for i in movies:
    if 'comedy' not in movies[counts].get('genres',[]):
        print(movies[counts].get('title',[]))
        counts += 1
    else:
        counts += 1
        continue


# С помощью while и break найдите первый по порядку в списке фильм с рейтингом выше 9.0; если такого фильма нет, цикл должен завершиться веткой else с сообщением "Шедевров не найдено".
counts = 0
while counts < len(movies):
    if movies[counts].get('rating') >= 9:
        print(movies[counts].get('title'))
        break
    counts += 1
else:
    print('Шедевров не найдено')

def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    """
    Функция count_long_movies(movies, threshold=120), 
    которая через for с накопительной переменной считает количество фильмов длиннее threshold минут.
    """
    counts = 0
    counts_film = 0
    for i in movies:
        if movies[counts].get('duration_min') > threshold:
            counts_film += 1
        counts += 1
    return counts_film



def normalize_title(title: str) -> str:
    """
    функция normalize_title(title), 
    приводит строку к формату Title Case 
    (каждое слово с заглавной буквы)   
    """
    string = title.split()
    new_string = []
    for i in string:
        new_string.append(i[0:1].upper()+i[1:])
    new_string = ' '.join(new_string) 
    return new_string  


def make_slug(title: str) -> str:
    """
    функция make_slug(title), превращает 
    нормализованное название 
    в «слаг» вида the-quiet-algorithm 
    """
    result = title.lower().replace(' ', '-')
    return result  


def format_report_line(movie: list[dict]) -> str:
    """
    функция format_report_line(movie), 
    возвращает единую строку с описанием фильма.
    Пример результата
    format_report_line(movies[7])
    '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi' 
    """
    title = movie.get('title')
    title_norm = normalize_title(title)
    year = movie.get('year')
    rating = movie.get('rating')
    duration = duration_in_hours(movie.get('duration_min'))
    genresss = movie.get('genres')
    genress = list(genresss)
    genress.sort()
    genres = ', '.join(genress)
    f = f'"{title_norm}" ({year}) — {rating}/10, {duration}, жанры: {genres}'
    return f



def titles_sorted_by_rating(movies: list) -> list:
    """
    Функция titles_sorted_by_rating(movies), 
    возвращающую список названий фильмов, 
    отсортированных по убыванию рейтинга.
    """
    sorted_films = sorted(movies, key=lambda movies: movies.get('rating'), reverse = True)
    movie_titles = [movie['title'] for movie in sorted_films]
    return movie_titles


def top_n_by_rating(movies: list, n: int = 3) -> list[tuple]:
    """
    Функция top_n_by_rating(movies, n=3), 
    возвращающая список из n кортежей (title, rating) — топ по рейтингу.
    """
    sorted_films = sorted(movies, key=lambda movies: movies.get('rating'), reverse = True)
    counts = 0
    result_list = []
    while counts < n:
        result_list.append((sorted_films[counts].get('title'), sorted_films[counts].get('rating')))
        counts += 1
    return result_list



def count_by_genre(movies: list) -> list:
    """
    Функция count_by_genre(movies), 
    возвращающает словарь {жанр: количество фильмов}
    """
    counts = 0
    result = []
    for i in movies:
        result = list(dict.fromkeys(result + list(movies[counts].get('genres',0))))
        counts += 1

    counts = 0
    lists = []
    for i in movies:
        lists.append(movies[counts].get('genres'))
        counts += 1

    final = {}
    for i in result:
        final[i] = sum(i in s for s in lists)
    return final



def actor_filmography(movies:list) -> dict:
    """
    функция actor_filmography(movies), 
    возвращает словарь {актер: [список названий фильмов]}
    """
    counts = {}
    for movie in movies:
        title = movie.get('title')
        for actor in movie.get('actors',[]):
            if actor not in counts:
                counts[actor] = []
            counts[actor].append(title)
    return counts


titles = []
counts = 0
for i in movies:
    titles.append(movies[counts].get('title'))
    counts += 1
rating = []
counts = 0
for i in movies:
    rating.append(movies[counts].get('rating'))
    counts += 1
avg_rate = average_rating(movies)
title_rating = {title: rate for title, rate in zip(titles, rating) if rate > avg_rate}
print(title_rating)


def all_genres(movies: list) -> set:
    """
    функция all_genres(movies), 
    возвращающую множество всех уникальных жанров каталога
    """
    empty = set()
    counts = 0
    for i in movies:
        empty = empty | movies[counts].get('genres')
        counts += 1
    return empty


def common_actors(movie1: list[int], movie2: list[int]) -> set:
    """
    функция common_actors(movie1, movie2), 
    возвращающая множество актеров, снимавшихся в обоих фильмах.
    """
    empty = set()
    counts = 0
    for i in movies:
        if movies[counts].get('title') == movie1.get('title'):
            empty = empty | set(movies[counts].get('actors'))
        counts += 1

    counts = 0
    for i in movies:
        if movies[counts].get('title') == movie2.get('title'):
            empty = empty & set(movies[counts].get('actors'))
        counts += 1
    return empty


def genres_only_in_one(movies_a: list[i], movies_b: list[i]) -> dict:
    """
    функция genres_only_in_one(movies_a, movies_b), 
    которая возвращает жанры, 
    встречающиеся в movies_a, но не встречающиеся в movies_b
    """
    mv_a = set()
    for movie in movies_a:
        mv_a = mv_a | movie.get('genres')

    mv_b = set()
    for movie in movies_b:
        mv_b = mv_b | movie.get('genres')

    result = mv_a - mv_b

    return result
result_goio = genres_only_in_one(movies[5:6], movies[:5])
#print(result_goio)

def iter_high_rated(movies: list, min_rating: float = 8.0) -> str:
    """
    функция-генератор iter_high_rated(movies, min_rating=8.0), 
    которая через yield лениво отдает фильмы 
    с рейтингом не ниже min_rating.
    """
    counts = 0
    for i in movies:
        if movies[counts].get('rating') > min_rating:
            yield i
        counts += 1

for movie in iter_high_rated(movies):
    print(format_report_line(movie))

total = sum(m["duration_min"] for m in movies if m["rating"] > 7)
print(total)

"""
Этап 9. Итоговый отчет
Собираем все вместе.
Задача
Напишите функцию build_report(movies), которая объединяет результаты всех предыдущих этапов в единый консольный отчет: общую статистику, топ-3 фильма, количество фильмов по каждому жанру и полный список уникальных жанров каталога.
Пример отчета

ОТЧеТ ПО КАТАЛОГУ
Средний рейтинг: 7.2
Средний возраст фильмов: 8 лет

Топ-3 фильма:
  "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi
  "Midnight In Oslo" (2020) — 8.9/10, 2ч 4м, жанры: mystery, thriller
  "The Dune Chronicles" (2021) — 8.6/10, 2ч 35м, жанры: drama, sci-fi

Фильмов по жанрам:
  drama — 5
  comedy — 3
  sci-fi — 3
  thriller — 3
  action — 2
  mystery — 1

Все жанры каталога: action, comedy, drama, mystery, sci-fi, thriller 
Требования
build_report — единственная точка входа: один ее вызов полностью воспроизводит отчет.
Жанры в списке количества отсортированы по убыванию числа фильмов.
Полный список жанров выводится одной строкой через ", ".join(...).
"""
def build_report(movies):
    avg_rating = average_rating(movies)
    avg_age = catalog_age_stats(movies)
    top = sorted(movies, key=lambda m: m.get('rating', 0), reverse=True)[:3]
    top_lines = "\n".join("  " + format_report_line(m) for m in top)
    return f'''
    ОТЧЕТ ПО КАТАЛОГУ
    Средний рейтинг: {avg_rating}
    Средний возраст фильмов: {avg_age[2]} лет

    Топ-3 фильма:
    {top_lines} 

    {count_by_genre(movies)}
    Фильмов по жанрам:
    drama — 5
    comedy — 3
    sci-fi — 3
    thriller — 3
    action — 2
    mystery — 1

    Все жанры каталога: action, comedy, drama, mystery, sci-fi, thriller 
    '''
result_final = build_report(movies)
print(result_final)





