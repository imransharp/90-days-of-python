fav_movies = {}

while True:
    name = input("Enter your name (or type 'exit' to stop): ")
    if name.lower() == 'exit':
        break  # Stop the loop if user types 'exit'
    
    movie = input(f"Hi {name}, what's your favorite movie? ")
    # If the name already exists, append the new movie
    if name in fav_movies:
        fav_movies[name].append(movie)
    else:
        fav_movies[name] = [movie]  # Store movie in a list

print("\n📌 Favorite Movies List:")
for name, movie in fav_movies.items():
    print(f"{name} loves {movie}.")
