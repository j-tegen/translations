from google.cloud import translate
import os
import io
import json

client = translate.Client()

SOURCE_FILE_NAME = 'source.json'

TARGETS = [
    'sv',
    'da',
    'no',
    'fi',
    'de',
    'fr',
    'th',
    'pl',
    'es',
    'it',
]


def translate_texts():
    with open(SOURCE_FILE_NAME, 'r') as f:
        source = json.load(f)
        if not source:
            print('No source texts were supplied in source.json')
            return

        results = {}
        translations = {}
        for key in source:
            translations['%s' %(key)] = key

        results['en'] = translations

        for target in TARGETS:
            translations = {}
            for key in source:
                result = client.translate(
                    key,
                    target_language=target
                ).get('translatedText', None)

                if not result:
                    continue

                translations['%s' %(key)] = result
            results['%s' %(target)] = translations

        with io.open('results.json'.format(target), 'w', encoding='utf8') as output:
            json.dump(results, output, ensure_ascii=False)


if __name__ == "__main__":
    translate_texts()
