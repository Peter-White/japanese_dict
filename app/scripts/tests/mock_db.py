import json
from base_chars.models import Hiragana, Katakana

g_path = "../../base_chars/init_data/gana_data.json"
k_path = "../../base_chars/init_data/kana_data.json"

def populate_gana():
    with open(g_path, 'r+') as json_file:
        dict_formatted_data = json.load(json_file)

        for gana in dict_formatted_data:
            romaji=gana["fields"]["romaji"]
            group_num=gana["fields"]["group_num"]
            body=gana["fields"]["body"]
        
            Hiragana.objects.create(group_num=group_num, romaji=romaji, body=body)

def populate_kana():
    with open(k_path, 'r+') as json_file:
        dict_formatted_data = json.load(json_file)

        for kana in dict_formatted_data:
            romaji=kana["fields"]["romaji"]
            group_num=kana["fields"]["group_num"]
            body=kana["fields"]["body"]
        
            Katakana.objects.create(group_num=group_num, romaji=romaji, body=body)

            