## Monopoli-pelin luokkakaavio

Lisätietoja harjoituksen tekemiseen löytyi:
- [Wikipediasta](http://fi.wikipedia.org/wiki/Monopoli_(peli))
- [Hasbron sivuilta löytyneestä sääntökirjasta](https://www.hasbro.com/common/documents/430e4f3f6bfd10148a8ef35124427085/D5C22B4250569047F56E08937DF18AB2.pdf)


```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" <|-- "1" Aloitusruutu
    Ruutu "1" <|-- Sattuma
    Sattuma -- SattumaKortti
    SattumaKortti : * toiminto()
    Ruutu "1" <|-- Yhteismaa
    Yhteismaa -- YhteismaaKortti
    YhteismaaKortti : * toiminto()
    Aloitusruutu : * toiminto()
    Aloitusruutu : sijainti
    Ruutu "1" <|-- Vankila
    Vankila : * toiminto()
    Vankila : sijainti
    Ruutu <|-- Asema
    Asema : * toiminto()
    Ruutu "1" <|-- Laitos
    Laitos : * toiminto()
    Ruutu "1" <|-- Katu
    Katu : nimi
    Katu : * toiminto()
    Katu -- "0..4" Talo
    Katu -- "0..1" Hotelli
    Talo .. Hotelli : JOKO TAI (neljä taloa voi poistaa ja rakentaa tilalle hotellin)
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja -- Katu
    Pelaaja : rahaa
```
