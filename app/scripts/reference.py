from base_chars.models import Hiragana, Katakana
from particles.models import Particle
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
import re

def ref_fetch_split(strg):
    regSpl = re.split(r'(\{[^{}]*\})', strg)
    return regSpl

def ref_fetch_reg(ref):
    reg = re.findall(r'\{([^{}]*)\}', ref)

    if len(reg) != 0:
        return reg[0]
    else:
        return None

def ref_fetch(ref):
    regex_pattern_prop = r'([^:|]+):([^|]+)'

    prop_tuples = re.findall(regex_pattern_prop, ref)
    
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
            return Hiragana.objects.get(id=ref_id).to_dict
        case "katakana":
            return Katakana.objects.get(id=ref_id).to_dict
        case "particle":
            part_obj = Particle.objects.get(id=ref_id).to_dict

            regSpl = ref_fetch_split(part_obj["body"])
            jref_arr = []

            for ind in range(len(regSpl)):
                if ref_fetch_reg(regSpl[ind]) != None:
                    base_obj = ref_fetch(regSpl[ind])
                    jref_arr.append(base_obj)
            
            part_obj["body"] = jref_arr

            return part_obj
        case "kanji":
            kanj_obj = KanjiBody.objects.get(id=ref_id).to_dict

            if(len(ref_props) > 0):
                for key, arr in ref_props.items():

                    match(key):
                        case "PRON":
                            for i, id in enumerate(arr):
                                pron_obj = KanjiPronunciation.objects.get(id=id).to_dict

                                regSpl = ref_fetch_split(pron_obj["body"])
                                jref_arr = []

                                for ind in range(len(regSpl)):
                                    refProps = ref_fetch_reg(regSpl[ind])
                                    if refProps != None:
                                        base_obj = ref_fetch(refProps)
                                        jref_arr.append(base_obj)

                                kanj_obj["prons"] += jref_arr
                        # case "DEFT":
                        #     kanj_obj["defts"] = kanji_prop_get(KanjiDefinition, val)
                        # case "COM":
                        #     kanj_obj["coms"] = kanji_prop_get(KanjiComprised, val)
                        case _:
                            return None

            return kanj_obj
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

        if refProps != None:
            prop = ref_fetch(refProps)
            jref_arr.append(ref_fetch(refProps))
        else:
            jref_arr.append(body)

    if(len(jref_arr) == 1):
        return jref_arr[0]

    return jref_arr