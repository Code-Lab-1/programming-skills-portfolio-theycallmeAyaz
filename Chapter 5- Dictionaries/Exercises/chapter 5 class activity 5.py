About_me = {"name":"Mohammad Ayaz Warsi", "Gender":"Male", "Age":"18", "Nationality":"Pakistani"}
About_me["name"]="Mohammad Ayaz Warsi"
print(About_me)
About_me.popitem()
print(About_me)
if "Nationality" in About_me:
    print("it is present.")
else: print("it is not present.")