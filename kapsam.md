# kapsam ve kurallar

## örnek 1
```python
yakit = 100

def yolculuk():
    yakit = 80
    print("İç:", yakit)

yolculuk()
print("Dış:", yakit)

iç 80 dış 100 tahmin

gerçek 80 iç 100 dış

yakıt = 80 ifadesi localde fonksiyon icinde kalıcak cünkü


#örnek 2 
def dis():
    konum = "dünya"
    def ic():
        konum = "mars"
        print("İç:", konum)
    ic()
    print("Dış:", konum)

dis()

tahmin iç mars dış dünya

sonuç iç mars dış dünya

en içteki fonksiyonda yapılan atama orda kalır


#örnek 3 
yakit = 100

def harca():
    print(yakit)
    yakit = yakit - 10

harca()

tahmin localunbounderror

sonuç UnboundLocalError: cannot access local variable 'yakit' 

python localde atanmış bi değer var oluşuna ragmen fonksiyon öncesinde okuma yaptıgı icin localde deger gözükmez ve UnboundLocalError verir

