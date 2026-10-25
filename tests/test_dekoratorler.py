import pytest
from uzay_oyunu.dektoratorler import sure_olc


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
    assert ornek_hesap.__doc__ == "Verilen tabanın üssünü hesaplar."