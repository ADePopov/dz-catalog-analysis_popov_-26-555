import math
from collections.abc import Iterator

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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
    for movie in movies:
        rating += movie.get('rating')
        counts += 1
    mean = round(rating/counts,1)
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
    year_movies = []
    for movie in movies:
        year_movies.append(movie.get('year'))

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
    ages = [current_year - movie["year"] for movie in movies]
    avg_year = math.ceil(sum(ages) / len(ages))

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
    elif rating >= 7 and rating < 9:
        return 'хорошо'
    elif rating >= 5 and rating < 7:
        return 'средне'
    return 'слабо' if rating < 5 else 'pass'



def decade_label(year: int) -> str:
    """
    функция decade_label(year), 
    через оператор match возвращает метку 
    "новые" (после 2020), "недавние" (2015–2020) или "старые" (раньше 2015).
    """
    match year:
        case _ if year > 2020: 
            return 'новые'
        case _ if 2015 <= year <= 2020:
            return 'недавние'
        case _ if year < 2015:
            return 'старые'


def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    """
    Функция count_long_movies(movies, threshold=120), 
    которая через for с накопительной переменной 
    считает количество фильмов длиннее threshold минут.
    """
    counts_film = 0
    for movie in movies:
        if movie.get('duration_min') > threshold:
            counts_film += 1
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


def format_report_line(movie: dict) -> str:
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



def titles_sorted_by_rating(movies: list[dict]) -> list:
    """
    Функция titles_sorted_by_rating(movies), 
    возвращающую список названий фильмов, 
    отсортированных по убыванию рейтинга.
    """
    sorted_films = sorted(movies, key=lambda movies: movies.get('rating'), reverse=True)
    movie_titles = [movie['title'] for movie in sorted_films]
    return movie_titles


def top_n_by_rating(movies: list[dict], n: int = 3) -> list[tuple]:
    """
    Функция top_n_by_rating(movies, n=3), 
    возвращающая список из n кортежей (title, rating) — топ по рейтингу.
    """
    sorted_films = sorted(movies, key=lambda movies: movies.get('rating'), reverse=True)
    counts = 0
    result_list = []
    while counts < n:
        result_list.append((sorted_films[counts].get('title'), 
                            sorted_films[counts].get('rating')))
        counts += 1
    return result_list



def count_by_genre(movies: list[dict]) -> dict[str, int]:
    """
    Функция count_by_genre(movies), 
    возвращающает словарь {жанр: количество фильмов}
    """
    final = {}
    for movie in movies:
        for genre in movie.get("genres", set()):
            final[genre] = final.get(genre, 0) + 1
    return dict(sorted(final.items(), key=lambda x: -x[1]))



def actor_filmography(movies:list[dict]) -> dict:
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


def all_genres(movies: list[dict]) -> set:
    """
    функция all_genres(movies), 
    возвращающую множество всех уникальных жанров каталога
    """
    empty = set()
    for movie in movies:
        empty = empty | movie.get('genres')
    return empty



def common_actors(movie1: dict, movie2: dict) -> set:
    """
    функция common_actors(movie1, movie2), 
    возвращающая множество актеров, снимавшихся в обоих фильмах.
    """
    return set(movie1.get("actors", [])) & set(movie2.get("actors", []))


def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set[str]:
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


def iter_high_rated(movies: list, min_rating: float = 8.0) -> Iterator[dict]:
    """
    функция-генератор iter_high_rated(movies, min_rating=8.0), 
    которая через yield лениво отдает фильмы 
    с рейтингом не ниже min_rating.
    """
    for movie in movies:
        if movie.get('rating', 0.0) >= min_rating:
            yield movie




def build_report(movies: list[dict]) -> str:
    line = []

    avg_rating = average_rating(movies)
    avg_age = catalog_age_stats(movies)

    line.append("ОТЧЕТ ПО КАТАЛОГУ")
    line.append(f"Средний рейтинг: {avg_rating}")
    line.append(f"Средний возраст фильмов: {avg_age[2]} лет")
    line.append("")

    line.append("Топ-3 фильма:")
    top = top_n_by_rating(movies)
    for title, rating in top:
        for movie in movies:
            if movie.get('title') == title:
                line.append("  " + format_report_line(movie))
                break
    line.append("")

    line.append("Фильмов по жанрам:")
    genre_c = count_by_genre(movies)
    for genre, c in genre_c.items():
        line.append(f"  {genre} — {c}")
    line.append("")

    k = all_genres(movies)
    line.append(f"Все жанры каталога: {', '.join(sorted(k))}")

    return "\n".join(line)

if __name__ == "__main__":

    # С помощью for и continue выведите на экран (print) 
    # названия всех фильмов, которые НЕ относятся к жанру "comedy".
    for movie in movies:
        if 'comedy' not in movie.get('genres',[]):
            print(movie.get('title',[]))
        else:
            continue

    # С помощью while и break найдите первый по порядку в списке фильм 
    # с рейтингом выше 9.0; если такого фильма нет, 
    # цикл должен завершиться веткой else с сообщением "Шедевров не найдено".
    counts = 0
    while counts < len(movies):
        if movies[counts].get('rating') > 9.0:
            print(movies[counts].get('title'))
            break
        counts += 1
    else:
        print('Шедевров не найдено')

    avg_rate = average_rating(movies)

    title_rating = {m["title"]: m["rating"] 
                    for m in movies 
                    if m.get("rating", 0) > avg_rate}

    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    
    total = sum(m["duration_min"] for m in movies if m["rating"] > 7)
    print(total)

    print(build_report(movies))






