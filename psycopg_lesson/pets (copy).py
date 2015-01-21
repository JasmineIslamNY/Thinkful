import csv 
#----------------------------------------------------------------------
def csv_to_dictionary(csv_file):
    """ Convert csv file to dictionary"""
    dictionary = csv.DictReader(csv_file, delimiter=',')
    return dictionary
 
def make_into_title(word):
    word = word.title()
    print word
    return word
 
def remove_whitespace(word):
    word = word.strip()
    print word
    return word

def make_upper(word):
    word = word.upper()
    print word
    return word

def clean_dictionary(dict_obj):
    """ Cleans up a dictionary to get it ready for input into database """
    for line in dict_obj:
        line["Name"] = remove_whitespace(line["Name"])
        line["Name"] = make_into_title(line["Name"])
        line["breed name"] = remove_whitespace(line["breed name"])
        line["breed name"] = make_into_title(line["breed name"])
        line["species name"] = remove_whitespace(line["species name"])
        line["species name"] = make_into_title(line["species name"])
        line["shelter name"] = make_upper(line["shelter name"])
        
"""
Why does calling print_dictionary(dictionary) not work???
def print_dictionary(dict_obj):
    """ """Prints dictionary for testing purposes """ """
    d = dict_obj
    for line in d:
            print(line["Name"]),
            print(line["age"]),
            print(line["breed name"]),
            print(line["species name"]),
            print(line["shelter name"]),
            print(line["adopted"])
"""

if __name__ == "__main__":
    with open("pets.csv") as f:
        dictionary = csv_to_dictionary(f)
        dictionary = clean_dictionary(dictionary)
        # print_dictionary(dictionary)
        for line in dictionary:
            print(line["Name"]),
            print(line["age"]),
            print(line["breed name"]),
            print(line["species name"]),
            print(line["shelter name"]),
            print(line["adopted"])