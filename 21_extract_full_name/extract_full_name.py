def extract_full_names(people):
    full_names = []
    for name in people:
        full_names.append(' '.join((name["first"], name["last"])))
    return full_names
