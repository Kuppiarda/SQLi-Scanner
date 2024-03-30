# SQLi Scanner 

Python ile geliştirilen SQL Enjeksiyonu Zafiyeti Tarayıcısı

## Özellikler

- Ziyaret edilen sayfanın **GET** ve **POST** methodlu formlarını tarama
- Sayfada bulunan linkleri taramaya dahil etme
    - Bulunan her linki dahil etme ya da aynı alan adına sahip linkleri dahil etme seçeneği
    - Taranacak URL'leri düzenli ifadeler([RegEx](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions "RegEx")) ile kısıtlama
- Çoklu **thread** kullanarak aynı anda birden çok sayfa tarama
- SQLi sorgularını ve tetikleyici uyarı mesajlarını metin belgelerinden düzenleme
- Zafiyetli olduğu düşünülen sayfaları otomatik olarak metin belgesine kaydetme

## Gereksinimler

- Windows işletim sistemi (Windows 10 sürümünde test edildi)
- Python 3.10 (3.10.6 sürümünde test edildi)
- [requirements.txt](https://github.com/Kuppiarda/SQLi-Scanner/blob/main/requirements.txt "requirements.txt")

## Kurulum

1. [Python 3.10.6](https://www.python.org/downloads/release/python-3106/ "Python 3.10.6") sürümünü kurun.
2. [git](https://git-scm.com/download/win "git") kurun. (Kurulum tercihine bağlı.)
3. `git clone https://github.com/Kuppiarda/SQLi-Scanner.git` komutu ile ya da manuel olarak proje dosyalarını indirin.
4. `pip install -r requirements.txt` komutu ile kütüphane gereksinimlerini kurun.

## Kullanım
1. `inputURLs.txt` klasörüne taramak istediğiniz URL'leri girin.
2. `Start.py` dosyasını çalıştırın ve yönergeleri takip edin.

## Sorgu Girdilerini ve Tetikleyici Mesajları Düzenleme

- SQLi sorgusunda kullanılacak girdileri `settings/query.txt` dosyasından değiştirebilirsiniz.
- Sorgunun dönüşünde taranmasını istediğiniz tetikleyici mesajları `settings/response.txt` dosyasından değiştirebilirsiniz.

## Kayıtları İnceleme

- Test edilen URL'leri `testedURLs.txt`, zafiyetli olabilecek URL'leri `vulnerableURLs.txt`, test edilecek URL'leri ise `inputURLs.txt` dosyasından takip edebilirsiniz.

## Son Söz

**Sadece koruma ve akademik amaçlı kullanınız.<br />**
**Use only for protection and academic purposes.**
