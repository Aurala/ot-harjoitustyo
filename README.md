# Aineopintojen harjoitustyö: ohjelmistotekniikka, kevät 2024

[Kurssisivu](https://ohjelmistotekniikka-hy.github.io/)

## Harjoitustyö: Outomaatti

Outomaatti-sovellus toteuttaa [soluautomaatin](https://fi.wikipedia.org/wiki/Soluautomaatti). Oletusarvoina sovelluksessa on John Conway'n kehittämän [Game of Lifen](https://fi.wikipedia.org/wiki/Game_of_Life) säännöt (B3/S23), mutta sovellus tarjoaa mahdollisuuden sääntöjen parametrien muuttamiseen.

Sovellusta voidaan käyttää viihdyttävänä ajanvietteenä tai opetuskäytössä, esimerkiksi innostamaan lapsia matematiikan opiskeluun tai jopa tuottamaan Python-koodia (omien sääntöjen kirjoittaminen).

## Toimintaympäristöstä

...

## Dokumentaatio

- Käyttöohje
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- Arkkitehtuurikuvaus
- Testausdokumentti
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

## Komentorivitoiminnot

### Käynnistys

Ohjelma käynnistyy komennolla:

```
poetry run invoke start
```

HUOMIO: Käyttöliittymän toteutus on vielä alkutekijöissään eikä siinä ole toiminnallisuutta. Sovellus ajaa Game of Life -sääntöjä 100x100-ruudussa määritellyille kuvioille kunnes käyttäjä sulkee sovellusikkunan.

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

Automaattitestit suoritetaan komennolla:

```
poetry run invoke test
```

Testiraportti generoidaan komennoilla:

```
poetry run invoke coverage
poetry run invoke coverage-report
```

Jälkimmäinen komento tuottaa HTML-muotoisen raportin, joka tallentuu projektin juureen hakemistoon 'htmlcov'.
