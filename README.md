# Web-Scrapping dengan Beautifulsoup untuk membuat visualisasi dan analysis pergerakan Data kurs US Dollar ke rupiah dari `https://www.exchange-rates.org/history/IDR/USD/T`

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. 


## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

Atau Bapak Ibu cukup menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```

## Rubics


## What You Need to Do

* Silahkan mencoba melakukan scraping soal di bawah menggunakan `beautiful soup` di notebook Bapak/Ibu terlebih dahulu.
* Bapak/Ibu dapat men-clone repo ini.
* Silahkan buka notebook template pada capstone ini dan isi sesuai dengan arahan yang ada. Pastikan Bapak/Ibu memberikan analisa yang dibutuhkan pada notebook tersebut.
* File di repo ini adalah skeleton yang dapat digunakan untuk membuat flask dashboard sederhana.
* Silahkan isi di bagian yang masih kosong.
* Isi fungsi `scrap` dengan proses scraping yang sudah Bapak/Ibu lakukan di notebook. 

```python
table = soup.find(___)
tr = table.find_all(___)
```

* Isi bagian ini untuk menyimpan hasil scrap yang Bapak/Ibu buat menjadi sebuah dataframe.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

* Terakhir Bapak/Ibu dapat menggunakan fungsi `scrap` dengan cara mengisi bagian berikut dengan link web yang Bapak/Ibu scrap.

```python
df = scrap(___) #insert url here
```

* Bapak/Ibu juga dapat bermain dengan UI nya pada `index.html` yang dimana Bapak/Ibu dapat mengikuti comment yang ada untuk mengetahui bagian mana yang dapat diubah. 




