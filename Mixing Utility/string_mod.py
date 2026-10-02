from data_raw import RAW_DATA
from data_raw_2 import RAW_DATA_2

from obj.ingredient import Ingredient

# Print items from any dictionary when dict passed as arg
def print_dict(d):      # Dict print function
    for k, v in d.items():
        print(f"Key: {k} Value: {v}")

# Prints all sub-dictionaries from the master dictionary
def print_all():
    for item in master_dict.keys():
        print_ingredient_dict(item)
        print()

# Prints items from master ing dictionary when ing dict passed as arg
# Helper function for print_all()
def print_ingredient_dict(d):
    # print(master_dict.items())
    for k, v in master_dict.items():
        if k == d:
            # print(v.items())
            for item in v.items():
                print(f"{item[0]}: {item[1]}")

# Prints all ingredient objects from the ing obj dict
def print_ing_objs():
    for ingredient in ingredient_objects.values():
        print(ingredient)

# Generates an obj dictionary from an ingredient dictionary
def gen_ing_obj_dict():
    ingredient_objects = {}

    for ing_name, ing_details in master_dict.items():
        if "name" not in ing_details:
            ing_details["name"] = ing_name 
        ingredient_objects[ing_name] = Ingredient(**ing_details)
    return ingredient_objects


# Assign raw data string to working variable
raw_data = RAW_DATA

# Create an empty list to store the parsed data
data_list = []

# Strip the outer new line chars from the raw data string
data_clean_1 = raw_data.strip("\n")

# Parse string into list of ingredrient data attributes by splitting at double new line
# Result is each list item representative of one set of ingredient attributes
data_list = data_clean_1.split("\n\n")

# Create an empty master ingredient dictionary
master_dict = {}

# Create a list of dictionary key names for ingredient attributes
md_names = ["name", "price", "rank", "description","effect_base"]

# Create categories for the type of data (indices will match the respective indecies of the data list item
data_names = ["icon", "multi_data_str"]

# Loop through cleaned list of ingredient data and convert each unique ingredient attribute data set into sub-dictionaries
for item_idx, item in enumerate(data_list):
    # print(item)

    # Create a temporary attribute dictionary for each list item (ingredient attribute data)
    att_data_dict = {}

    #Splite the item into a list of attributes
    att_data = item.split("\n")
    # print(f"\nSublist Index # {item_idx}:\n{att_data}")

#  separate data by name (for key) and remaining attribute data
    for data_idx, data in enumerate(att_data):

        # if the index of the attribute is 
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

# Generate obj dictionary from ingredient dictionary
ingredient_objects = gen_ing_obj_dict()

# Create an instance of a cuke object by assigning from the object dictionary
cuke = ingredient_objects["Cuke"]


print(f"------------ TEST AREA ------------\n-----------------------------------")


print(f"Raw Data:{repr(raw_data)}\n")
print(f"Data_clean:{repr(data_clean_1)}\n")
print(f"Data_list:{repr(data_list)}\n")
print(f"\nMaster_dict:\n{repr(master_dict)}\n")
print(cuke)
print(f"Cuke Cost: {cuke.cost}")


raw_data_2 = RAW_DATA
data_list_2 = []

# Clean the raw string by removing the outer new lines
data_clean_2 = raw_data_2.strip("\n")

data_clean_3 = raw_data_2.strip("\t")

# Parse blocks of text into list by splitting at double new line
data_list_2 = data_clean_3.split("\n\n")

print()
print(data_list_2)

for item in data_list_2:
    print(item)

print_all()
