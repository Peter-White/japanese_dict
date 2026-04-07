def order_manage(cat, kanji):
    if len(cat) != 0:
        ords = set(cat.values_list("order", flat=True))

        set_match = len(ords) == len(cat)

        numbered_corr = cat[0].get_order() == 1 and cat[len(cat)-1].get_order() == len(cat)

        if not set_match or not numbered_corr:
            for ind, val in enumerate(cat):
                index = ind + 1

                if(val.get_order() != index):
                    val.set_order(index)
                    val.save()