from imdb import IMDb

def get_movie_rating(movie_name):
    ia = IMDb()
    movies = ia.search_movie(movie_name)
    if not movies:
        return "Movie Not Found"
    movie = movies[0]
    ia.update(movie)
    rating = movie.get("rating")
    if rating:
        return f"The IMDb rating of '{movie['title']}' is: {rating}"
    else:
        return "No IMDb rating found for this movie."


movie_name = input("Enter the movie name: ")
print(get_movie_rating(movie_name))