from collections.abc import Callable
from typing import Any

from uzay_oyunu.oyun import envanter_metni

# komutları (fonksiyon, aciklama) çifti olarak tutan kayıt sözlüğü
KOMUTLAR: dict[str, tuple[Callable[[dict[str, Any]], str], str]] = {}


def komut(
    ad: str, aciklama: str = ""
) -> Callable[[Callable[[dict[str, Any]], str]], Callable[[dict[str, Any]], str]]:
    """Fonksiyonu değiştirmeden KOMUTLAR sözlüğüne (fonksiyon, aciklama) olarak kaydeder."""

    def kaydet(
        fonksiyon: Callable[[dict[str, Any]], str],
    ) -> Callable[[dict[str, Any]], str]:
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayıtlı!")
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon

    return kaydet


@komut("yardim", "komutları listeler")
def yardim(durum: dict[str, Any]) -> str:
    """Kayıtlı tüm komutları ve açıklamalarını alfabetik sırayla döndürür."""
    satirlar = [
        f"{ad:<10} {aciklama}" for ad, (_, aciklama) in sorted(KOMUTLAR.items())
    ]
    return "\n".join(satirlar)


@komut("envanter", "eşyalarını gösterir")
def envanter(durum: dict[str, Any]) -> str:
    """Oyuncunun sahip olduğu eşyaları döndürür."""
    return envanter_metni(
        credits=durum.get("credits", False),
        engines=durum.get("engines", False),
        copilot=durum.get("copilot", False),
    )


@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum: dict[str, Any]) -> str:
    """Mevcut konumdan gidilebilecek gezegenleri virgülle ayrılmış olarak döndürür."""
    konum = durum["konum"]
    hedefler = durum["baglantilar"].get(konum, [])
    return ", ".join(hedefler)