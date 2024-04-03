import unittest
'''def es__palindromo(palabra):
    palabra = palabra.lower()
#compara palabra con su reverso
    if palabra == palabra[::-1]:
        return True
    else:
        return False'''
    
def palindrome (palabra):
    palabra = palabra.lower()
    for valor in range(len(palabra)):
        if palabra[valor] != palabra[-valor - 1]:
            return False
    return True

def es_palindrome (palabra):
    palabra = palabra.lower()
    # Eliminar caracteres no alfabéticos
    palabra = ''.join(char for char in palabra if char.isalpha())
    for valor in range(len(palabra)):
        if palabra[valor] != palabra[-valor - 1]:
            return False
    return True
'''def es_palindrome(palabra):
    # Convertir la palabra a minúsculas
    
    # Verificar si la palabra resultante es un palíndromo
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[-i - 1]:
            return False
    return True'''


def obtener_cantidad_de_palabras_palindrome(lista_palabras):
    contador_palindromo = 0 
    for palabra in lista_palabras:
        if es_palindrome(palabra):
            contador_palindromo += 1
    return contador_palindromo
           

class TestIsPalindrome (unittest.TestCase):
    def test_with_a(self):
        use_input = "a"
        result = palindrome (use_input)
        self.assertTrue(result)
    def test_with_ala(self):
        use_input = "ala"
        result = palindrome(use_input)
        self.assertTrue(result)

    def test_with_mañana(self):
        use_input = "mañana"
        result = palindrome(use_input)
        self.assertFalse(result)
    
    def test_with_mayuscula_true(self):
        use_input = "NeuqueN"
        result = palindrome(use_input)
        self.assertTrue(result)

    def test_with_mayuscula_false(self):
        use_input = 'FrancO'
        result = palindrome(use_input)
        self.assertFalse(result)
    
    def test_with_numero(self):
        use_input = 'h2l1a'
        result = palindrome(use_input)
        self.assertFalse(result)

class TestCantidadDePalabrasPalindromes(unittest.TestCase):

    def test_cantidad_de_palabras_palindromes_simple(self):

        palabras = ["ala"]

        resultado = obtener_cantidad_de_palabras_palindrome(palabras)

        self.assertEqual(resultado, 1)



    def test_cantidad_de_palabras_palindromes_con_2(self):

        palabras = ["ala", "neuquen"]

        resultado = obtener_cantidad_de_palabras_palindrome(palabras)

        self.assertEqual(resultado, 2)



    def test_cantidad_de_palabras_palindromes_con_3(self):

        palabras = ["ala", "neuquen", "hola"]

        resultado = obtener_cantidad_de_palabras_palindrome(palabras)

        self.assertEqual(resultado, 2)



    def test_cantidad_de_palabras_palindromes_con_4(self):

        palabras = ["ala", "neuquen", "hola", "programacion"]

        resultado = obtener_cantidad_de_palabras_palindrome(palabras)

        self.assertEqual(resultado, 2)



    def test_cantidad_de_palabras_palindromes_con_5(self):

        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]

        resultado = obtener_cantidad_de_palabras_palindrome(palabras)

        self.assertEqual(resultado, 3)



    def test_cantidad_de_palabras_palindromes_complejo(self):

        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]

        resultado = obtener_cantidad_de_palabras_palindrome(palabras)

        self.assertEqual(resultado, 4)



    def test_cantidad_de_palabras_palindromes_complejo_2(self):

        palabras = [

            "ala",

            "neuquen",

            "hola",

            "programacion",

            "palap",

            "neu  quen",

            "agita falsos usos la fatiga",

            "presidente de la camara de diputados: martin menem",

			"A man, a plan, a canal -- Panama"


        ]

        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        
        self.assertEqual(resultado, 6)


    

unittest.main()