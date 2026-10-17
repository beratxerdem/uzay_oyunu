from collections.abc import Iterator
from itertools import islice, takewhile

def fibonacci() -> Iterator[int]:
    """sonsuz fibonacci sayı dizisini üreten generator"""
    a,b = 0,1
    while True:
        yield a
        a,b = b,a + b

def yakitGöstergesi(yakıt: int, tüketim: int):
    """her next() cagrısında tüketim kadar azalıp kalan yakıtı üretir ve döndürür yakıt 0a gelince durur."""
    while yakıt>0:
        yakit = max(0, yakit - tüketim)
        yield yakit

if __name__ == "__main__":
    #next ile ilk üç değer
    g = fibonacci()
    print("next() ile ilk 3:", next(g), next(g), next(g))

    #itertools.islice ile ilk 12 değer
    print("islice ile ilk 12:", list(islice(fibonacci(), 12)))

    #itertools.takewhile ile 100den küçük değerler
    print("100den kücük değerler: ", list(takewhile(lambda x: x<100, fibonacci())))





    