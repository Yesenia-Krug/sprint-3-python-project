# write your code here
# a) Create a list of game names using a loop
game_names = []
for game in video_game_sales:
    game_names.append(game[NAME])
print(game_names)

# b) Append the new game and print the updated length
new_game = [21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18]
video_game_sales.append(new_game)
print(len(video_game_sales))

# c) Create a tuple with dataset metadata and print it
dataset_info = (len(video_game_sales), 10, 'Video Game Sales')
print(dataset_info)

# A tuple is more appropriate than a list for this data because is a metadata
# Like the name of the dataset and the number of colums is fix. 
# Tuples are immutable, which prevents this data from being accidentally changed. 
