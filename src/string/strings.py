class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        if texto is None:
            return False
        limpio = "".join(ch.lower() for ch in texto if ch.isalnum())
        return limpio == limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        resultado = ""
        for ch in texto:
            resultado = ch + resultado
        return resultado
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        if not texto:
            return 0
        vocales = set("aeiouAEIOU")
        return sum(1 for ch in texto if ch in vocales)
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        if not texto:
            return 0
        vocales = set("aeiouAEIOU")
        return sum(1 for ch in texto if ch.isalpha() and ch not in vocales)
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        if texto1 is None or texto2 is None:
            return False
        a = "".join(ch.lower() for ch in texto1 if ch.isalnum())
        b = "".join(ch.lower() for ch in texto2 if ch.isalnum())
        return sorted(a) == sorted(b) and a != ""
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        if not texto or texto.strip() == "":
            return 0
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        res = []
        mayus = True
        for ch in texto:
            if mayus and ch.isalpha():
                res.append(ch.upper())
                mayus = False
            else:
                res.append(ch)
                if ch.isspace():
                    mayus = True
        return "".join(res)
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        out = []
        i = 0
        n = len(texto)
        while i < n:
            out.append(texto[i])
            if texto[i] == " ":
                while i + 1 < n and texto[i + 1] == " ":
                    i += 1
            i += 1
        return "".join(out)
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if texto is None:
            return False
        t = texto.strip()
        if t in ("+", "-") or t == "":
            return False
        if t[0] in "+-":
            t = t[1:]
        return t.isdigit()
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = ""
        for ch in texto:
            if ch.isalpha():
                base = ord("A") if ch.isupper() else ord("a")
                resultado += chr((ord(ch) - base + desplazamiento) % 26 + base)
            else:
                resultado += ch
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if not subcadena:
            return []
        posiciones = []
        L = len(subcadena)
        for i in range(len(texto) - L + 1):
            if texto[i:i+L] == subcadena:
                posiciones.append(i)
        return posiciones