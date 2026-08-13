def ref_break(ref, prop):
    
    if isinstance(ref, dict):
        if prop in ref:
            return ref[prop]
        else:
            return None
        

    body = []
    for obj in ref:
        if prop in obj:
            body.append(obj[prop])
        else:
            body.append(None)
            continue


    return body

def get_ids(ref):
    return ref_break(ref, "id")

def get_cats(ref):
    return ref_break(ref, "cat")