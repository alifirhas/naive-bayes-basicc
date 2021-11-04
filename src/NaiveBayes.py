class NaiveBayes:

    def dict_item_list(x: dict, field: str):
        k = []
        for item in range(0,len(x)):
            k.append(x[item][field])
        return k

    def list_unique_items(x: list):
        return list({y for y in x})

    def get_dict_key(x: dict):
        return list(x[0].keys())

