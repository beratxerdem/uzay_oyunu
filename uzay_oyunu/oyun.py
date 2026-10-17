import json
from pathlib import Path
from typing import Any
from uzay_oyunu.araclar import hamle_sayaci


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Eşya varsa 'Sende: ...' metnini, yoksa boş metin döndürür."""
    esyalar: list[str] = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("hiperdrive")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""
    return "Sende: " + ", ".join(esyalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Gezegen hedeflerini numaralı menü metni olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)


def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs: Any,
) -> dict[str, Any]:
    """Galaksi verisini doğrular ve oyun durumu sözlüğünü kurar."""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' listede yok!")

    yakit = kwargs.get("yakit", 50)
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }


def harita_yukle() -> dict[str, Any]:
    """galaksi.json dosyasını okur ve galaksi_kur ile sözlük döndürür."""
    dosya_yolu = Path(__file__).parent / "galaksi.json"
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        veri = json.load(f)
    return galaksi_kur(**veri)


def travel() -> None:
    """Uzay oyununun ana seyahat fonksiyonu (Görev 5 son hali)."""
    galaksi = harita_yukle()
    planet = galaksi["konum"]
    credits = False
    engines = False
    copilot = False

    sayac = hamle_sayaci()
    toplam_hamle = 0

    while True:
        print(f"\nŞu anki gezegen: {planet}")
        metin = envanter_metni(credits, engines, copilot)
        if metin:
            print(metin)

        if planet == "centauri":
            credits = True
        elif planet == "sirius":
            engines = True
        elif planet == "orion":
            copilot = True
        elif planet == "kara_delik":
            if credits and engines and copilot:
                print("Tebrikler! Oyunu kazandın!")
            else:
                print("Donanımın eksik, kara delikte kayboldun!")
            break

        destinations = galaksi["baglantilar"][planet]
        print(hedef_menusu(destinations))

        secim = input("Seçiminiz (çıkmak için 'q'): ")
        if secim == "q":
            break
        if secim.isdigit() and 1 <= int(secim) <= len(destinations):
            planet = destinations[int(secim) - 1]
            galaksi["konum"] = planet
            toplam_hamle = sayac()

    print(f"Oyunu {toplam_hamle} hamlede bitirdin!")

if __name__ == "__main__":
    travel()