dekoratör sırası ve çağrı sayılarını açıklar:


kendini tekrar eden fib(20) fonksiyonu 3 farklı dektörator dizlimiyle çalıştırıldığında elde edilen çağrı miktarları{

    yalnızca @say: 21891
    @say üstte @lru_cache altta iken: 39
    @lru cache üstte @say altta iken: 21

}

farklı sonucların cıkmasının sebebi ise sadece @say kullanırken önbellekleme yapılmayışı dolayısıyla bütün kodun tekrar edişi

@say üstte @lru cache altta iken 39 cıkması ise dekoratörlerin içten dışa doğru cıkması yani çağrılar
ilk önce @saydan geçer ardından cache'ce kontrol edilir sonuç olarak önbellekte bulunsa bile @say'a girdigi icin sayac artar 2-20 aralıgındaki 19 dügümün hepsi 2 alt cagrı yaptıgı icin ve en başta 1 ana çağrı olduguna göre 1+19*2 den 39 çağrı sayılır

@lru cache üstteyken en dışta bulunduğu icin önbellekteki hic bir sayı tekrar çağırılmaz
dolayısıyla sadece 0 dan 20 ye kadar olan 21 farklı sayı ilk kez hesaplanırken çağırılır.
