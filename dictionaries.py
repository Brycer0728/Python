ssn_name_pairs = dict()
# can also use {} instead of dict()

# write name of dictionary[key] = value
#ssn_name_pairs["123-456-789"] = "John Appleseed"
#ssn_name_pairs["000-000-002"] = "Dwight Schrute"
#ssn_name_pairs["000-000-005"] = "Pam Beesly"

# can also write it by puting the key in {} and seperate from the value with :
ssn_name_pairs = {"123-456-789": "John Appleseed",
                "000-000-002": "Dwight Schrute",
                "000-000-005": "Pam Beesly"}

#print(ssn_name_pairs)
#print(ssn_name_pairs["000-000-005"])

ssn_name_pairs["000-000-005"] = "Angela Martin" # will replace Pam Beesly with Angela Martin sicne they share the same key
ssn_name_pairs["000-000-003"] = "Andy Bernard" # will add Andy Bernard to the dictionary
#print(ssn_name_pairs)

del ssn_name_pairs["000-000-002"] # removed Dwight Schrute from dictionary
#print(ssn_name_pairs)

key = "000-000-005" # deleted Pam Beesly and added an else function to tell me if the provided key was invalid
if key in ssn_name_pairs:
    del ssn_name_pairs[key]
else:
    print(f"Invalied key {key}.")
print(ssn_name_pairs)