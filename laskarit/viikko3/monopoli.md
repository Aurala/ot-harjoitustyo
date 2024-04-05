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
    Ruutu "1" <|-- "3" Sattuma
    Sattuma "1" -- "1" SattumaKortti : päällimmäinen kortti 16 kortin pinosta (satunnaisjärjestys)
    SattumaKortti : jokuToiminto()*
    Ruutu <|-- "3" Yhteismaa
    Yhteismaa "1" -- "1" YhteismaaKortti : päällimmäinen kortti 16 kortin pinosta (satunnaisjärjestys)
    YhteismaaKortti : jokuToiminto()*
    Aloitusruutu : jokuToiminto()*
    Aloitusruutu : sijainti
    Ruutu <|-- "1" Vankila
    Vankila : jokuToiminto()*
    Vankila : sijainti
    Ruutu <|-- "4" Asema
    Asema : jokuToiminto()*
    Ruutu <|-- "2" Laitos
    Laitos : jokuToiminto()*
    Ruutu <|-- "24" Katu
    Katu : nimi
    Katu : jokuToiminto()*
    Katu "1" -- "0..4" Talo
    Katu "1" -- "0..1" Hotelli
    Talo .. Hotelli : JOKO TAI (neljä taloa voi poistaa ja rakentaa tilalle hotellin)
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "0..1" -- "1" Katu
    Pelaaja : rahaa
```

Erilaisten ruutujen ja niihin liittyvien korttien lukumääriä osoittavissa merkinnöissä epävarmuutta. Toivottavasti meni edes jokseenkin oikein.