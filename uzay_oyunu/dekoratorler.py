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

def say(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """fonksiyonun kaç kez çağrıldığını .cagri şeklinde sayan dekoratör."""

    @wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        sarmalayici.cagri += 1  # type: ignore[attr-defined]
        return fonksiyon(*args, **kwargs)

    sarmalayici.cagri = 0  # type: ignore[attr-defined]
    return sarmalayici



def log_cagri(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """Her çağrıdan önce fonksiyon adını/argümanlarını, sonra dönüş değerini yazdırır."""

    @wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        konumsal = [repr(a) for a in args]
        adli = [f"{k}={v!r}" for k, v in kwargs.items()]
        tum_argumanlar = ", ".join(konumsal + adli)

        print(f"-> {fonksiyon.__name__}({tum_argumanlar})")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"<- {fonksiyon.__name__} {sonuc!r}")
        return sonuc

    return sarmalayici

if __name__ == "__main__": #uzun süre beklememek için yorum satırı olarak tutuluyor.
    #from uzay_oyunu.akis import onbelleksiz_rota_sayaci
    #from uzay_oyunu.oyun import harita_yukle

    #galaksi = harita_yukle()
    #onebelleksiz rotaya sure dekoratoru uygulanıyor

    #say = sure_olc(onbelleksiz_rota_sayaci(galaksi["baglantilar"]))
    #print("Önbelleksiz rota sayacı (adim = 20) hesaplanıyor....")
    #sonuc = say("dünya", 20)
    #print(f"Sonuç: {sonuc}")

    #görev 2 gösterimi

    from functools import lru_cache

    @say
    def fib_sadece_say(n: int) -> int:
        return n if n < 2 else fib_sadece_say(n - 1) + fib_sadece_say(n - 2)

    @say
    @lru_cache(maxsize=None)
    def fib_say_ustte(n: int) -> int:
        return n if n < 2 else fib_say_ustte(n - 1) + fib_say_ustte(n - 2)

    @lru_cache(maxsize=None)
    @say
    def fib_cache_ustte(n: int) -> int:
        return n if n < 2 else fib_cache_ustte(n - 1) + fib_cache_ustte(n - 2)

    fib_sadece_say(20)
    fib_say_ustte(20)
    fib_cache_ustte(20)

    print("yalnızca @say                :", fib_sadece_say.cagri)
    print("@say üstte, @lru_cache altta :", fib_say_ustte.cagri)
    print("@lru_cache üstte, @say altta :", fib_cache_ustte.__wrapped__.cagri)


def sinirla(alt: int | float, ust: int | float) -> Callable[..., Any]:
    """dekore edilen fonksiyonun ilk argümanı [alt, ust] aralığında değilse ValueError döndürür"""

    def dekorator(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(fonksiyon)
        def sarmalayici(*args: Any, **kwargs: Any) -> Any:
            if args:
                ilk_deger = args[0]
                if not (alt <= ilk_deger <= ust):
                    raise ValueError(
                        f"{fonksiyon.__name__}: {ilk_deger} değeri {alt}-{ust} aralığında değil"
                    )
            return fonksiyon(*args, **kwargs)

        return sarmalayici

    return dekorator

@sinirla(0, 100)
def yakit_harca(miktar: int) -> int: #testlerde cagırabilmek icin burda kullanacğaım.
    """verilen miktar kadar yakıt harcar ve kalan yakıtı döndürür."""
    baslangic_yakit = 100
    return baslangic_yakit - miktar