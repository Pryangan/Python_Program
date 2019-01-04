import sqlite3

while True:
    print('***************************Menu********************************')
    print('1. Create Database\n2. Create Table\n3. Insert Record into Table\n4. Select From Table\n5. Update Table\n6. Delete from Table')
    choice = int(input('Enter Your Choice- '))

    if choice is 1:
        dbName = input('Enter Database Name- ')
        conn = sqlite3.connect(dbName+'.sqlite')
        conn.close()
        print(dbName+'.sqlite is Created!!!')
    elif choice is 2:
        dbName = input('Enter Database Name- ')
        conn = sqlite3.connect(dbName+'.sqlite')
        cur = conn.cursor()

        table = input('Enter Table Name- ')
        cur.execute('create table '+table+'(name varchar(127), id integer)')
        print(table+' is created!!!')
        conn.close()
    elif choice is 3:
        dbName = input('Enter Database Name- ')
        conn = sqlite3.connect(dbName+'.sqlite')
        cur = conn.cursor()

        table = input('Enter Table Name- ')
        name = input('Enter Employee Name- ')
        empid = input('Enter Employee Id- ')
        cur.execute('insert into '+table+' (name,id) values(?,?)',(name,empid))
        conn.commit()
        print('Record inserted!!!')
        conn.close()
    elif choice is 4:
        dbName = input('Enter Database Name- ')
        conn = sqlite3.connect(dbName+'.sqlite')
        cur = conn.cursor()

        table = input('Enter Table Name- ')
        for row in cur.execute('select name,id from '+table):
            print('[ Employee Name :',row[0],' ] ,[ Employee Id :',row[1],' ]')
        conn.close()
    elif choice is 5:
        dbName = input('Enter Database Name- ')
        conn = sqlite3.connect(dbName+'.sqlite')
        cur = conn.cursor()

        table = input('Enter Table Name- ')
        name = input('Enter Name for Update- ')
        empid  = input('Enter id- ')
        cur.execute('update '+table+' set name=? where id=?',(name,empid))
        conn.commit()
        conn.close()
        print('Updated record')
    elif choice is 6:
        dbName = input('Enter Database Name- ')
        conn = sqlite3.connect(dbName+'.sqlite')
        cur = conn.cursor()

        table = input('Enter Table Name- ')
        empid  = input('Enter id- ')
        cur.execute('delete from '+table+' where id=?',(empid,))
        conn.commit()
        conn.close()
        print('Deleted record')

    res = input('Do You want to Continue [y/Y]- ')
    if not res is 'y':
        break
