class Movies(object):
    def __init__(self):
        self.movies = []

    def add_movie(self, title):
        self.movies.append(title)


a = Movies()
a.add_movie('The Thing')
a.add_movie('Nosferatu')

b = Movies()
b.add_movie('Toy Story')

print(a.movies)
print(b.movies)