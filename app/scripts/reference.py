from base_chars.models import Hiragana, Katakana
from particles.models import Particle
import re

def ref_fetch_split(strg):
    regSpl = re.split("({[a-z]\\w+})", strg)
    return regSpl

def ref_fetch_reg(ref):
    return re.search("^({)([a-z])(\\w+)(})$", ref)

def gana_obj(id):
    gana = Hiragana.objects.get(id=id)
    obj = {}
    obj["id"] = gana.pk
    obj["cat"] = "gana"
    obj["body"] = gana.body
    obj["rom"] = gana.romaji
    return obj

def kana_obj(id):
    kana = Katakana.objects.get(id=id)
    obj = {}
    obj["id"] = kana.pk
    obj["cat"] = "kana"
    obj["body"] = kana.body
    obj["rom"] = kana.romaji
    return obj

def particle_obj(id):
    part = Particle.objects.get(id=id)
    obj = {}
    obj["id"] = part.pk
    obj["cat"] = "particle"
    obj["body"] = part.body
    obj["rom"] = part.romaji
    obj["desc"] = part.description
    obj["use"] = part.use
    return obj

def ref_fetch(ref):
    reg_groups = ref_fetch_reg(ref).groups()
    ref_obj = {}

    cat = reg_groups[1]
    id = reg_groups[2]

    match(cat):
        case "h":
            return gana_obj(id)
        case "k":
            return kana_obj(id)
        case "p":
            part_obj = particle_obj(id)

            regSpl = ref_fetch_split(part_obj["body"])
            jref_arr = []

            for ind in range(len(regSpl)):
                if ref_fetch_reg(regSpl[ind]) != None:
                    gana = ref_fetch(regSpl[ind])
                    jref_arr.append(gana)
            
            part_obj["body"] = jref_arr

            return part_obj
        # case "j":
        #     return ref_fetch_kanji(id)
        # case "w":
        #     return ref_fetch_word(id)
        case _:
            return "Error: Invalid category"

def jref(strg):
    regSpl = ref_fetch_split(strg)
    jref_arr = []

    for ind in range(len(regSpl)):
        if regSpl[ind] == '':
            continue
        elif ref_fetch_reg(regSpl[ind]) != None:
            jref_arr.append(ref_fetch(regSpl[ind]))
        else:
            jref_arr.append(regSpl[ind])

    return jref_arr