class Movies(object):
    movies = []

    def add_movie(self, title):
        self.movies.append(title)


import ipdb; ipdb. set_trace()

a = Movies()
a.add_movie('The Thing')
a.add_movie('Nosferatu')

b = Movies()
b.add_movie('Toy Story')

print(a.movies)
print(b.movies)
