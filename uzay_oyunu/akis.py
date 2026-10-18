from collections.abc import Iterator,Iterable
from itertools import islice, takewhile
from pathlib import Path
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

def satirlari_oku(yol: str | Path) -> Iterator[str]:
    """dosyayı satır satır okur boş ve # ile baslayan satırlar haric"""
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz
    
def ayristir(satirlar: Iterable[str]) -> Iterator[tuple[str, str, int]]:
    """satırlardan kaynak hedef ve yakıt verilerini tupleye çevirir."""
    for satir in satirlar:
        # kelimeleri ayırmak için.
        parcalar = satir.replace("->", " ").replace(">", " ").split()
        kaynak = parcalar[0]
        hedef = parcalar[1]
        yakit = int(parcalar[2])
        yield(kaynak,hedef,yakit)


def uzun_yolculuklar(kayitlar: Iterable[tuple[str,str,int]], esik: int) -> Iterator[tuple[str,str,int]]:
    """yakıtın max değerinden fazla olan kayıtları süzer."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield(kaynak,hedef,yakit)




if __name__ == "__main__":
    #next ile ilk üç değer
    g = fibonacci()
    print("next() ile ilk 3:", next(g), next(g), next(g))

    #itertools.islice ile ilk 12 değer
    print("islice ile ilk 12:", list(islice(fibonacci(), 12)))

    #itertools.takewhile ile 100den küçük değerler
    print("100den kücük değerler: ", list(takewhile(lambda x: x<100, fibonacci())))

    #görev 2 yakıt göstergesi
    print("Yakıt göstergesi (100, 30):", list(yakitGöstergesi(100,30)))





    