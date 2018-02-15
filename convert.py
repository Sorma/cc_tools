import cc_dat_utils, cc_json_utils, test_data
import test_json_utils
import json
'''
#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data
FILE = "data/pfgd_test.dat"
result_data = cc_dat_utils.make_cc_data_from_dat(FILE)
print (result_data)

text_file = open('data/pfgd_text.txt', 'w')
text_file.write(str(result_data))
text_file.close()


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
json_data = json.load(open(input_json_file))
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
game_library = test_json_utils.make_game_library_from_json(json_data)
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
print (game_library)

### End Add Code Here ###
'''

#Part 3
#Load your custom JSON file
input_level_json_file = "data/jiajunl2_cc1.json"
output_level_dat_file = "data/jiajunl2_cc1.dat"
with open(input_level_json_file, 'r') as json_file, open(output_level_dat_file, 'w') as dat_file:
    json_level_data = json.load(json_file)
    #Convert JSON data to cc_data
    cc_data = cc_json_utils.make_cc_data_from_json(json_level_data)
    #Save converted data to DAT file
    print(cc_data.levels[0])
    cc_dat_utils.write_cc_data_to_dat(cc_data, output_level_dat_file)
