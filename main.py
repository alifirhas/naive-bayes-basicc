from src.NaiveBayes import *
from itertools import *

def main():
    # = Cuaca	Temperatur	Berolahraga
    # = Cerah	Normal      Ya
    # = Cerah	Tinggi      Ya
    # = Hujan	Tinggi      Tidak
    # = Cerah	Tinggi	    Tidak
    # = Hujan	Normal	    Tidak
    # = Cerah	Normal	    Ya

    nb = NaiveBayes()

    loads = [
        {
            'Cuaca': 'Cerah',
            'Temperatur': 'Normal',
            'Berolahraga': 'Ya'
        },
        {
            'Cuaca': 'Cerah',
            'Temperatur': 'Tinggi',
            'Berolahraga': 'Ya'
        },
        {
            'Cuaca': 'Hujan',
            'Temperatur': 'Tinggi',
            'Berolahraga': 'Tidak'
        },
        {
            'Cuaca': 'Cerah',
            'Temperatur': 'Tinggi',
            'Berolahraga': 'Tidak'
        },
        {
            'Cuaca': 'Hujan',
            'Temperatur': 'Normal',
            'Berolahraga': 'Tidak'
        },
        {
            'Cuaca': 'Cerah',
            'Temperatur': 'Normal',
            'Berolahraga': 'Ya'
        },
    ]
    
    print("Field dan unique item")

    fields = nb.get_dict_key(loads)
    print(fields)

    adjv_field_item = []
    for index, field in enumerate(fields):
        x = nb.dict_item_list(loads, field)
        x_unique =  nb.list_unique_items(x)
        print(index, ", ", field, ": ", x_unique)
        adjv_field_item.append(x_unique)

    print(adjv_field_item)
    a = adjv_field_item[0]
    b = adjv_field_item[1]
    c = adjv_field_item[2]

    for i in product(a,b,c):
        print(list(i))

    # print(x)
    # print(list_unique_items(x))
    # print({i:x.count(i) for i in x if i == "Ya"})

    # def dynamic_for_loop(boundaries, *vargs):
    #     if not boundaries:
    #         print(*boundaries)
    #         # for j in range(0, len(vargs)):
    #         #     print(boundaries[vargs[j]]) # or whatever you want to do with the values
    #     else:
    #         bounds = boundaries[0]
    #         for i in range(0, len(bounds)):
    #             dynamic_for_loop(boundaries[1:], *(vargs + (i,)))

    # loads = [
    #     ['Cerah', 'Hujan'],
    #     ['Tinggi', 'Normal', 'Rendah'],
    #     ['Ya', 'Tidak']
    # ]

    # print(range(0, len(loads[0])))

    # # loads = [[0,5,1], [0,3,1], [0,3,1]]

    # dynamic_for_loop(loads)

if __name__ == '__main__':
    main()