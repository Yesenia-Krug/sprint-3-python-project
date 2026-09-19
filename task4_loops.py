# write your code here
# a) Games with over 23M global sales
for game in video_game_sales:
    if float(game[9]) > 25:
        print(f"Name: {game[0]}, Global Sales: {game[9]}M")

# b) County of games released before 2000
pre_2000_count = 0
for game in video_game_sales:
    if str(game[3]).isdigit() and int(game[3]) < 2000:
        pre_2000_count += 1
print(f"Games released before 2000: {pre_2000_count}")

# c) Total NA vs JP sales comparison
total_na_sales = 0.0
total_jp_sales = 0.0

for game in video_game_sales:
    total_na_sales += float(game[6])
    total_jp_sales += float(game[8])

print(f"Total NA Sales: {total_na_sales:.2f}M")
print(f"Total Japan Sales: {total_jp_sales:.2f}M")

if total_na_sales > total_jp_sales:
    print("North America had higher sales.")
elif total_jp_sales > total_na_sales:
    print("Japan had higher sales.")
else:
    print("Both regions had equal sales.")

# d) Nintendo games list and count
nintendo_games = []
for game in video_game_sales:
    if game[5] == 'Nintendo':
        nintendo_games.append(game[1])

print("Nintendo Games:", nintendo_games)
print(f"Total Nintendo games: {len(nintendo_games)}")
