def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> str:
    """Görev başlığını, adımlarını, önceliğini ve ek bilgileri metin olarak döndürür."""
    satirlar = [f"[{oncelik.upper()}] {baslik}"]
    for i, adim in enumerate(adimlar, start=1):
        satirlar.append(f"{i}. {adim}")
    for anahtar, deger in ekler.items():
        satirlar.append(f"{anahtar}: {deger}")
    return "\n".join(satirlar)


if __name__ == "__main__":
    #doğrudan argümanlarla çağrı
    print(gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe",
    ))
    print("-" * 30)
    #Liste (*) ve sözlük (**) açarak çağrı
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"oncelik": "yüksek", "sorumlu": "Ayşe"}
    print(gorev_kaydi("Kara deliğe atla", *adim_listesi, **ek_bilgiler))