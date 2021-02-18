#!/usr/bin/python3
import re, crypt, os

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
    print("Algoritmo identificado: %s" % algo['name'])

    decrypted_pwd = performBruteForce(split_hash)
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
    counter_palabras = 0
    hash_a_encontrar = "$" + split_hash[1] + "$" + split_hash[2] + "$" + split_hash[3]
    salt = "$" + split_hash[1] + "$" + split_hash[2]
    print("Buscando hash \"%s\" con salt \"%s\"" % (hash_a_encontrar, salt))
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".txt"):
            print("Buscando en archivo %s..." % file)
            f = open(file, "r")
            for line in f:
                line = line.rstrip()
                counter_palabras += 1
                hash_resultante = crypt.crypt(line, salt)
                if hash_a_encontrar == hash_resultante:
                    print("Total de lineas analizadas: %i. Archivo donde se encontro: %s" % (counter_palabras, file))
                    return line
            f.close()

    return None

if __name__ == "__main__":
    main()