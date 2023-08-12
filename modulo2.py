from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///diccionario2_db.db")
session = sessionmaker(bind=engine)()

Base = declarative_base()


class Palabra(Base):

    __tablename__ = "Palabras"

    palabrita = Column(String, primary_key=True)
    significadito = Column(String)

    def __init__(self, palabrita, significadito):
        self.palabrita = palabrita
        self.significadito = significadito


Base.metadata.create_all(engine)


def inicio():
    menu()


def menu():
    print("Menu"
          "\n1- Agregar Palabra"
          "\n2- Editar Palabra"
          "\n3- Mostrar Diccionario"
          "\n4- Eliminar Palabra"
          "\n5- Buscar Palabra"
          "\n6- Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        agregar()
    elif opcion == 2:
        editar()
    elif opcion == 3:
        mostrar_todas()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        buscar()
    elif opcion == 6:
        exit(0)


def agregar():
    palabra = input("Ingrese palabra: ")
    significado = input("Ingrese significado: ")
    palabra_1 = Palabra(palabra, significado)
    session.add(palabra_1)
    session.commit()
    inicio()


def editar():
    palabra = input("Ingrese palabra a modificar: ")
    record = session.query(Palabra).filter_by(palabrita=palabra).first()
    nuevo_significado = input("Ingrese significado: ")
    record.significadito = nuevo_significado
    session.commit()
    inicio()


def mostrar_todas():
    records = session.query(Palabra).all()
    for record in records:
        print("Palabra: " + record.palabrita + " Significado: " + record.significadito)
    inicio()


def eliminar():
    palabra = input("Ingrese palabra a eliminar: ")
    record = session.query(Palabra).filter_by(palabrita=palabra).first()
    session.delete(record)
    session.commit()
    print("Palabra eliminada con exito.")
    inicio()


def buscar():
    palabra = input("Ingrese palabra a buscar: ")
    record = session.query(Palabra).filter_by(palabrita=palabra).first()
    print("Palabra: " + record.palabrita + "; Significado: " + record.significadito)
    inicio()


inicio()