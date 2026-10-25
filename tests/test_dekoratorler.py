import pytest
from uzay_oyunu.dekoratorler import sure_olc, say
from functools import lru_cache


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