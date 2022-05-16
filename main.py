"""
Universidad Francisco Marroquín
Examen Final - Programación I
"""


secret_message = "Ef43u77432kMu65fD3u88fsu32u86Fa30u694rU43Q4u82fdu8332Au84Fwu65u80u80f3tfu6942u780iu329p4u35fk3u494H"
caracter_cod = []
result = 0
x = 0
def find_message(encoded_message: str) -> str:

    for i in range(len(secret_message)):
        if secret_message[i] == "u":
            x = secret_message[i+1] + secret_message[i+2]
            caracter_cod == int(i)
            result = chr(i)

    return result
    
print(find_message(secret_message))