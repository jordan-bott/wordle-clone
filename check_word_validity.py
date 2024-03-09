import requests


def check_word_validity(word):
    if len(word) != 5:
        return False
    else:
        dict_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        dict_json = dict_response.json()
        if not isinstance(dict_json, list):
            return False
        else:
            return True
