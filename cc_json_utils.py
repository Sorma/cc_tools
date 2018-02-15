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
        data.levels.append(level)
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
    level.upper_layer = level_data["upper layer"]
    level.lower_layer = level_data["lower layer"]
    # optional fields
    for json_field in level_data["fields"]:
        # determine which field to create based on type number.
        cc_field = make_field_from_json(json_field["type"], json_field["value"])
        # add the optional field into the field list
        level.add_field(cc_field)
    return level

def make_field_from_json(type, value):
    '''
    Reads data from a field data and build different types of fields according to type number.
    params:
        type (int): the type number specified in json file
        value: the value of the field
    returns:
        A specific kind of CCField object constructed with the data from the given file
    '''
    if type == 3:
        return cc_data.CCMapTitleField(value)
    elif type == 6:
        return cc_data.CCPasswordField(value)
    elif type == 7:
        return cc_data.CCMapHintField(value)
    elif type == 10:
        coordinate_list = []
        for i in value:
            coordinate_list.append(cc_data.CCCoordinate(i[0], i[1]))
        return cc_data.CCMonsterMovementField(coordinate_list)
