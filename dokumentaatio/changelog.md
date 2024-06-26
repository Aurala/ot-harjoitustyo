# Viikko 3

- Alustettu projekti kurssila määritelyillä pakollisilla riippuvuuksilla
- Lisätty riippuvuuksia: Pygame, Numpy, Dynaconf
- Tehty toteutus Universe-luokasta, jossa tieto soluista sekä metodit niiden käsittelyyn
- Tehty minimaalinen Outomaatti-service, jossa käyttöliittymien tarvitsemat palvelut
- Rakennettu kaksi ei-interaktiivista tekstipohjaista käyttöliittymää ja yksi ei-interaktiivinen graafinen käyttöliittymä, joilla varmistettu, että sovellus osaa ladata dynaamisesti ja suorittaa eri luokista eri sääntöjä toteuttavia funktioita oikein
- Tehty kattavat taskit sovelluksen ja testien ajamiseen sekä testiraporttien generoimiseen
- Toteutettu automaattitestejä Universe-luokalle ja Outomaatti-servicelle
- (Aloitettu raakile Pattern-luokasta ja -repositorystä - ei kuitenkaan vielä käytössä)
- (Aloitettu väsäämään tietokantaa luovaa koodia - ei kuitenkaan vielä käytössä)

# Viikko 4

- Vaihdettu Pygame Community Editioniin
- Lisätty Pygame-menu -kirjasto käyttöliittymän valikoiden rakentamiseen (kokeiltu ensin Pygame GUI -kirjastoa, mutta osoittautui rikkinäiseksi ainakin omassa kehitysympäristössäni)
- Käyttöliittymään lisätty status-palkki ja menu oikeaan reunaan
- Käyttöliittymän napeista toimii play, pause, clean, exit, mutta nappien tilat (active/deactive) eivät päivity (vielä)
- Käyttäjä voi piirtää soluja ruudulle simulaation ollessa pysäytettynä
- Käyttäjä voi poistaa soluja ruudulta simulaation ollessa pysäytettynä
- Font Awesome -fontti lisätty, jotta saadaan tyylikkäitä ikoneita menun nappeihin
- Tietokannan luova koodi tehty, oma taski (initdb)
- Ylimääräisten tiedostojen poistoon tehty taski (clean), jota varten asennettu Pyclean
- Koodia refaktoroitu ja formatoitu, automaattisesti ja käsin, linttausvirheiden poistamiseksi (< 10 virhettä)
- **Käytössä olevien luokkien** haarautumakattavuus > 20%
- Optimointia isojen solumäärien käsittelyä varten

# Viikko 5

- Käyttöliittymän toiminnallisuutta kasvatettu
- Kasvaneesta toiminnallisuudesta huolimatta, erilaisten kontrollien määrää vähennetty
- Toimivia nappeja:
    - Play/pause
    - Trash
    - Snapshot
    - Exit
- Käyttöliittymän nappien tilat päivittyvät sen mukaan onko simulaatio käynnissä vai ei
- Suurempi määrä asetuksia (outomaatti.toml)
- Koodia refaktoroitu ja formatoitu, automaattisesti ja käsin, linttausvirheiden poistamiseksi (< 5 virhettä)
- **Käytössä olevien luokkien** haarautumakattavuus > 40%

# Viikko 6

- RLE-muodossa olevien kuvioiden tuonti sovellukseen toteutettu
    - Käyttöliittymän import-nappi ei vielä toimi
    - Tietokannan luova skripti populoi tietokantaan joukon kategorioita ja tuo niihin RLE-kuvioita määritellyistä tiedostoista data-kansiossa
- Frames per second -laskuri toteutettu
- Random-nappi toteutettu (lisää satunnaisia kuvioita kanvaasille)
- Suurempi määrä asetuksia (outomaatti.toml)
- DocStringit lähes kaikissa luokissa
- Koodia refaktoroitu ja formatoitu, automaattisesti ja käsin, linttausvirheiden poistamiseksi (< 5 virhettä)
- Luokkien haarautumakattavuus > 60% (paitsi luokka HighLife, jota ei ajeta ellei erikseen konffata Lifen tilalle)
- Alustavat käyttöohjeet ja arkkitehtuurikuvaus

# Viikko 7 (loppupalautus)

- UI-koodi refaktoroitu pienempiin kokonaisuuksiin (komponentteihin)
- Konfirmaatiodialogeja toiminnallisuuksissa
- Info-toiminnallisuus toteutettu
- Next-toiminnallisuus toteutettu
- Joka kuviokategoriaan lisätty valmiiksi määritettyjä kuvioita
- Nopeusvalinta toteutettu
- Asetukset-valikko totetettu
- Omien kuvioiden tuominen sovellukseen drag & dropilla toteutettu
- Testikattavuutta lisätty
- DocStringit lisätty kaikkiin luokkiin ja funktioihin
- Koodia siistitty
- Kattava testaus suoritettu
- Kattava vertailu arviointikriteereihin suoritettu
- Dokumentaatiota lisätty vaatimusten mukaisesti
