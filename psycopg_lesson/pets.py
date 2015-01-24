import csv
import psycopg2
import sys
 
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

def empty_to_none(word):
    if word == "":
        word = None
    return word

def clean_up_dictlist(listtoclean):
    """ This method cleans up the csv file for db entry, it: 
        removes empty spaces - all fields, 
        make all letter upper case - Shelter Name,
        capitalizes the first letter of each word - Name, Breed Name, Species Name, 
        and then sets empty variables to None, which is the Python null """
    for line in listtoclean:
        line["Name"] = empty_to_none(make_into_title(remove_whitespace(line["Name"])))
        line["breed_name"] = empty_to_none(make_into_title(remove_whitespace(line["breed_name"])))
        line["species_name"] = empty_to_none(make_into_title(remove_whitespace(line["species_name"])))
        line["shelter_name"] = empty_to_none(make_upper(remove_whitespace(line["shelter_name"])))
        line["age"] = empty_to_none(remove_whitespace(line["age"]))
        line["adopted"] = empty_to_none(remove_whitespace(line["adopted"]))                                     
    return listtoclean
     
def print_dictionary(dictlist):
    for line in dictlist:
        print(line["Name"]),
        print(line["age"]),
        print(line["breed_name"]),
        print(line["species_name"]),
        print(line["shelter_name"]),
        print(line["adopted"])      
 
def load_db(payload):
    payload = tuple(payload)
    
    try:
        conn=psycopg2.connect("dbname='pets' user='postgres' password='731Lexington'")
        #print "I connected"
    except:
        print "I am unable to connect to the database."
    cur = conn.cursor()
    
    for line in payload:
        if line["species_name"] == None:
            #print(line["species_name"])
            continue
        
        cur.execute("""INSERT INTO species (name) SELECT %(species_name)s WHERE NOT EXISTS (SELECT 1 FROM species WHERE name = %(species_name)s)""", line)
        #print(line["species_name"])
        
    conn.commit()    
    
    for line in payload:
        if line["shelter_name"] == None:
            #print(line["shelter_name"])
            continue
        
        cur.execute("INSERT INTO shelter (name) SELECT %(shelter_name)s WHERE NOT EXISTS (SELECT 1 FROM shelter WHERE name = %(shelter_name)s)", line)
        #print(line["shelter_name"])
        
    conn.commit()       
    
    
    for line in payload:
        if line["breed_name"] == None:
            #print(line["breed_name"])
            continue
        
        cur.execute("INSERT INTO breed (name, species_id) SELECT %(breed_name)s, (SELECT id FROM species WHERE name = %(species_name)s) WHERE NOT EXISTS (SELECT 1 FROM breed WHERE name = %(breed_name)s and species_id in (SELECT id FROM species WHERE name = %(species_name)s))", line)
        #print(line["breed_name"])
        
    conn.commit()       
    
    for line in payload:
        if line["Name"] == None:
            #print(line["Name"])
            continue
        
        cur.execute("INSERT INTO pet (name, age, shelter_id, breed_id, adopted) VALUES (%(Name)s, %(age)s, (select id from shelter where name = %(shelter_name)s), (select id from breed where species_id in (select id from species where name = %(species_name)s) and name = %(breed_name)s), bool(%(adopted)s))", line)
        #print(line["breed_name"])
                
    conn.commit()
          

    cur.execute("""SELECT * from species""")               
    rows = cur.fetchall()
    for row in rows:
        print "   ", row
        
    cur.execute("""SELECT * from shelter""")               
    rows = cur.fetchall()
    for row in rows:
        print "   ", row        

    cur.execute("""SELECT * from breed""")               
    rows = cur.fetchall()
    for row in rows:
        print "   ", row

    cur.execute("""SELECT * from pet""")              
    rows = cur.fetchall()
    print("   ID | Name | Age | Adopted | Dead | Breed ID | Shelter ID")
    for row in rows:
        print "   ", row
    
if __name__ == "__main__":
    dictlist = []
    with open("pets.csv") as f:
        csvdict = csv_to_dictionary(f)
        for line in csvdict:
            dictlist.append(line)
    dictlist = clean_up_dictlist(dictlist)
    print_dictionary(dictlist)
    load_db(dictlist)