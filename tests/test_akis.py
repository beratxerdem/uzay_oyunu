from itertools import islice, takewhile
from uzay_oyunu.akis import fibonacci

def test_fibonacci_uc_yol() -> None:
    """fibonacci generatorunun next, islice ve takwhile ile kullanımını test eder."""
    #next ile 3 deger
    g = fibonacci()
    assert(next(g), next(g), next(g) == (0,1,1))

    #is lice ile ilk 12

    ilk_12 = list(islice(fibonacci(), 12))
    assert ilk_12 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    #takewhile ile x<100 değerleri
    yuzdenKucuk = list(takewhile(lambda x: x < 100, fibonacci()))
    assert yuzdenKucuk == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
                       
def test_fibonnaci_singleuse() -> None:
    #aynı generatorun ikinci list(islice) cagrısının farklı döndüp dönmedigini test eder
    ayniGenerator = fibonacci()
    ilk_cagrı = list(islice(ayniGenerator, 5))
    ikinci_cagrı = list(islice(ayniGenerator, 5))
    assert ilk_cagrı == [0,1,1,2,3]
    assert ikinci_cagrı == [5,8,13,21,34]
    assert ilk_cagrı != ikinci_cagrı