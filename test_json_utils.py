import test_data
json_file = 'data/test_data.json'

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data

def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    for entry in json_data:
        title = entry["title"]
        year = entry["Year"]
        platform = test_data.Platform(entry["platform"]["name"], entry["platform"]["launch year"])
        game = test_data.Game(title, platform, year)
        game_library.add_game(game)
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library
    return game_library
