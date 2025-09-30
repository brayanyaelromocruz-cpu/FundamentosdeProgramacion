#
import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },
    "987-84-450-00668-7": {
        "título":"EEl Señor de los Anillos III.(El Retorno del Rey)",
        "autor":["J. R. R. Tolkien"],
        "géneros": ["Fantacia ","Guerra"]
    },
    "978-60-731-9464-8": {
        "título":"Dune ( Las crónicas de Dune 1 )",
        "autor":["Frank Herbert"],
        "géneros":[" Space Opera Ciencia Ficción"," Ciencia Ficción Militar "]
    },
    "978-60-752-7967-1": {
        "título":"La Narradora(Mar de tinta y oro)",
        "autor":["Traci Chee"],
        "géneros":["fantasía, aventuras,"]
    }
    

}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)