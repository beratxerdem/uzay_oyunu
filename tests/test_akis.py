from itertools import islice, takewhile
from uzay_oyunu.akis import fibonacci
from pathlib import Path
from uzay_oyunu.akis import( 
    fibonacci,yakitGöstergesi,satirlari_oku,ayristir,uzun_yolculuklar
)

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


def test_seyir_defteri_pipeline() -> None:
    """seyir defteri pipelineının listeyi okumadan dogru sonuc cıkarttıgını test eder"""
    dosya_yolu = Path(__file__).parent.parent / "veri" / "seyir.txt"

    #sürecin liste degil iterator döndügünü checkler
    okuyucu = satirlari_oku(dosya_yolu)
    assert hasattr(okuyucu, "__next__")

    #toplam yakıt hesabı
    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(dosya_yolu)))
    assert toplam_yakit == 88

    #esik değerlerinden büyük yolculukların hedefleri

    kayitlar = ayristir(satirlari_oku(dosya_yolu))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]