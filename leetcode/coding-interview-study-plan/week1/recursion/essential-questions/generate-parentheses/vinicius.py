'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
 
Constraints:

1 <= n <= 8


Success
Details 
Runtime: 42 ms, faster than 82.09% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.4 MB, less than 11.91% of Python3 online submissions for Generate Parentheses.
Next challenges:
Letter Combinations of a Phone Number
Check if a Parentheses String Can Be Valid
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        outputs = [['()']] # CASO BASE
        def geraParentese(n):
            if len(outputs[-1]) == 2*n - 1: # Se a quantidade de elementos na última lista inserida nos outputs for igual ao dobro de n menos 1 (A qtde de combinações de parênteses é sempre o dobro de n - 1)
                return outputs[-1] # Retorna o último elemento da lista de outputs (Que é outra lista, com a combinação dos parênteses, excluídas as duplicidades)
            setpar = set() # Criação do set para armazenar as combinações e eliminar as duplicidades.
            for element in geraParentese(n-1): # Cada elemento do último elemento (lista) dos outputs. Não é cada elemento dos outputs. Ou seja, no caso base é '()'.
                for i in range(len(element)): # Em cada posição desse último elemento (string) (exceto na última, por isso itera até o len), insere um parêntese válido '()'.
                    setpar.add(element[:i]+'()'+element[i:]) # No caso de n = 2, por exemplo, a string seria o caso base '()' e seriam inseridos os parênteses na posição 0: '()()' e 1: '(())' dessa string base '()'.
            outputs.append(list(setpar)) #Transforma o set em lista e insere no final de output
            return outputs[-1] #Retorna a última lista dos outputs
        return geraParentese(n)



