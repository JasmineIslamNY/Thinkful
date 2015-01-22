import psycopg2
 
def update_db():
    pass     
     
def load_db(payload):
    dictionary = []
    dictonary = payload
    print dictionary
    
    try:
        conn=psycopg2.connect("dbname='pets' user='action' password='731Lexington'")
        print "I connected"
    except:
        print "I am unable to connect to the database."
    cur = conn.cursor()
    try:
        cur.executemany("""INSERT INTO pets (name, age, breed_id, shelter_id, adopted) VALUES (%(Name)s, %(age)s, (select breed_id from breed where breed_name = %(breed_name)s), (select shelter_id from shelter where shelter_name = %(shelter_name)s), %(adopted)s)""", payload)
    except:
        print "I can't SELECT from bar"
    # else cur.commit()
    
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * from pets""")
    except:
        print "I can't SELECT from pets"
    
    rows = cur.fetchall()
    for row in rows:
        print "   ", row
        
    return payload
    