import json
from base_chars.models import Katakana, Hiragana

def kanaGanaSetup():
        gana_path = "base_chars/init_data/gana_data.json"
        kana_path = "base_chars/init_data/kana_data.json"

        with open(gana_path, 'r+') as json_file:
            dict_formatted_data = json.load(json_file)

            for obj in dict_formatted_data:
                Hiragana.objects.create(body=obj["fields"]["body"], 
                                        romaji=obj["fields"]["romaji"],
                                        group_num=obj["fields"]["group_num"])
            
        with open(kana_path, 'r+') as json_file:
            dict_formatted_data = json.load(json_file)

            for obj in dict_formatted_data:
                Katakana.objects.create(body=obj["fields"]["body"], 
                                        romaji=obj["fields"]["romaji"],
                                        group_num=obj["fields"]["group_num"])