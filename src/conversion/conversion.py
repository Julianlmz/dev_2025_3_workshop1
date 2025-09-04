class Conversion:
    def celsius_a_fahrenheit(self, celsius):

        return(celsius * 9/5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):

        return(fahrenheit - 32) * 5/9
    
    def metros_a_pies(self, metros):

        return(metros * 3.28084)
    
    def pies_a_metros(self, pies):

        return (pies * 0.3048)
    
    def decimal_a_binario(self, decimal):

        if decimal == 0:
            return "0"
        if decimal < 0:
            raise ValueError("Solo se permiten enteros no negativos")
        return bin(int(decimal))[2:]
    
    def binario_a_decimal(self, binario):

        return int(binario, 2)
    
    def decimal_a_romano(self, numero):

        if not (1 <= int(numero) <= 3999):
            raise ValueError("El número debe estar entre 1 y 3999")
        numero = int(numero)
        miles = ["", "M", "MM", "MMM"]
        centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            miles[numero // 1000]
            + centenas[(numero % 1000) // 100]
            + decenas[(numero % 100) // 10]
            + unidades[numero % 10]
        )
    
    def romano_a_decimal(self, romano):

        valores = {"I": 1, "V": 5, "X": 10, "L": 50,
                   "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = 0
        for letra in romano.upper()[::-1]:
            valor = valores[letra]
            if valor < prev:
                total -= valor
            else:
                total += valor
            prev = valor
        return total
    
    def texto_a_morse(self, texto):

        tabla = {
            'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
            'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
            'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
            'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
            'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----','1': '.----','2': '..---','3': '...--',
            '4': '....-','5': '.....','6': '-....','7': '--...',
            '8': '---..','9': '----.',
            ' ': '/' 
        }
        texto = texto.upper()
        return ' '.join(tabla[ch] for ch in texto if ch in tabla)
    
    def morse_a_texto(self, morse):

        tabla_inv = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
            '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
            '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
            '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z',
            '-----': '0', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7',
            '---..': '8', '----.': '9'
        }

        resultado = []
        for token in morse.strip().split():
            if token == '/':
                resultado.append(' ')
            elif token in tabla_inv:
                resultado.append(tabla_inv[token])
        return ''.join(resultado)