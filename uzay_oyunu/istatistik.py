from functools import partial, reduce
from typing import Any

#okunaklılık yorumu

#liste üreticiyi daha okunaklı buluyorum lambda ifadesi ve ic ice fonksiyon cagırmak sürekli akılda bir şey tutmamı gerektiriyorken
#liste okurken daha rahat ediyorum

def büyük_harfli_gezegenler_map(galaksi: dict[str, Any]) -> list[str]:
    """map ile gezegen adlarını büyük harfli liste olarak döner"""
    return list(map(lambda g: g.upper(), galaksi["gezegenler"]))

def büyük_harfli_gezegenler_lc(galaksi: dict[str, Any]) -> list[str]:
    """liste üretici kullanarak gezegen adlarını büyük harfli liste olarak döner"""
    return [g.upper() for g in galaksi["gezegenler"]]


def en_az_iki_baglantili_filter(galaksi: dict[str, Any]) -> list[str]:
    """filter kullanarak en az 2 baglantisi olan gezegenleri döner"""
    baglantilar = galaksi["baglantilar"]
    return list(
        filter(lambda g: len(baglantilar.get(g, []))) >= 2, galaksi["gezegenler"]
    )

def en_az_iki_baglantili_lc(galaksi: dict[str, Any]) -> list[str]:
    """liste üretici kullanarak en az 2 baglantisi olan gezegenleri döner"""
    baglantilar = galaksi["baglantilar"]
    return [g for g  in galaksi["gezegenler"] if len(baglantilar.get[g, []]) >= 2]


def toplam_baglanti_reduce(galaksi: dict[str, Any]) -> int:
    """reduce kullanarak galaksideki total baglantı sayısını hesaplar"""
    baglantilar = galaksi["baglantilar"]
    return reduce(
        lambda acc, g: acc + len(baglantilar.get(g, [])),
        galaksi["gezegenler"],
        0,
    )

def toplam_baglanti_sum(galaksi: dict[str, Any]) -> int:
    """sum kullanarak galaksideki toplam baglanti sayisini hesaplar"""
    baglantilar = galaksi["baglantilar"]
    return sum(len(baglantilar.get(g, [])) for g in galaksi["gezegenler"])

# functools.partial ile hiz=3 sabitlenmiş hizli_yolculuk fonksiyonu
def yolculuk(hedef: str, mesafe: int, hiz: int = 1) -> float:
    """Verilen hedefe belirtilen mesafe ve hızla ulaşma süresini döndürür."""
    return mesafe / hiz

hizli_yolculuk = partial(yolculuk, hiz=3)

if __name__ == "__main__":
    from uzay_oyunu.oyun import harita_yukle

    g = harita_yukle()
    print(buyuk_harfli_gezegenler_lc(g))
    print(en_az_iki_baglantili_lc(g))
    print(toplam_baglanti_sum(g))
    print("Normal yolculuk (mesafe=30):", yolculuk("sirius", 30))
    print("Hızlı yolculuk (mesafe=30, hiz=3):", hizli_yolculuk("sirius", 30))