def order_manage(model):
    prons = model.objects.all().filter(kanji=3).order_by("order")
    ords = set(prons.values_list("order", flat=True))

    set_match = len(ords) == len(prons)
    numbered_corr = prons[0].get_order() == 1 and prons[len(prons)-1].get_order() == len(prons)

    if not set_match or not numbered_corr:
        for ind, val in enumerate(prons):
            index = ind + 1

            if(val.get_order() != index):
                val.set_order(index)
                val.save()