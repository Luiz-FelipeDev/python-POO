import sys 

class Valor:
    c = 0.0    
    d = 0.0   
    e = 0.0
    
    def valor_1(self):
        try:
            c = self.c = int(input("Digite o primeiro valor "))
            return c
        except:
            print("Valor inválido! Digite um número, se for floar utilize '.' ")
        self.valor_1()
        
    def valor_2(self):
        try:
            d = self.d = int(input("Digite o primeiro valor "))
            return d
        except:
            print("Valor inválido! Digite um número, se for floar utilize '.'")
        self.valor_2
        
        
                      
       