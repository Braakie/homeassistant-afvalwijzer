def _waste_type_rename(item_name):
    # Mapping of waste types
    waste_mapping = {
        "branches": "takken",
        "best_bag": "best-tas",
        "bulklitter": "grofvuil",
        "bulkygardenwaste": "tuinafval",
        "christmas_trees": "kerstbomen",
        "gemengde plastics": "plastic",
        "glass": "glas",
        "green": "gft",
        "groente": "gft",
        "groente-, fruit en tuinafval": "gft",
        "groente, fruit- en tuinafval": "gft",
        "grey": "restafval",
        "kca": "chemisch",
        "kerstb": "kerstboom",
        "kerstboom": "kerstbomen",
        "opk": "papier",
        "packages": "pmd",
        "pap": "papier",
        "paper": "papier",
        "pdb": "pmd",
        "papier en karton": "papier",
        "plastic": "plastic",
        "plastic, blik & drinkpakken arnhem": "pmd",
        "plastic, blik & drinkpakken overbetuwe": "pmd",
        "pmd": "pmd",
        "pmdrest": "pmd-restafval",
        "pruning_waste": "snoeiafval",
        "remainder": "restwagen",
        "residual_waste": "restafval",
        "rest": "restafval",
        "restafvalzakken": "restafvalzakken",
        "sloop": "grofvuil",
        "snoeiafval": "takken",
        "tariefzak restafval": "restafvalzakken",
        "textile": "textiel",
        "tree": "kerstbomen",
        "zak_blauw": "restafval",
    }

    return waste_mapping.get(item_name, item_name)


if __name__ == "__main__":
    print("Yell something at a mountain!")
