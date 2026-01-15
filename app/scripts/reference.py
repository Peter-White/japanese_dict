from base_chars.models import Hiragana, Katakana
from particles.models import Particle
import re

def ref_fetch_reg(ref):
    return re.search("^({)([a-z])(\\w+)(})$", ref)

def ref_fetch(ref):
    reg_groups = ref_fetch_reg(ref).groups()
    ref_obj = {}

    cat = reg_groups[1]
    id = reg_groups[2]

    match(cat):
        case "h":
            return Hiragana.objects.get(id=id)
        case "k":
            return Katakana.objects.get(id=id)
        case "p":
            fetch_part = Particle.objects.get(id=id)
            fetch_gana = ref_fetch(fetch_part.body)

            fetch_part.boby = fetch_gana.body

            return fetch_part
        # case "j":
        #     return ref_fetch_kanji(id)
        # case "w":
        #     return ref_fetch_word(id)
        case _:
            return "Error: Invalid category"

def jref(strg):
    regSpl = re.split("({[a-z]\\w+})", strg)
    jref_obj = {}

    for ind in range(len(regSpl)):
        test = regSpl[ind]
        if ref_fetch_reg(regSpl[ind]) != None:
             jref_obj[ind] = ref_fetch(regSpl[ind])
        else:
            jref_obj[ind] = regSpl[ind]

    return jref_obj