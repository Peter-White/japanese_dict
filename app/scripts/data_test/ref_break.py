# def cat_break(ref):
#     match ref["cat"]:
#         case "hiragana" | "katakana" | "kanji":
#             return ref["body"]
#         case _:
#             return None



# def ref_break(ref, prop):
    
#     if isinstance(ref, dict):
#         if prop in ref:
#             return ref[prop]
#         else:
#             return None
        

#     body = []
#     for obj in ref:
#         if prop in obj:
#             body.append(obj[prop])
#         else:
#             body.append(None)
#             continue


#     return body

# def get_ids(ref):
#     return ref_break(ref, "id")

# def get_cats(ref):
#     return ref_break(ref, "cat")

def get_bodies(ref):
    body = ""

    for obj in ref:
        match(obj['cat']):
            case "hiragana" | "katakana" | "kanji" | "other":
                body += obj["body"]
            case "particle" | "word":
                body += get_bodies(obj["body"])
            case _:
                body += ""

    return body

def get_romaji(ref):
    rom = ""

    for obj in ref:
        match(obj['cat']):
            case "hiragana" | "katakana" | "kanji" | "other":
                rom += obj["rom"]
            case "particle" | "word":
                rom += get_bodies(obj["rom"])
            case _:
                rom += ""

    return rom