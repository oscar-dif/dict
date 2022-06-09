import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="dict1",
   password="dict1"
)
# read_dict: returns the list of all dictionary entries:
# argument: C - the database connection.

def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

#add_word: creates a serial and two insert variables 'word' and 'translation' and adds them to the table dictionary

def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

#delete_word deletes the serial which are connected to one variable 'word' and one variable 'translation'

def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()

#save_dict uses the command 'COMMIT' to save possible changes to the database thrue the connection C

def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(f"Here is the current dictionary: ")
        print(read_dict(conn))
    elif cmd == "add":
        word = input("  Word: ")
        translation = input("  Translation: ")
        add_word(conn, word, translation)
        print(f"  Added word {word} to dictionary.")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
        print(f"  Deleted word with ID {ID}.")
    elif cmd == "quit":
        save_dict(conn)
        print(f"  Goodbye!")
        exit()
