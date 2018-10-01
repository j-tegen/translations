## Translations

### Installation ###
- Install dependencies with `pip install -r requirements.txt` in a python environment of your choice.
- Follow the instructions to set up a service account and create a key file at https://cloud.google.com/translate/docs/quickstart-client-libraries
- Create a _source.json_ file in the root directory and configure according to below

As of right now (2018-10-01) the texts will be translated into the following languages:
- Swedish
- Danish
- Norwegian
- Finnish
- German
- French
- Thai
- Polish
- Spanish
- Italian

To add more languages, simply modify the list `TARGETS`.

### Configuration ###
The source.json file should contain a list with english texts that you want translated:
```
[
    "First text",
    "Second text",
    "Third text"
]

```
This is a JSON file and not a js file, and must thus use double quots and no trailing commas.

### Result ###

Result will be a JSON file called _result.json_ with the following structure:
```
{
    "en": {
        "First text": "First text",
        "Second text": "Second text",
        "Third text": "Third text"
    },
    "sv": {
        "First text": "Första texten",
        "Second text": "Andra texten",
        "Third text": "Tredje texten"
    },
    "da": {
        "First text": "Første tekst",
        "Second text": "Andet tekst",
        "Third text": "Tredje tekst"
    },
    "no": {
        "First text": "Første tekst",
        "Second text": "Andre tekst",
        "Third text": "Tredje tekst"
    },
    "fi": {
        "First text": "Ensimmäinen teksti",
        "Second text": "Toinen teksti",
        "Third text": "Kolmas teksti"
    },
    "de": {
        "First text": "Erster Text",
        "Second text": "Zweiter Text",
        "Third text": "Dritter Text"
    },
    "fr": {
        "First text": "Premier texte",
        "Second text": "Deuxième texte",
        "Third text": "Troisième texte"
    },
    "th": {
        "First text": "ข้อความแรก",
        "Second text": "ข้อความที่สอง",
        "Third text": "ข้อความที่สาม"
    },
    "pl": {
        "First text": "Pierwszy tekst",
        "Second text": "Drugi tekst",
        "Third text": "Trzeci tekst"
    },
    "es": {
        "First text": "Primer texto",
        "Second text": "Segundo texto",
        "Third text": "Tercer texto"
    },
    "it": {
        "First text": "Primo testo",
        "Second text": "Secondo testo",
        "Third text": "Terzo testo"
    }
}
```