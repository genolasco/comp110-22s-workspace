"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empt dictionary
schools = dict()


# Set a key-value pairing in teh dictionary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal represntaion
print(schools)

# Access avlue by its key  -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from dictionary
# by its key
# schools.pop("Duke")

# Test for the existence of a key 
if "Duke" in schools:
    print("Found the key ' Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstraion of dictionary literals

# Empty dictionary literal
schools = {}  # same ad dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400, 
    "DUkie": 6717, 
    "NCSU": 26150
}
print(schools)

# What happens when a key doesn not exist?
# print(schools["UNCC"])
# You get a KeyError

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")