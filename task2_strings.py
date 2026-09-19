messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

# write your code here
# a) Extract the name of the 5h game and print just 'Pokemon'
game_name = video_game_sales[4][1]
print(game_name[:7])

# b) Clean whitespace and lowercase each name
messy_name = ['Wii sports', 'TETRIS', 'mario kart WII']
for name in messy_name:
    print(name.strip().lower())

# c) Use an f-string to print a formatted summary of the #1 game
game = video_game_sales[0]
print(f'#{game[0]} Best Seller: {game[1]} ({game[3]}) - ${game[9]}M global sales')
