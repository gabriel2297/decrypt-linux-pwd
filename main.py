#!/usr/bin/python3
import re


def main():
    # mostrar banner de bienvenida y pedir al usuario la informacion necesaria
    hash = getUserInfo()
    # verificar si el hash es valido o no
    if not isValidHash(hash):
        print("Hash invalido, por favor ingrese un hash en el formato especificado.")
        exit(0)
    # partir el hash en 3 partes, el algoritmo, el salt y el hash en si (devuelve un arreglo de 4 partes)
    split_hash = re.split("\$", hash)
    # validar que el algoritmo es valido
    algo = getAlgo(split_hash[1])
    if algo is None:
        print("Algoritmo invalido, utilice 1 para md5, 2a para blowfish, 2y para blowfish con manejo de caracteres de 8 bits, 5 para sha256 o 6 para sha512")
        exit(0)
    
    print("Algoritmo: %s" % algo['name'])
    print("Salt: %s" % split_hash[2])
    print("Hash: %s" % split_hash[3])


def getUserInfo():
    """
    Imprime un banner de bienvenida y pide al usuario el hash de la contraseña que desea desencriptar.
    Devuelve el hash que el usuario ingreso+    
    """
    print("""\
    +-------------------------------------------------------------------------------------------------------------------------------------+
    |   Bienvenido!! Por favor ingrese el hash de la contraseña que desea desencriptar. El formato debe de ser $algoritmo$salt$contraseña |
    +-------------------------------------------------------------------------------------------------------------------------------------+
    """)
    return input("Hash a desencriptar: ")


def isValidHash(hash):
    """
    Funcion utilizada para validar que el hash que se haya ingresado sea el indicado. 
    Retorna un objeto match o None dependiendo si el hash, una vez validado por la expresion regular, es valido.
    """
    return re.search("^\$[1256]{1}[ay]{0,1}\$[^:]*\$[^:]*$", hash)


def getAlgo(algo):
    valid_algorithms = {
        '1': {'id': '1', 'name': 'md5'}, 
        '2a': {'id': '2a', 'name': 'blowfish'}, 
        '2y': {'id': '2y', 'name': 'blowfish with correct 8 bit character support'}, 
        '5': {'id': '5', 'name': 'sha256'}, 
        '6': {'id': '6', 'name': 'sha512'}
    }
    for alg, data in valid_algorithms.items():
        if alg == algo:
            return data
    return None


if __name__ == "__main__":
    main()
