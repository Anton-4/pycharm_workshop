# PyCharm Workshop

Bij deze workshop gebruiken we een bijna opgelost porbleem van de vlaamse programmeerwedstrijd 2010 genaamd bloedgroepen.

## Bloedgroepen
Het bloed van elke persoon heeft twee markers die ABO allelen genoemd worden.
Elk van deze markers wordt voorgesteld door een van drie letters:
A, B of O. Hierdoor kan elke persoon een van zes mogelijke combinaties van
deze allelen hebben, die elk resulteren in een bepaalde ABO bloedgroep voor
deze persoon zoals aangegeven in de tabel hieronder:


| kruising | ABO bloedgroep |
| -------- | -------------- |
| A en A   | A		    |
| A en B   | AB             |
| A en O   | A              |
| B en B   | B              |
| B en O   | B              |
| O en O   | O              |

Volledig analoog heeft het bloed van elke persoon twee allelen voor de rhe-
susfactor. Deze rhesusfactor wordt voorgesteld door de lettertekens
+ en -. Een persoon die rhesuspositief is, heeft ten minste een +
allel maar kan er ook twee hebben. Iemand die rhesusnegatief is, heeft altijd twee
- allelen.
Dit wordt geıllustreerd in de rechtse tabel hierboven.

| kruising | rhesusfactor   |
| -------- | -------------- |
| + en +   | +              |
| + en -   | +              |
| - en -   | -              |

De bloedgroep van een persoon wordt bepaald door de combinatie van de
ABO bloedgroep en de rhesusfactor. Deze bloedgroep wordt genoteerd door
de lettercombinatie van de ABO bloedgroep te laten volgen door een plus-
of minteken dat de rhesusfactor voorstelt. Voorbeelden zijn
A+, AB- en O-.

Bloedgroepen worden overgeerfd: elke biologische ouder geeft een ABO allel
(willekeurig gekozen uit de twee aanwezige allelen) en een rhesusallel door
aan zijn of haar kind. Op die manier bepalen de 2 ABO allelen en 2 rhe-
susallelen van de ouders de bloedgroep van het kind.
Stel bijvoorbeeld dat beide ouders van een kind bloedgroep A-
hebben, dan kan het kind ofwel bloedgroep A- of bloedgroep O-
hebben. Een kind met ouders die bloedgroep A+ en B+
hebben kan elke mogelijke bloedgroep hebben.

### Opgave

Voor dit probleem krijg je telkens de bloedgroep van beide ouders of van een
ouder en zijn of haar kind. Op basis van deze gegevens moet je de (mogelijk
lege) verzameling bepalen van alle mogelijke bloedgroepen die het kind of
de andere ouder heeft.

**Opmerking:**
Bij dit probleem wordt de hoofdletter O gebruikt in de notatie
van bloedgroepen, en niet het cijfer 0 (nul).


#### Invoer
Het invoerbestand bevat n gevallen, en dit aantal staat aangegeven op de
eerste regel van het bestand. Elk geval staat op een afzonderlijke regel en
bevat de bloedgroep van een ouder, de bloedgroep van de andere ouder en
tenslotte de bloedgroep van het kind, behalve dat de bloedgroep van een
van de ouders of van het kind werd vervangen door een vraagteken (‘?’).
Bloedgroepen worden telkens van elkaar gescheiden door een enkele spatie.

#### Uitvoer
Voor elk geval in het invoerbestand moet de bloedgroep van beide ouders en
het kind worden afgedrukt op een afzonderlijke regel. Bloedgroepen worden
telkens van elkaar gescheiden door een enkele spatie.  Indien geen enkele
bloedgroep mogelijk is voor een ouder, dan moet daarvoor de tekenreeks
ONMOGELIJK worden afgedrukt. Indien meerdere bloedgroepen mogelijk zijn
voor een van beide ouders of voor het kind, dan moeten alle mogelijkheden
gescheiden door komma’s worden opgelijst, waarbij de volledige lijst tussen
openende en sluitende accolades (‘{’,‘}’) geplaatst wordt. Bloedgroepen
moeten in oplopende volgorde worden opgelijst, waarbij ABO bloedgroepen
alfabetisch gerangschikt worden en een plusteken voor een minteken wordt
gerangschikt.

### Voorbeeld

#### Invoer

5
O+ O- ?
O- O- ?
O+ ?  O-
AB- AB+ ?
AB+ ?  O+

#### Uitvoer

O+ O- {O+,O-}
O- O- O-
O+ {A-,A+,B-,B+,O-,O+} O-
AB- AB+ {A+,A-,AB+,AB-,B+,B-}
AB+ ONMOGELIJK O+
