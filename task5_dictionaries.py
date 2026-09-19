# write your code here

# a) Total global sales by genre
sales_by_genre = {}
for game in video_game_sales:
    genre = game[4]
    sales = float(game[-1])
    sales_by_genre[genre] = sales_by_genre.get(genre, 0.0) + sales

print(sales_by_genre)

# b) Number of games per publisher
games_per_publisher = {}
for game in video_game_sales:
    publisher = game[5]
    games_per_publisher[publisher] = games_per_publisher.get(publisher, 0) + 1

print(games_per_publisher)

# c) Details of the #1 ranked game
# Create the dictionary for the #1 ranked game (Wii Sports from the common video game sales dataset)
top_game = {
    'name': 'Wii Sports',
    'year': 2006,
    'genre': 'Sports',
    'publisher': 'Nintendo',
    'global_sales': 82.74
}

# Print each key-value pair on its own line using .items()
for key, value in top_game.items():
    print(f"{key}: {value}")
