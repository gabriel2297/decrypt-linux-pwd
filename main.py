#!/usr/bin/python3
import re, crypt


def main():
    hash = getUserInfo() # mostrar banner de bienvenida y pedir al usuario la informacion necesaria

    if not isValidHash(hash): # verificar si el hash es valido o no
        print("Hash invalido, por favor ingrese un hash en el formato especificado.")
        exit(0)

    split_hash = re.split("\$", hash) # partir el hash en 3 partes (devuelve un arreglo de 4 partes)
    algo = getAlgo(split_hash[1]) # validar el algoritmo
    if algo is None:
        print("Algoritmo invalido, utilice 1 para md5, 2a para blowfish, 2y para blowfish con manejo de caracteres de 8 bits, 5 para sha256 o 6 para sha512")
        exit(0)
    
    # imprimir informacion del algoritmo 
    print("Algoritmo: %s" % algo['name'])
    print("Salt: %s" % split_hash[2])
    print("Hash: %s" % split_hash[3])

    decrypted_pwd = performBruteForce(split_hash) # intentar desencriptar contraseña
    if decrypted_pwd is None:
        print("No se pudo obtener la contraseña, lo sentimos... :( ")
        exit(0)

    print("Felicidades!! La contraseña es \"%s\" (sin las comillas) :) " % decrypted_pwd)


def getUserInfo():
    return input("Por favor ingrese el hash de la contraseña que desea desencriptar. El formato debe de ser $algoritmo$salt$contraseña: ")


def isValidHash(hash):
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

def performBruteForce(split_hash):
    print("TODO")
    return False

if __name__ == "__main__":
    main()
