import re

text = "abddc abbbb, baccc hg,fahbbhbb. bcaDJFGDb : abc_  a_bc Abcdefg B"
pattern = r"ab*"
match = re.search(pattern, text)
print(match.group())

pattern1 = r"abbb?"
match1 = re.search(pattern1, text)
print(match1.group())

pattern2 = r"[a-z]_+"
match2 = re.search(pattern2, text)
print(match2.group())

pattern3 = r"[A-Z].{1}[a-z]+"
match3 = re.search(pattern3, text)
print(match3.group())

pattern4 = r"[a].*b" # r"[a].*b"
match4 = re.findall(pattern4, text)
print(match4)

pattern5 = r"[., ]"
match5 = re.sub(pattern5, ":", text)
print(match5)

text1 ="snake_case_string_to_camel_case_string"
pattern6 = r"_([a-zA-Z])"
match6 = re.sub(pattern6, lambda x: x.group(1).upper() ,text1)
print(match6)

text2 = "ExampleForMatch7"
pattern7 = r"(?=[A-Z])"
match7 = re.split(pattern7, text2)
print(match7)

text3 = "SpaceDlyaEtoiZadachi"
pattern8 = r"(?<!^)(?=[A-Z])"
match8 = re.sub(pattern8, " ", text3)
print(match8)

text4 = "Snake_string_for_example"
pattern9 = r"([a-z])([A-Z])"
match9 = re.sub(pattern9, r"\1_\2", text4)