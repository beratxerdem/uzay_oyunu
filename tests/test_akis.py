from itertools import islice, takewhile
from uzay_oyunu.akis import fibonacci
from pathlib import Path
from uzay_oyunu.akis import( 
    fibonacci,yakit_gostergesi,satirlari_oku,ayristir,uzun_yolculuklar,rota_sayaci,
)
from uzay_oyunu.oyun import harita_yukle, travel
from uzay_oyunu.istatistik import(
    büyük_harfli_gezegenler_lc,büyük_harfli_gezegenler_map,en_az_iki_baglantili_filter,en_az_iki_baglantili_lc,hizli_yolculuk,toplam_baglanti_reduce,toplam_baglanti_sum,yolculuk,
)

def test_fibonacci_uc_yol() -> None:
    """fibonacci generatorunun next, islice ve takwhile ile kullanımını test eder."""
    #next ile 3 deger
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)

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


def test_rota_sayaci() -> None:
    """önebellekli rotasayacinin örnekleri dogru hesapladıgını test eder"""
    galaksi = harita_yukle()
    say = rota_sayaci(galaksi["baglantilar"])

    assert (say("dünya", 3), say("dünya", 10), say("dünya", 40)) == (15, 11683, 20975801689045883)#benim testimin sonuçları

    #önbellegin calıstıgını dogrular
    bilgi = say.cache_info()
    assert bilgi.hits > 0


def test_istatistik_soruları() -> None:
    """görev 5deki üç sorunun iki farklı yonötemlede aynı sonucu verdiğini testler"""
    galaksi = harita_yukle()

    #büyük harfli gezegenler
    beklenen_buyuk = ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]
    assert büyük_harfli_gezegenler_map