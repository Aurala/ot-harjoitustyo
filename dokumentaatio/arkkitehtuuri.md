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

- Oheinen luokkakaavio kuvastaa meneillään olevan refaktoroinnin jälkeistä tilannetta. Viikon 4 arviointia tehtäessä näitä muutoksia voi tarkastella branchissa ["viikko5"](https://github.com/Aurala/ot-harjoitustyo/tree/viikko5).
- UI-luokassa oleva toteutus on tarkoitus jakaa useampaan alaluokkaan (mm. Menu, Visualization), mutta tämä edellyttää tarkempaa perehtymistä Pygameen.
