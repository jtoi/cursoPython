import sqlite3

DB_NAME = "./peliculas.db"

def create_squema():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS peliculas ("+
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
                   "titulo TEXT NOT NULL, "+
                   "director TEXT NOT NULL, "+
                   "ano_estreno INTEGER NOT NULL)")
    connection.commit()
    cursor.close()

def create(titulo, director, ano_estreno):
    cursor = connection.cursor()
    sql=f"insert into peliculas (titulo, director, ano_estreno) values ('{titulo}','{director}',{ano_estreno})"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def read(id):
    cursor = connection.cursor()
    sql = f"select * from peliculas where id={id}"
    peliculas = cursor.execute(sql).fetchone()
    connection.commit()
    cursor.close()
    return peliculas

def read_all():
    cursor = connection.cursor()
    sql = f"select * from peliculas"
    peliculas = cursor.execute(sql).fetchall()
    connection.commit()
    cursor.close()
    return peliculas

def update(id, ano):
    cursor = connection.cursor()
    sql = f"update peliculas set ano_estreno = ? where id= ?"(ano, id)
    peliculas = cursor.execute(sql)
    connection.commit()
    cursor.close()
    return peliculas

def delete(id):
    cursor = connection.cursor()
    sql = f"delete from peliculas where id={id}"
    cursor.execute(sql)
    connection.commit()
    cursor.close()


if __name__ == "__main__":
    connection = sqlite3.connect(DB_NAME)
    create_squema()
    #CREATE
    #titulo = input("Título: ")
    #director = input("Director: ")
    #ano_estreno = input("Año estreno: ")
    #create(titulo, director, ano_estreno)

    #READ ALL
    # registros = read_all()
    # for registro in registros:
    #     print(F"{registro[0]}")

    # ·UPDATE
    # ID = input("ID del registro: ")
    # ano_estreno = input("Año estreno: ")
    # update(ID, ano_estreno)

    # ·DELETE
    ID = input("ID del registro: ")
    delete(ID)

    # READ
    # ID = input("ID del registro: ")
    # peli = read(ID)
    # print(f"ID: {peli[0]} Titulo: {peli[1]} Director: {peli[2]} Año: {peli[3]}")

    connection.close()