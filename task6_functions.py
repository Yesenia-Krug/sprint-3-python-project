# write your code here
# a) Calculate total sales (NA + EU + JP)
def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]

# Test on the first game (index 0)
first_game_sales = calculate_total_sales(video_game_sales[0])
print(f"Total NA, EU, and JP sales for the first game: {first_game_sales}")

print("-" * 30)

# b) Filter games by genre
def filter_by_genre(data, genre='Platform'):
    filtered_list = []
    for game in data:
        if game[GENRE] == genre:
            filtered_list.append(game)
    return filtered_list

# Test without specifying a genre (defaults to 'Platform')
platform_games = filter_by_genre(video_game_sales)
print(f"Number of Platform games: {len(platform_games)}")

# Test with specifying a genre ('Sports')
sports_games = filter_by_genre(video_game_sales, 'Sports')
print(f"Number of Sports games: {len(sports_games)}")

print("-" * 30)

# c) Get formatted summary string
def get_summary(game):
    name = game[NAME]
    year = game[YEAR]
    genre = game[GENRE]
    global_sales = game[GLOBAL_SALES]
    return f"{name} ({year}) - {genre} - ${global_sales}M"

# Loop through the dataset and print the summary for every game
for game in video_game_sales:
    print(get_summary(game))
