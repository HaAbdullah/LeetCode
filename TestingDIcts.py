movies = {"Harry Potter": 1, "Stuart Little": 3, "Tenet": 2, "Oppenheimer": 10}
sorted(movies)
for movie in movies: 
    print(movie, movies[movie])

print(movies["Harry Potter"])
# So basically, a "movie" variable in a dictionary of movies is just the movie name, not the name + it's number