from base_chars.models import Hiragana, Katakana
from particles.models import Particle
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
import re

def ref_fetch_split(strg):
    regSpl = re.split("({[a-z]\\w+})", strg)
    return regSpl

def ref_fetch_reg(ref):
    return re.search("^({)([a-z])(\\w+)(})$", ref)

def ref_fetch(ref):
    reg_groups = ref_fetch_reg(ref).groups()
    ref_obj = {}

    cat = reg_groups[1]
    id = reg_groups[2]

    match(cat):
        case "h":
            return Hiragana.objects.get(id=id).to_dict
        case "k":
            return Katakana.objects.get(id=id).to_dict
        case "p":
            part_obj = Particle.objects.get(id=id).to_dict

            regSpl = ref_fetch_split(part_obj["body"])
            jref_arr = []

            for ind in range(len(regSpl)):
                if ref_fetch_reg(regSpl[ind]) != None:
                    gana = ref_fetch(regSpl[ind])
                    jref_arr.append(gana)
            
            part_obj["body"] = jref_arr

            return part_obj
        # case "j":
            
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