from base_chars.models import Hiragana, Katakana
from particles.models import Particle
from kanji.models import KanjiBody, KanjiComprised, KanjiDefinition, KanjiPronunciation
from app.reference.ref_exceptions import ModelNotFound, IDNotNumber, CategoryNotValid
from words.models import WordBody
import math
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

def ref_build(strg, ref_func):
    regSpl = ref_fetch_split(strg)
    jref_arr = []

    for body in regSpl:
        if body == '':
            continue

        if ref_fetch_reg(body) != None:
            prop = ref_func(body)
            jref_arr.append(prop)
        else:
            strg_obj = { "cat" : "other", "body" : body }
            jref_arr.append(strg_obj)

    return jref_arr

def ref_obj_fetch(jmodel, ref_id):
    try:
        ref_id = int(ref_id)
    except:
        raise IDNotNumber(f"{ref_id} is non a valid whole number")

    model_objs = jmodel

    try:
        model_objs = model_objs.objects
    except:
        raise ModelNotFound("Model does not exist")

    try:
        return model_objs.get(id=ref_id).to_dict
    except :
        raise ModelNotFound(f"ID {ref_id} is invalid")

def ref_fetch(ref):
    try:
        refProps = ref_fetch_reg(ref)

        regex_pattern_prop = r'([^:|]+):([^|]+)'

        prop_tuples = re.findall(regex_pattern_prop, refProps)

        if len(prop_tuples) < 1:
            return None
        
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
                return ref_obj_fetch(Hiragana, ref_id)
            case "katakana":
                return ref_obj_fetch(Katakana, ref_id)
            case "particle":
                part_obj = ref_obj_fetch(Particle, ref_id)
                part_obj["body"] = ref_build(part_obj["body"], ref_fetch)

                return part_obj
            case "kanji":
                kanj_obj = ref_obj_fetch(KanjiBody, ref_id)

                if(len(ref_props) > 0):
                    for key, arr in ref_props.items():

                        match(key):
                            case "PRON":
                                for id in arr:
                                    pron_obj = ref_obj_fetch(KanjiPronunciation, id)
                                    pron_obj["body"] = ref_build(pron_obj["body"], ref_fetch)
                                    kanj_obj["prons"].append(pron_obj)
                            case "DEFT":
                                for id in arr:
                                    kanj_obj["defts"].append(ref_obj_fetch(KanjiDefinition, id))
                            case "COM":
                                for id in arr:
                                    kanj_obj["com"].append(ref_obj_fetch(KanjiComprised, id))
                            case _:
                                continue

                return kanj_obj
            case "word":
                word_obj = ref_obj_fetch(WordBody, ref_id)
                word_obj["body"] = ref_build(word_obj["body"], ref_fetch)

                return word_obj
            case _:
                raise CategoryNotValid("Category is not a valid category")
    except IDNotNumber as id_e:
        return id_e
    except ModelNotFound as model_e:
        return model_e
    except CategoryNotValid as cat_e:
        return cat_e

def jref(strg):
    return ref_build(strg, ref_fetch)