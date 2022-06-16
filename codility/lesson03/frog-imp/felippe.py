def solution(X, Y, D):
  if X == Y:   # testar os casos que não precisam de jump
    return 0
  jump_float = (Y-X)/D
  jump_int = (Y-X)//D
  if jump_float == jump_int: # divisão inteira
    return jump_int
  if jump_int % 2 == 0: # arrendondamento de números pares
    if (jump_float - jump_int) > 0.5:
        result = round(jump_float)
    else:
        result = round(jump_float) + 1
  else: # arrendondamento de números ímpares
    if (jump_float - jump_int) >= 0.5:
        result = round(jump_float)
    else:
        result = round(jump_float) + 1
  return int(result)
