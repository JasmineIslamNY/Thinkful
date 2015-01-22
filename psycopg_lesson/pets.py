import csv
import psycopg2
 
def csv_to_dictionary(csv_file):
    """ Convert csv file to dictionary"""
    dictionary = csv.DictReader(csv_file, delimiter=',')
    return dictionary

def make_into_title(word):
    word = word.title()
    return word
 
def remove_whitespace(word):
    word = word.strip()
    return word

def make_upper(word):
    word = word.upper()
    return word

def clean_up_dictlist(listtoclean):
    for line in listtoclean:
        line["Name"] = remove_whitespace(line["Name"])
        line["Name"] = make_into_title(line["Name"])
        line["breed name"] = remove_whitespace(line["breed name"])
        line["breed name"] = make_into_title(line["breed name"])
        line["species name"] = remove_whitespace(line["species name"])
        line["species name"] = make_into_title(line["species name"])
        line["shelter name"] = make_upper(line["shelter name"])
    return listtoclean
     
def print_dictionary(dictlist):
    for line in dictlist:
        print(line["Name"]),
        print(line["age"]),
        print(line["breed name"]),
        print(line["species name"]),
        print(line["shelter name"]),
        print(line["adopted"])      
     
def update_db():
    pass     
     
def load_db(payload):
    try:
        conn=psycopg2.connect("dbname='pets' user='action' password='731Lexington'")
        print "I connected"
    except:
        print "I am unable to connect to the database."
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * from species""")
    except:
        print "I can't SELECT from bar"
    
    rows = cur.fetchall()
    for row in rows:
        print "   ", row
    
if __name__ == "__main__":
    dictlist = []
    with open("pets.csv") as f:
        csvdict = csv_to_dictionary(f)
        for line in csvdict:
            dictlist.append(line)
    dictlist = clean_up_dictlist(dictlist)
    # print_dictionary(dictlist)
    load_db(dictlist)
    update_db()