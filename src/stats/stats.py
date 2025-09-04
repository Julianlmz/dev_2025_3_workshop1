class Stats:
    def promedio(self, numeros):

        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):

        if not numeros:
            return 0
        numeros = sorted(numeros)
        n = len(numeros)
        mitad = n // 2
        if n % 2 == 0:
            return (numeros[mitad - 1] + numeros[mitad]) / 2
        return numeros[mitad]
    
    def moda(self, numeros):

        if not numeros:
            return None
        frecuencia = {}
        moda_val = numeros[0]
        max_freq = 0
        for num in numeros:
            frecuencia[num] = frecuencia.get(num, 0) + 1
            if frecuencia[num] > max_freq:
                max_freq = frecuencia[num]
                moda_val = num
        return moda_val
    
    def desviacion_estandar(self, numeros):

        if not numeros:
            return 0
        media = sum(numeros) / len(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return varianza ** 0.5
    
    def varianza(self, numeros):
 
        if not numeros:
            return 0
        media = sum(numeros) / len(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):

        if not numeros:
            return 0
        return max(numeros) - min(numeros)