from base_chars.models import Hiragana, Katakana
import re

def ref_fetch_gana(id):
    return Hiragana.objects.get(id)

def ref_fetch_kana(id):
    return Katakana.objects.get(id)

# def ref_fetch_particle(part):
#     return grab_by_id(part_path, part)

# def ref_fetch_kanji(kanji):
#     return ""

# def ref_fetch_word(word):
#     return ""

# def ref_fetch_reg(ref):
#     return re.search("^({)([a-z])(\\w+)(})$", ref)

# def ref_obj_create(id, sym, rom):
#     return {"id": id, "symbol": sym, "romaji": rom}

# def ref_fetch(ref):
#     try:
#         reg_groups = ref_fetch_reg(ref).groups()
#         ref_obj = {}

#         cat = reg_groups[1]
#         id = reg_groups[2]

#         match(cat):
#             case "h":
#                 fetch = ref_fetch_gana(id)
#                 return ref_obj_create(fetch["pk"], fetch["fields"]["symbol"], fetch["fields"]["romaji"])
#             case "k":
#                 fetch = ref_fetch_kana(id)
#                 return ref_obj_create(fetch["pk"], fetch["fields"]["symbol"], fetch["fields"]["romaji"])
#             case "p":
#                 fetch_part = ref_fetch_particle(id)
#                 fetch_gana = ref_fetch(fetch_part["fields"]["gana_ref"])

#                 return ref_obj_create(fetch_part["pk"], fetch_gana["symbol"], fetch_part["fields"]["romaji"])
#             case "j":
#                 return ref_fetch_kanji(id)
#             case _:
#                 return "Error: Invalid category"
#     except AttributeError:
#         return "Error: Incorrect RegEx pattern"
#     except TypeError:
#         return "Error: Record not found"

# def jref(strg):
#     regSpl = re.split("({[a-z]\\w+})", strg)

#     for ind in range(len(regSpl)):
#         if ref_fetch_reg(regSpl[ind]) != None:
#             regSpl[ind] = ref_fetch(regSpl[ind])

#     return regSpl