# format_map in braces {} use key name and .format_map(dictionary_name)
lunch = {"Food": "Pizza", "Drink": "Wine", "mobile" : "Mi"}
print("Lunch: {Food}, {Drink} {mobile}".format_map(lunch))