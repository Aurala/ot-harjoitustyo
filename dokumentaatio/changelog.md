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
- Font Awesome -fontti lisätty, jotta saadaan tyylikkäitä ikoneita menun nappeihin
- Tietokannan luova koodi tehty, oma taski (initdb)
- Koodia refaktoroitu ja formatoitu automaattisesti ja käsin linttausvirheiden poistamiseksi
- Pientä optimointia siellä ja täällä isojen solumäärien käsittelyyn
