import re

string= "Affjg Bdkf Afkkff"
pattern = r"^A[a-z]+"
match = re.findall(pattern, string)
print(match)