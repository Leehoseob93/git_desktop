from collections import defaultdict

movies=[
    ('Inception', 'SF'),
    ('Interstellar', 'SF'),
    ('Titanic', 'Drama'),
    ('The Drak knight', 'Actiton'),
    ('Joker', 'Drama')
]

moviess = defaultdict(list)
for title, genre in movies:
    moviess[genre].append(title)

for genre, title in moviess.items():
    print(f'{genre} : {title}')