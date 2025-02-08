import argparse

def karatsuba(x, y):
    # Caso base: se x ou y tiverem 1 dígito, multiplicamos diretamente
    if x < 10 or y < 10:
        return x * y

    # Calcula o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Divide os números em partes altas e baixas
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # Recursivamente calcula os três produtos necessários
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # Combina os resultados usando a fórmula de Karatsuba
    return ac * 10**(2 * m) + ad_plus_bc * 10**m + bd

# Recebe os argumentos da linha de comando do x e y
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="primeiro número")
parser.add_argument("y", type=int, help="segundo número")
args = parser.parse_args()


# Exemplo de uso
resultado = karatsuba(args.x, args.y)
print(f"{args.x} * {args.y} = {resultado}")