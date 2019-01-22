import sqlite3

# The sys modules gives us access to whatever is passed in from the command line, in the form of a list called 'argv' so the name of the file you're executing is always index 0. Running `python super.py Batman` would give us a sys.argv of ['super.py', 'Batman']
import sys

bagOfLot_db = '/Users/danielcombs/workspace2/practice/excersises/excersise13/bagOfLot.db'

# 1  Add a toy to the bag o' loot, and label it with the child's name who will receive it.
# The first argument must be the word add. The second argument is the gift to be delivered.
#  The third argument is the name of the child.
def addPresent(Presents):
  with sqlite3.connect(bagOfLot_db) as conn:
    cursor = conn.cursor()
    try:
      cursor.execute(
        '''
        INSERT INTO Presents
        Values(?, ?, ?, ?)
        ''', (None , Presents["name"] , Presents["delivered"] , Presents["child_Id"])
      )
    except sqlite3.OperationalError as err:
      print("oops", err)


# 2 Remove a toy from the bag o' loot in case a child's status changes before delivery starts.
def deletePresent(presentID):

      with sqlite3.connect(bagOfLot_db) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f'''
            Delete From Presents
            Where Presents.present_Id = '{presentID}'
            '''
            )
        except sqlite3.OperationalError as err:
            print("oops", err)

# 3 Produce a list of children currently receiving presents.
def getChildren():
  with sqlite3.connect(bagOfLot_db) as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Child')
    child = cursor.fetchall()
    print("GetChildren",child)

# 4 List toys in the bag o' loot for a specific child.
def getChild(child):
  with sqlite3.connect(bagOfLot_db) as conn:
    cursor = conn.cursor()

    cursor.execute(f'''SELECT * FROM Child c
                      JOIN Presents p
                      ON c.child_Id = p.child_id
                      WHERE c.Name = '{child}'
                    ''')

    child = cursor.fetchone()
    print("get child",child)
    return child


def addChild(child):
  with sqlite3.connect(bagOfLot_db) as conn:
    cursor = conn.cursor()
    try:
      cursor.execute(
        '''
        INSERT INTO Child
        Values(?,?)
        ''', (None , "Daniel")
      )
    except sqlite3.OperationalError as err:
      print("oops", err)


def  getPresentId(present_name):
    with sqlite3.connect(bagOfLot_db) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f'''
            select * from Presents
            where Presents.present_name = '{present_name}'
            '''
            )
            present_id = cursor.fetchone()
            return present_id[0]
        except sqlite3.OperationalError as err:
            print("oops", err)


def presentsRecieved(childName):

      with sqlite3.connect(bagOfLot_db) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f'''
            select * from Child c
            where c.Name = '{childName}'
            and c.delivered = 0
            '''
            )
            print("Delivered")

        except sqlite3.OperationalError as err:
            print("oops", err)





if __name__ == "__main__":

    if sys.argv[1] == 'getAll':
        getChildren()


    if sys.argv[1] == 'getChild':
        print(sys.argv[2])
        getChild(sys.argv[2])

    if sys.argv[1] == 'deletePresent':
        present_id = getPresentId(sys.argv[2])
        deletePresent(present_id)
    if sys.argv[1] == 'wasDeliveredTo':
        presentsRecieved(sys.argv[2])

# Must be able to list all children who are getting a toy.