class Poligono:
    def __init__(self, numero_de_lados):
        self.n = numero_de_lados
        self.lados = [0 for i in range(numero_de_lados)]
        
    def le_lados(self):
        '''
        for i, lado in enumerate(self.lados):
            self.lados[i] = lado = float(input(f'Digite o valor do lado {lado+1}: '))
        '''
        self.lados = [float(input(f'Digite o valor do lado {lado+1}: '))  
                        for lado in self.lados
                    ]
          
    def mostra_lados(self):
        for i in range(self.n):
            print(f'lado {i+1} tem comprimento {self.lados[i]}')
        
class Triangulo(Poligono):
    def __init__(self):
        Poligono.__init__(self, 3)
        
    def area(self):
        a, b, c = self.lados
        # calcula do semiperimetro:
        p = (a + b + c)/2
        area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        print(f'Area do triangulo é {area}')  
        
class Retangulo(Poligono):
    def __init__(self):
        Poligono.__init__(self, 4)
        
    def le_lados(self):
        lado_1 = float(input(f'Digite o primeiro lado: '))
        lado_2 = float(input(f'Digite o segundo lado: '))
        
        self.lados[0] = self.lados[2] = lado_1
        self.lados[1] = self.lados[3] = lado_2
        
    def area(self):
        return  self.lados[0] * self.lados[1]
    
    def diagonal(self):
        return (self.lados[0] **2 + self.lados[1]**2) ** 0.5
        
    
        
                    
        
    
        
'''    
poli = Poligono(3)
poli.le_lados()
poli.mostra_lados()
'''

tri = Triangulo()
tri.le_lados()
tri.mostra_lados()
tri.area()
