# Aineopintojen harjoitustyö: ohjelmistotekniikka, kevät 2024

[Kurssisivu](https://ohjelmistotekniikka-hy.github.io/)

## Harjoitustyö: Outomaatti

Outomaatti-sovellus toteuttaa [soluautomaatin](https://fi.wikipedia.org/wiki/Soluautomaatti). Oletusarvoina sovelluksessa on John Conway'n kehittämän [Game of Lifen](https://fi.wikipedia.org/wiki/Game_of_Life) säännöt (B3/S23), mutta sovellus tarjoaa käyttäjälle mahdollisuuden käyttää erilaisia sääntöjä.

Sovellusta voidaan käyttää viihdyttävänä ajanvietteenä tai opetuskäytössä, esimerkiksi innostamaan lapsia matematiikan opiskeluun tai jopa tuottamaan Python-koodia (omien sääntöjen kirjoittaminen).

## Toimintaympäristöstä

Testatut ympäristöt:
- macOS 14.4.1 (Apple Silicon)
- Helsingin yliopiston Cubbli Linux -virtuaalikoneet

Riippuvuuksien puolesta sovellus toimii Python-versioilla 3.8-3.11. Kehityksessä ja testauksessa on ollut käytössä pääasiassa Python 3.10.

## Lataa ja kokeile

Koodikatselmointiin tarkoitettu release löytyy [täältä](https://github.com/Aurala/ot-harjoitustyo/releases/tag/Viikko5).

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- Testausdokumentti
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

## Komentorivitoiminnot

### Asennus

Kun projekti on kopioitu haluttuun paikkaan, siirrytään koodin sisältävään hakemistoon ja ajetaan komento:

```
poetry install
```

Komento virtuaaliympäristön ja lataa tarvittavat riippuvuudet.

Poetryn asennusohjeet löytyvät [täältä](https://python-poetry.org/docs/#installing-with-the-official-installer).

### Käynnistys

Ohjelma käynnistyy komennolla:

```
poetry run invoke start
```

Käyttöliittymän toteutus on vielä kesken ja kaikki sen sisältämät kontrollit eivät toimi. Toimivaa mm.:

- Play/Pause
- Solujen poisto
- Solujen piirtäminen ja poistaminen hiirellä
- Snapshot (kirjoittaa tiedostoon PNG-kuvan simulaatiosta)
- Exit

Vaihtoehtoisesti käyttäjä voi käynnistää tekstimuotoisen käyttöliittymän komennoilla:

```
poetry run invoke life
```

tai

```
poetry run invoke highlife
```

Erona komennoissa on se, että ensimmäinen käyttää oletusarvoisia sääntöjä (B3/S23) ja jälkimmäinen nk. Highlife-sääntöjä (B36/S23). Sovellus lataa säännöt toteuttavat funktiot dynaamisesti eri luokista.

### Testaus

Koodin laatua mittaava testi ajetaan komennolla:

```
poetry run invoke lint
```

Automaattitestit suoritetaan komennolla:

```
poetry run invoke test
```

Testiraportti generoidaan komennolla:

```
poetry run invoke coverage
```

Tai jos käyttäjä haluaa HTML-muotoisen testiraportin, joka tallentuu projektin juureen hakemistoon 'htmlcov', niin komento on:

```
poetry run invoke coverage-report
```

### Muuta

Erilaisten työkalujen luomat työtiedostot ja cache-tiedostot voidaan poistaa komennolla:

```
poetry run invoke clean
```
