"""
Methods for encoding and decoding Chip's Challenge (CC) data to and from customized JSON files
"""
import json
import cc_data


def make_cc_data_from_json(json_data):
    """
    Reads data from a JSON file and constructs a CCDataFile object out of it
    This code assumes a valid DAT file and does not error check for invalid data
    params:
        json_file (string): file name of the JSON file to read
    returns:
        A CCDataFile object constructed with the data from the given file
    """
    data = cc_data.CCDataFile()
    # is header bytes a thing here?
    # get number of levels
    num_levels = len(json_data)
    # make levels and add to level pack
    for i in range(num_levels):
        level = make_level_from_json(json_data[i])
        data.append(level)
    return data

def make_level_from_json(level_data):
    """
    Reads data from a JSON file and constructs a CCLevel object
    params:
        json_file (string): file name of the JSON file to read
    returns:
        A CCLevel object constructed with the data from the given file
    """
    level = cc_data.CCLevel()
    # level.num_bytes = ?
    level.level_number = level_data["level number"]
    level.time = level_data["time"]
    level.num_chips = level_data["chip count"]