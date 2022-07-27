# Lesson 7 Ex 03
# Stone Wall
# 92%
# 100% correctness
# 82% performance
# Detected time complexity: O(N) or O(N**2)

def solution(H):
    N = len(H)
    H_open = H[0]
    open_blocks = [H_open]
    blocks = 1 # bloco do elemento inicial
    
    for i in range(1, N):
      
        if open_blocks[-1] > H[i]: # fechando blocos
            
            B = list(filter(lambda element: element > H[i], open_blocks)) # comparando quantos elementos de open_blocks são maiores do que o novo elemento
            blocks += len(B) # blocos que serão fechados
            open_blocks = list(filter(lambda element: element < H[i], open_blocks)) # open_blocks serão os elementos menores e o elemento atual
            open_blocks.append(H[i]) # incluindo o elemento atual
     
        if open_blocks[-1] < H[i]: # abrindo blocos
            open_blocks.append(H[i])
       
    return blocks + len(open_blocks) - 1
