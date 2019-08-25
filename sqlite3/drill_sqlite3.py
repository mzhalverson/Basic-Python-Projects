

import sqlite3, os



conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()

conn.close()


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for file in fileList:
    name, ext = os.path.splitext(file)
    
    if ext == '.txt':
        conn = sqlite3.connect('files.db')
        with conn:
            cur = conn.cursor()
            print(file)
            cur.execute("INSERT INTO tbl_txtfiles(col_file) VALUES (?)", (file,))        
            conn.commit()
        conn.close()


conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file FROM tbl_txtfiles")
    varFile = cur.fetchall()
    print(varFile)
    
    conn.commit()

conn.close()






    
