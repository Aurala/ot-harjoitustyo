# Arkkitehtuuri

```mermaid
classDiagram
    UI "1" -- "1" OutomaattiService
    Universe "1" -- "1" OutomaattiService
    OutomaattiService "1" -- "1" LibraryRepository
    LibraryRepository "1" -- "1" Library
    Library "1" -- "*" Pattern
    Library "1" -- "*" Category
    Library "1" -- "*" Rules
    Ruleset "*" -- "1" OutomaattiService
    CustomRuleset "1" --|> "1" Ruleset
```

Kommentti liittyen luokkakaavioon: UI-luokassa oleva toteutus on tarkoitus jakaa useampaan alaluokkaan (mm. Menu, Visualization), mutta tämä edellyttää tarkempaa perehtymistä Pygameen viimeisten viikkojen aikana.

Oheinen sekvenssikaavio kuvaa mitä tapahtuu kun käyttäjä sovelluksen avattuaan painaa Play-nappia. Tässä vaiheessa:
- UI on luonut OutomaattiService-olion.
- OutomaattiService-olio on luonut Universe-olion, joka kuvaa x*x-kokoista soluautomaattia.
- UI on lisännyt muutamia testikuvioita OutomaattiServiceä käyttäen Universeen.


```mermaid
sequenceDiagram
    Käyttäjä->>+UI: painaa Play-nappia
    UI->>UI: is_simulation_running=True
    UI->>UI: change_button_states(True)
    UI->>+OutomaattiService: next_generation()
    OutomaattiService->>+CustomRuleset: calculate(Universe)
    CustomRuleset->>+Universe: get_entire_universe_as_ndarray()
    Universe-->>-CustomRuleset: ndarray
    CustomRuleset->>CustomRuleset: laskenta
    CustomRuleset->>Universe: set_entire_universe_as_ndarray(new_universe)
    CustomRuleset-->>-OutomaattiService: 
    OutomaattiService-->>-UI: 
    UI->>+OutomaattiService: get_universe_as_ndarray()
    OutomaattiService->>+Universe: get_universe_as_ndarray()
    Universe-->>-OutomaattiService: ndarray
    OutomaattiService-->>-UI: ndarray
    UI->>-UI: renderöinti
```

Olen pitänyt tähän asti yhden sukupolven laskennan ja sen hakemisen renderöitäksi erillisinä toimintoina. Tämän voisi toki muuttaa niin, että data palautetaan next_generation()-kutsussa.

OutomaattiService voisi ehkä myös välittää ndarray:n laskentaa hoitavalle luokalle (ja takaisin). Ajatus oli, että tulevaisuuden CustomRuleset-luokissa olisi sellaista monimutkaista toiminnallisuutta, joka vaatisi pääsyä Universe-luokan metodeihin.
