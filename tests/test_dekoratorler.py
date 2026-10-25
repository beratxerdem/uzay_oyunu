import pytest
from uzay_oyunu.dekoratorler import log_cagri, say, sure_olc, yakit_harca
from functools import lru_cache
from uzay_oyunu.komutlar import KOMUTLAR, envanter, harita, komut, yardim

@sure_olc
def ornek_hesap(taban: int, us: int = 2) -> int:
    """verilen tabanın üstünü hesaplar"""
    return taban**us


def test_sure_olc_sonuc_korunuyor(capsys: pytest.CaptureFixture[str]) -> None:
    """dekoratörün fonksiyon sonucunu değiştirmeden döndürdüğünü ve süreyi yazdırdığını test eder."""
    assert ornek_hesap(5) == 25
    cikti = capsys.readouterr().out
    assert "ornek_hesap:" in cikti
    assert "sn" in cikti

def test_sure_olc_adli_argumanlar() -> None:
    """Dekoratörün adlı argümanlarla (kwargs) doğru çalıştığını test eder."""
    assert ornek_hesap(taban=3, us=4) == 81

def test_sure_olc_isim_ve_doc_korunuyor() -> None:
    """functools.wraps sayesinde __name__ ve __doc__ niteliklerinin korunduğunu test eder."""
    assert ornek_hesap.__name__ == "ornek_hesap"
    assert ornek_hesap.__doc__ == "verilen tabanın üstünü hesaplar"


def test_say_ve_dekorator_sirasi() -> None:
    """say dekoratörünün üç farklı fibonacci tanımında doğru çağrı sayılarını verdiğini test eder."""

    @say
    def fib1(n: int) -> int:
        return n if n < 2 else fib1(n - 1) + fib1(n - 2)

    @say
    @lru_cache(maxsize=None)
    def fib2(n: int) -> int:
        return n if n < 2 else fib2(n - 1) + fib2(n - 2)

    @lru_cache(maxsize=None)
    @say
    def fib3(n: int) -> int:
        return n if n < 2 else fib3(n - 1) + fib3(n - 2)

    assert fib1(20) == 6765
    assert fib2(20) == 6765
    assert fib3(20) == 6765

    assert fib1.cagri == 21891  # type: ignore[attr-defined]
    assert fib2.cagri == 39  # type: ignore[attr-defined]
    assert fib3.__wrapped__.cagri == 21  # type: ignore[attr-defined]


def test_log_cagri(capsys: pytest.CaptureFixture[str]) -> None:
    """log_cagri dekoratörünün giriş argümanlarını ve dönüş değerini doğru yazdırdığını test eder."""

    @log_cagri
    def yolculuk(hedef: str, hiz: int = 1) -> str:
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)
    assert sonuc == "orion hiz=3"

    cikti = capsys.readouterr().out
    assert "-> yolculuk('orion', hiz=3)" in cikti
    assert "<- yolculuk 'orion hiz=3'" in cikti


def test_komut_kayit_ve_cift_isim_hatasi() -> None:
    """komut dekoratörünün fonksiyonu değiştirmeden kaydettiğini ve çift isimde ValueError verdiğini test eder."""
    assert "yardim" in KOMUTLAR
    assert "envanter" in KOMUTLAR
    assert "harita" in KOMUTLAR

    #aynı ad iki kez kullanılırsa tanım anında ValueError döndürür
    with pytest.raises(ValueError):

        @komut("yardim", "tekrar tanımlama denemesi")
        def sahte_yardim(durum: dict) -> str:
            return ""


def test_yardim_komutu() -> None:
    """yardim komutunun tüm komutları ve açıklamalarını listelediğini test eder."""
    sonuc = yardim({})
    assert "envanter" in sonuc and "eşyalarını gösterir" in sonuc
    assert "harita" in sonuc and "gidebileceğin gezegenleri gösterir" in sonuc
    assert "yardim" in sonuc and "komutları listeler" in sonuc


def test_envanter_komutu() -> None:
    """envanter komutunun oyuncu durumuna göre doğru metni döndürdüğünü test eder."""
    durum_bos = {"credits": False, "engines": False, "copilot": False}
    assert envanter(durum_bos) == ""

    durum_dolu = {"credits": True, "engines": True, "copilot": False}
    sonuc = envanter(durum_dolu)
    assert "bol kredi" in sonuc
    assert "hiperdrive" in sonuc


def test_harita_komutu() -> None:
    """harita komutunun mevcut konumdaki bağlantıları virgülle ayırarak döndürdüğünü test eder."""
    durum = {
        "konum": "sirius",
        "baglantilar": {"sirius": ["orion", "dünya", "kara_delik"]},
    }
    assert harita(durum) == "orion, dünya, kara_delik"

def test_sinirla_dekoratoru_sinir_degerler() -> None:
    """sınır değerlerinin (0 ve 100) ValueError döndürmedigini test eder."""
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0