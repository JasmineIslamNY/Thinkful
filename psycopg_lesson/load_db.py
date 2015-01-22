import psycopg2
 
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
    