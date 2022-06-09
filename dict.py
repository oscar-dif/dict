import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="dict1",
   password="dict1"
)
# read_dict: returns the list of all dictionary entries:
# argument: conn - the database connection.

def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

#add_word: creates a serial and two insert variables 'word' and 'translation' and adds them to the table dictionary

def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

#delete_word deletes the serial which are connected to one variable 'word' and one variable 'translation'

def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()

#save_dict uses the command 'COMMIT' to save possible changes to the database thrue the connection C

def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()

main()
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
main()
    while True: ## REPL - Read Execute Program Loop
        cmd = input("Command: ")
        if cmd == "list":
            for i, wd, trans in read_dict(conn):
                print(f"{i}: {wd} - {trans}")
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
