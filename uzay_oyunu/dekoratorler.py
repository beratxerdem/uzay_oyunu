import time
from collections.abc import Callable
from functools import wraps
from typing import Any

def sure_olc(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """fonksiyonun calıstıgı süreyi ölcüm fonksiyon_adı:0.0123 sn seklinde belirtir."""

    @wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        print(f"{fonksiyon.__name__}: {bitis - baslangic:.4f} sn")
        return sonuc
    return sarmalayici

if __name__ == "__main__":
    from uzay_oyunu.akis import onbelleksiz_rota_sayaci
    from uzay_oyunu.oyun import harita_yukle

    galaksi = harita_yukle()
    #onebelleksiz rotaya sure dekoratoru uygulanıyor

    say = sure_olc(onbelleksiz_rota_sayaci(galaksi["baglantilar"]))
    print("Önbelleksiz rota sayacı (adim = 20) hesaplanıyor....")
    sonuc = say("dünya", 20)
    print(f"Sonuç: {sonuc}")