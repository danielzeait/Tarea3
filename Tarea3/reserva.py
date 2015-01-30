import points
import rangos

'''
Created on 29/1/2015

@author: Daniel Zeait
@author: Hector Goncalves

Programa que retorna si hay o no espacio para un carro
en un estaciomento a una hora determinada

'''
    
''' ----- Definiciones de clases ----- '''
    
class Point:
    def __init__(self, point,type):
        self.point=point
        self.type=type
        
    def get_Point(self):
        return self.point
    
    def get_Type(self):
        return self.type

    
class Range:
    def __init__(self, start,end):
        self.start=start
        self.end=end
        
    def get_Start(self):
        return self.start
    
    def get_End(self):
        return self.end

'''----- Definiciones de funciones ---- '''


def sort_table(table):

    for i in range(1, len(table)):
        j = i
        while j > 0 and table[j].get_Point() < table[j-1].get_Point():
            table[j], table[j-1] = table[j-1], table[j]
            j -= 1
    return table

''' ---- Implementacion del algoritmo de Marzullo --- '''
        
def marzullo(Range):
        best = 0
        cnt = 0
        beststart = 0
        bestend = 0 
        p = 0
            
        tabla = []
      
        for r in Range:
            
            point_inicial = Point(r.get_Start(),-1)
            point_final = Point(r.get_End(),+1)
            tabla.append(point_inicial)
            tabla.append(point_final)
                       
        tabla = sort_table(tabla)
        
        while p < len(tabla):
           
            cnt = cnt - tabla[p].get_Type()
            if cnt > best:
                best = cnt
                beststart = tabla[p].get_Point()
                if p < len(tabla) -1:
                    bestend = tabla[p+1].get_Point()                
            else:
                pass             
            p+=1
            
        result = [best,beststart,bestend]
        return result
    

'''--- Codigo programa principal --- '''
ranges = []

def main():
    
    ''' variables '''

    max_spots = 10
    
    r=Range 
    
    r1 = Range(5,9)
    r2 = Range(4,9)
    r3 = Range(5,7)
    r4 = Range(3,4)
    r5 = Range(6,8)
    r6 = Range(1,9)
    r7 = Range(5,9)
    r8 = Range(4,9)
    r9 = Range(5,7)
    r10 = Range(5,7)
   
    ranges.append(r1)
    ranges.append(r2)
    ranges.append(r3)
    ranges.append(r4)
    ranges.append(r5)
    ranges.append(r6)
    ranges.append(r7)
    ranges.append(r8)
    ranges.append(r9)
    ranges.append(r10)

    hi = input('Introduzca hora inicial reservación ')
    hf = input('Introduzca hora final reservación ')

    hii=int(hi)
    hfi=int(hf)
    
    new_range = Range(hii,hfi)
    ranges.append(new_range)
    
    r = marzullo(ranges)
    print(r)
    
    if (r[0] == max_spots and ((hii or hfi) in (r[1],r[2]))):
        print("No hay puestos disponibles en el horario solicitado")
    else:
        print("Contamos con puestos disponibles. Solicitu aprobada")

    
main()