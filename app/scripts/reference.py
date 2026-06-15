from base_chars.models import Hiragana, Katakana
from particles.models import Particle
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
import re

def ref_fetch_split(strg):
    regSpl = re.split(r'(\{[^{}]*\})', strg)
    return regSpl

def ref_fetch_reg(ref):
    reg = re.findall(r'\{([^{}]*)\}', ref)
    return reg

def ref_fetch(ref):
    regex_pattern_prop = r'([^:|]+):([^|]+)'

    prop_tuples = re.findall(regex_pattern_prop, ref[0])
    
    ref_cat = ""
    ref_id = -1
    ref_props = {}

    for tup in prop_tuples:
        if tup[0] == "CAT":
            if ref_cat != "":
                return None
            else:
                ref_cat = tup[1]
        elif tup[0] == "ID":
            if ref_id != -1:
                return None
            else:
                ref_id = int(tup[1])
        else:
            if tup[0] not in ref_props:
                ref_props[tup[0]] = [tup[1]]
            else:
                ref_props[tup[0]].append(tup[1])
        
    if ref_id == -1 or ref_cat == "":
        return None

    match(ref_cat):
        case "hiragana":
            gana = Hiragana.objects.get(id=ref_id)
            return gana.to_dict
        case "katakana":
            return Katakana.objects.get(id=ref_id).to_dict
        case "particle":
            part_obj = Particle.objects.get(id=ref_id).to_dict

            regSpl = ref_fetch_split(part_obj["body"])
            jref_arr = []

            for ind in range(len(regSpl)):
                if ref_fetch_reg(regSpl[ind]) != None:
                    gana = ref_fetch(regSpl[ind])
                    jref_arr.append(gana)
            
            part_obj["body"] = jref_arr

            return part_obj
        # case "kanji":
            
        # case "word":
        #     return ref_fetch_word(id)
        case _:
            return "Error: Invalid category"
        

def jref(strg):
    regSpl = ref_fetch_split(strg)
    jref_arr = []

    for body in regSpl:
        if body == '':
            continue

        refProps = ref_fetch_reg(body)

        if len(refProps) != 0:
            prop = ref_fetch(refProps)
            jref_arr.append(ref_fetch(refProps))
        else:
            jref_arr.append(body)

    return jref_arr