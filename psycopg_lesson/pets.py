import csv
#from load_db import load_db
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
        line["breed_name"] = remove_whitespace(line["breed_name"])
        line["breed_name"] = make_into_title(line["breed_name"])
        line["species_name"] = remove_whitespace(line["species_name"])
        line["species_name"] = make_into_title(line["species_name"])
        line["shelter_name"] = make_upper(line["shelter_name"])
        line["shelter_name"] = remove_whitespace(line["shelter_name"])
        line["age"] = remove_whitespace(line["age"])
        line["adopted"] = remove_whitespace(line["adopted"])
    return listtoclean
     
def print_dictionary(dictlist):
    for line in dictlist:
        print(line["Name"]),
        print(line["age"]),
        print(line["breed_name"]),
        print(line["species_name"]),
        print(line["shelter_name"]),
        print(line["adopted"])      
     
def update_db():
    pass     
 
def load_db(payload):
    #print payload
    #payload = tuple(payload)
    #print payload
    
    for line in payload:
      print line
      try:
          conn=psycopg2.connect("dbname='pets' user='action' password='731Lexington'")
          print "I connected"
      except:
          print "I am unable to connect to the database."
      cur = conn.cursor()
      try:
          #cur.execute("""INSERT INTO pet (name, age, breed_id, shelter_id) VALUES ('Titch', 1, 1, 1)""")      
          #cur.execute("INSERT INTO pet (name, age) VALUES (%(Name)s, %(age)s)", line)
          cur.execute("INSERT INTO pet (name, age, shelter_id, breed_id, adopted) VALUES (%(Name)s, %(age)s, (select id from shelter where name = %(shelter_name)s), (select id from breed where species_id in (select id from species where name = %(species_name)s) and name = %(breed_name)s), bool(%(adopted)s))", line)
          #cur.commit()
      except:
          print "I can't Insert Into pet"
      # else cur.commit()
    
      cur = conn.cursor()
      try:
          cur.execute("""SELECT * from pet""")
      except:
          print "I can't SELECT from pet"
    
      rows = cur.fetchall()
      for row in rows:
          print "   ", row
        
      return payload
    


if __name__ == "__main__":
    dictlist = []
    with open("pets.csv") as f:
        csvdict = csv_to_dictionary(f)
        for line in csvdict:
            dictlist.append(line)
    dictlist = clean_up_dictlist(dictlist)
    # print_dictionary(dictlist)
    dictlist = load_db(dictlist)
    update_db()