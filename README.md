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

- [Koodikatselmointiin tarkoitettu release](https://github.com/Aurala/ot-harjoitustyo/releases/tag/Viikko5)
- [Viikon 6 palautus](https://github.com/Aurala/ot-harjoitustyo/releases/tag/Viikko6)
- [Loppupalautus](https://github.com/Aurala/ot-harjoitustyo/releases/tag/Loppupalautus)

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)
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

Seuraavaksi alustetaan tietokanta komennolla:

```
poetry run invoke build
```

### Käynnistys

Ohjelma käynnistyy komennolla:

```
poetry run invoke start
```

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
poetry run invoke coverage-report
```

Testit ajetaan tilapäistä testitietokantaa vasten.

### Muuta

Erilaisten työkalujen luomat työtiedostot, cache-tiedostot yms. voidaan poistaa komennolla:

```
poetry run invoke clean
```
