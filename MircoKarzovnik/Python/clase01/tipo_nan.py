from decimal import Decimal
import math


# NaN (Not a Number)
a = float('nan')
print(f'a: {a}')

# Modula Mth
a = float('nan')
print(f"Es de todo tipo NaN(Not a Number)?: {math.isnan(a)}")

#Modulo decimal
a = Decimal('nan')
print(f'Es de tipo NaN(Not a Number)?: {math.isnan(a)}')