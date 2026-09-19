# a)Store the total number of games in the dataset
total_games = len(video_game_sales)
print(total_games) 

# b)Calculate the average global sales across all 20 games
total_sales = sum(game[GLOBAL_SALES] for game in video_game_sales)
avg_global_sales = total_sales / total_games
print(f'The average global sales across all games is {avg_global_sales} million USD.')

# c) Calculate what percentage of the total global sales Wii Sports represents
wii_sports = video_game_sales[0][GLOBAL_SALES]
top_game_share = (wii_sports / total_sales) * 100
print(f'Wii Sports represents {top_game_share}% of the total global sales.') # write your code here
