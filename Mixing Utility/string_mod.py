from data_raw import RAW_DATA

from obj.ingredient import Ingredient

raw_data = RAW_DATA
data_list = []

# Clean the raw string by removing the outer new lines
data_clean_1 = raw_data.strip("\n")

# Parse blocks of text into list by splitting at double new line
data_list = data_clean_1.split("\n\n")

"""
print(raw_data)
print(data_clean_1)
print(data_list)
"""

md_names = ["name", "price", "rank", "description","effect_base"]
data_names = ["icon", "multi_data_str"]
master_dict = {}
print()
def print_dict(d):      # Dict print function
    for k, v in d.items():
        print(f"Key: {k} Value: {v}")

def print_ingredient_dict(d):
    for k, v in master_dict.items():
        if k == d:
            for item in v.items():
                print(f"{item[0]}: {item[1]}")

def print_all():
    for item in master_dict.keys():
        print_ingredient_dict(item)
        print()

for item_idx, item in enumerate(data_list):
    att_data_dict = {}
    att_data = item.split("\n")
    # print(f"\nSublist Index # {item_idx}:\n{att_data}")

    for data_idx, data in enumerate(att_data):
        
        if data_idx < 2:
            key_name = f"{data_names[data_idx]}"
        else:
            effect_num = data_idx
            key_name = f"effect_{effect_num}"

        att_data_dict[key_name] = data

    multi_data_str = att_data_dict["multi_data_str"]
    dolla_index = multi_data_str.find('$')
    md_name_str = multi_data_str[:dolla_index].strip("\t")
    md_cost_str = multi_data_str[dolla_index:dolla_index+2]
    md_rest_split = multi_data_str[dolla_index+3:].split("\t")

    reord_dict = {}
    reord_dict["name"] = md_name_str
    reord_dict["cost"] = md_cost_str
    reord_dict["rank"] = md_rest_split[0]
    reord_dict["description"] = md_rest_split[1]
    reord_dict["effect_base"] = md_rest_split[2]
    reord_dict["effect_1"] = md_rest_split[3]

    for data_idx, data in enumerate(att_data):
        
        if data_idx > 1:
            key = f"effect_{data_idx}"
            reord_dict[key] = data
        else:
            continue

    master_dict[reord_dict["name"]] = reord_dict

# print_all()

def gen_ing_obj_dict():
    ingredient_objects = {}

    for ing_name, ing_details in master_dict.items():
        if "name" not in ing_details:
            ing_details["name"] = ing_name 
        ingredient_objects[ing_name] = Ingredient(**ing_details)
    return ingredient_objects

ingredient_objects = gen_ing_obj_dict()

cuke = ingredient_objects["Cuke"]
print(cuke)
print(f"Cuke Cost: {cuke.cost}")
print()

for ingredient in ingredient_objects.values():
    # print(ingredient)
    print(ingredient.name)









print()
