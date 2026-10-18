import time
from functools import lru_cache
from collections.abc import Callable,Iterator,Iterable
from itertools import islice, takewhile
from pathlib import Path
def fibonacci() -> Iterator[int]:
    """sonsuz fibonacci sayı dizisini üreten generator"""
    a,b = 0,1
    while True:
        yield a
        a,b = b,a + b

def yakit_gostergesi(yakit: int, tüketim: int):
    """her next() cagrısında tüketim kadar azalıp kalan yakıtı üretir ve döndürür yakıt 0a gelince durur."""
    while yakit>0:
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



def rota_sayaci(baglantilar: dict[str,list[str]]) -> Callable[[str,int], int]:
    """icinde @lru cache ile süslenmiş rota sayısı(gezegen, adim) fonksiyonunu tanımlayıp döner."""

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int: 
        if adim == 0:
            return 1
        return sum(
            rota_sayisi(komsu,adim - 1)
            for komsu in baglantilar.get(gezegen, [])
        )
    return rota_sayisi


def onbelleksiz_rota_sayaci(baglantilar: dict[str, list[str]]) -> Callable[[str,int], int]:
    """performans karşılaştırması adim=20 ölçümü için önbelleksiz rota sayacı."""
    def rota_sayisi(gezegen: str, adim: int) -> int: 
            if adim == 0:
                return 1
            return sum(
                rota_sayisi(komsu,adim - 1)
                for komsu in baglantilar.get(gezegen, [])
            )
    return rota_sayisi
    



if __name__ == "__main__":
    #next ile ilk üç değer
    g = fibonacci()
    print("next() ile ilk 3:", next(g), next(g), next(g))

    #itertools.islice ile ilk 12 değer
    print("islice ile ilk 12:", list(islice(fibonacci(), 12)))

    #itertools.takewhile ile 100den küçük değerler
    print("100den kücük değerler: ", list(takewhile(lambda x: x<100, fibonacci())))

    #görev 2 yakıt göstergesi
    print("Yakıt göstergesi (100, 30):", list(yakit_gostergesi(100,30)))


# önbellekli ve önbelleksiz Rota Sayacı Karşılaştırması
    ornek_baglantilar = {
        "sirius": ["dünya", "centauri", "orion", "kara_delik"],
        "centauri": ["dünya", "sirius", "orion"],
        "dünya": ["centauri", "sirius"],
        "orion": ["centauri", "sirius"],
        "kara_delik": [],
    }
    say_onbelleksiz = onbelleksiz_rota_sayaci(ornek_baglantilar)
    basla1 = time.perf_counter()
    sonuc1 = say_onbelleksiz("dünya", 20)
    bitis1 = time.perf_counter()
    print(f"\nÖnbelleksiz (adim=20): {sonuc1} | Süre: {bitis1 - basla1:.6f} sn")

    say_onbellekli = rota_sayaci(ornek_baglantilar)
    basla2 = time.perf_counter()
    sonuc2 = say_onbellekli("dünya", 20)
    bitis2 = time.perf_counter()
    print(f"Önbellekli  (adim=20): {sonuc2} | Süre: {bitis2 - basla2:.6f} sn")
    print("Cache Info (adim=20):", say_onbellekli.cache_info())  # type: ignore[attr-defined]