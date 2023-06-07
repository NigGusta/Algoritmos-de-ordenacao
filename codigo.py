#para abrir arquivos txt
with open('name.txt','r') as f:
    lista = f.readlines()
    lista = [x.strip('\n')for x in lista]
    listaint = list(map(int, lista))
 #___________________________________________________________________________________________________
#para abrir arquivos in
arquivo = open("name.in", "r")  
conteudo = arquivo.readlines()  
conteudo = [x.strip('\n') for x in conteudo]  
conteudo = list(map(int, conteudo))  
arquivo.close() 
#___________________________________________________________________________________________________
#ALGORITMOS DE ORDENACAO SEPARADOS EM FUNCOES
def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
      
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
#___________________________________________________________________________________________________
def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    print("A lista ordenada com o InsertionSort: ")  
    return data
#___________________________________________________________________________________________________   
def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
             if data[j] < data[min_index]:
                 min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    print("A lista ordenada com o SelectionSort: ")  
    return data
#___________________________________________________________________________________________________ 
def quick_sort(data):
    if len(data) <= 1:
      return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
#___________________________________________________________________________________________________
def bubble_sort(data): 
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print("A lista ordenada com o BubbleSort: ")            
    return data
#___________________________________________________________________________________________________
