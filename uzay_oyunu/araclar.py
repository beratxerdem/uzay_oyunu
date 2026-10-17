import time
from typing import Any, Callable


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında 1 artan bir sayaç fonksiyonu (closure) döndürür."""
    sayac = 0

    def artir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return artir


def sure_olc(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """Verilen fonksiyonun çalışma süresini ölçüp yazdıran sarmalayıcı döndürür."""
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        print(f"{fonksiyon.__name__} süresi: {bitis - baslangic:.6f} sn")
        return sonuc

    return sarmalayici


def en_bagli_gezegenler(galaksi: dict[str, Any]) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür."""
    baglantilar = galaksi["baglantilar"]
    return sorted(
        galaksi["gezegenler"],
        key=lambda g: (-len(baglantilar.get(g, [])), g),
    )


if __name__ == "__main__":
    ornek_g = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "sirius": ["dünya", "centauri", "orion", "kara_delik"],
            "centauri": ["dünya", "sirius", "orion"],
            "dünya": ["centauri", "sirius"],
            "orion": ["centauri", "sirius"],
            "kara_delik": [],
        },
    }
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    print(en_bagli_gezegenler(ornek_g))