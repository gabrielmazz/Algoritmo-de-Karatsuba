# <p align="center">Algoritmo de Karatsuba</p>

<h3 align="center">Projeto de Análise e Algoritmos</h3>

<p align="center">
    O algoritmo de Karatsuba é um método rápido de multiplicação de números grandes. O algoritmo foi descoberto por Anatolii Alexeevitch Karatsuba em 1960 e publicado em 1962. Este algoritmo reduz a multiplicação de dois números de n dígitos ao máximo
</p>

$$
Mult\_{tradicional} = O\left(n^2\right)
$$

$$
Alg\_{Karatsuba} = O\left(n^{\log_2{3}}\right) \approx O\left(n^{1.585}\right)
$$

<p align="center">
    Para o algoritmo ser executado, básicamente ele separa os números em duas partes, e realiza a multiplicação de forma recursiva, até que os números sejam pequenos o suficiente para serem multiplicados de forma tradicional, sempre pegando a parte mais significativa e menos significativa dos números.
</p>

```python
a = x // 10**m
b = x % 10**m
c = y // 10**m
d = y % 10**m
```

<p align="center">
    Calcula-se três valores, sendo a multiplicação de a e c, b e d, e a soma de a e b multiplicado por c e d, indo então para o
    resultado final que é a multiplicação de ac * 10^(2m) + (ad + bc) * 10^m + bd, dando o resultado da multiplicação dos números.
</p>

```python
ac = karatsuba(a, c)
bd = karatsuba(b, d)
ad_bc = karatsuba(a + b, c + d) - ac - bd
return ac * 10**(2 * m) + ad_plus_bc * 10**m + bd
```

<h4 align="center">Executar o algoritmo</h4>

<p align="center">
    Para executar o algoritmo, basta rodar o arquivo Karatsuba.py, passando como parâmetro os números que deseja multiplicar, sendo o primeiro número o x e o segundo o y

```bash
python3 Karatsuba.py 1234 4321
```

