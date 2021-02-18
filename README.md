# Universidad de Costa Rica
### PF3893 - Seguridad aplicada a infraestructura | decrypt-linux-pwd
Estudiantes: 
- Jean Carlo Mata Serrano (B89880)
- Gabriel Umaña Frías (C09913)

### Uso
1. Clone este repositorio a su computadora.
2. Agregue diccionarios de contraseñas al directorio en donde se encuentra este archivo. Puede encontrar ejemplos aqui https://github.com/danielmiessler/SecLists/tree/master/Passwords
3. Ejecute `python3 main.py` e ingrese el hash a desencriptar una vez se le pida. Ejemplo: 

```
➜  tareapractica2 git:(main) ✗ python3 main.py
Por favor ingrese el hash de la contraseña que desea desencriptar. El formato debe de ser $algoritmo$salt$contraseña: $1$SALt$.3QJjMGNt0dIcUC06TXYc1
Algoritmo identificado: md5
Buscando hash "$1$SALt$.3QJjMGNt0dIcUC06TXYc1" con salt "$1$SALt"
Buscando en archivo xato-net-10-million-passwords-dup.txt...
Total de lineas analizadas: 6006. Archivo donde se encontro: xato-net-10-million-passwords-dup.txt
Felicidades!! La contraseña es "radiohead" (sin las comillas) :)
```