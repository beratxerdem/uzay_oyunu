def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Verilen miktarı yakıt deposuna ekler. None kalıbıyla mutable default argüman tuzağını önler."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle_tuzagi() -> None:
    """yakit_ekle fonksiyonunun her varsayılan çağrıda yeni bir liste oluşturduğunu doğrular."""
    birinci = yakit_ekle(10)
    assert birinci == [10]

    ikinci = yakit_ekle(20)
    assert ikinci == [20]