chai_types = {"Masala" : "Spicy", "Ginger" : "Zesty", "Green" : "Mild"}
# print(chai_types)

# print(chai_types["Masala"])

# for key, value in chai_types.items():
#     print(key, value)

# if "Masala" in chai_types:
#     print("i have masala chai")

# chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

# chai_types.pop("Ginger")
# print(chai_types)

# del chai_types["Green"]
# print(chai_types)

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

