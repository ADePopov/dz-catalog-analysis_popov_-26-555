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
result_ar = average_rating(movies)
#print(result_ar)


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

    #нахождение среднего по годам выхода фильма
    for i in year_movies:
        avg_year += i
    avg_year = math.ceil(avg_year/counts)
    
    #нахождение фильма с минимальной давностью выхода
    for i in year_movies:
        if min_year < i:
            min_year = i

    #нахождение фильма с максимальной давностью выхода
    for i in year_movies:
        if max_year > i:
            max_year = i

    return max_year, min_year, avg_year
result_cas = catalog_age_stats(movies, current_year=2026)
#print(result_cas)


def duration_in_hours(minutes: int) -> str:
    """
    Функция duration_in_hours(minutes) переводит минуты в формат "2ч 35м", 
    используя целочисленное деление и остаток от деления.
    """
    hour = minutes // 60
    minute = minutes % 60
    return f"{hour}ч {minute}м"
result_din = duration_in_hours(660)
#print(result_din)


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
result_rt = rating_tier(0.1)
#print(result_rt)


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
result_dl = decade_label(2230)
#print(result_dl)


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
result_clm = count_long_movies(movies)
#print(result_clm) 

"""
3.Напишите функцию format_report_line(movie), 
возвращающую единую строку с описанием фильма.
Пример результата

format_report_line(movies[7])
# '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi' 
Требования
normalize_title нельзя реализовывать через str.title().
make_slug использует .lower() и .replace().
format_report_line обязательно собирается через f-строку и вызывает duration_in_hours из этапа 1.
Жанры в строке отчета отсортированы по алфавиту.
Подсказка
Срез word[1:] — это «все, кроме первого символа»; вместе с word[0].upper() он и дает смену регистра первой буквы вручную.
"""

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
result_nt = normalize_title("silent hours")
print(result_nt)

def make_slug(title: str) -> str:
    """
    функция make_slug(title), превращает 
    нормализованное название 
    в «слаг» вида the-quiet-algorithm 
    """
    result = title.lower().replace(' ', '-')
    return result  
result_ms = make_slug("Silent Hours")
print(result_ms)

def format_report_line(movie):
    title = movie.get('title')
    year = movie.get('year')
    rating = movie.get('rating')
    duration = duration_in_hours(movie.get('duration_min'))
    genres = str(movie.get('genres'))
    f = f'{title} ({year}) — {rating}/10, {duration}, жанры: {genres}'
    return f
films = format_report_line(movies[1])
print(films)