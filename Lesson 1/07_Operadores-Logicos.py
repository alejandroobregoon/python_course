# Operadores Lógicos | siempre devuelve un booleano true o false
""" AND | TRUE & TRUE == TRUE | SINO TOD0 ES FALSO
    OR  | FALSO & FALSO == FALSE | SINO TOD0 ES VERDADERO
    NOT | NOT(TRUE & TRUE == TRUE) == FALSE | REVIERTE EL VALOR
    NOT | NOT(FALSE & FALSE == FALSE) == TRUE | REVIERTE EL VALOR"""

uno = 1
dos = 2
tres = 3
cuatro = 4

op1 = uno == uno and dos == dos
print(op1)

op2 = uno == uno and dos == tres
print(op2)

op3 = dos == tres or tres == cuatro
print(op3)

op4 = dos == dos or tres == cuatro
print(op4)

op5 = not(uno == uno and dos == dos)
print(op5)

op6 = not(dos == tres or tres == cuatro)
print(op6)

