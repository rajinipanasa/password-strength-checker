password = input("Enter your password:")

length_ok = len(password) >=8
number_ok = any (char .isdigit() for char in password)
uppercase_ok = any (char .isupper() for char in password)

special_chars = {"!", "@", "#", "$", "%", "&", "*"}
special_ok = any (char in special_chars for char in password)

score = length_ok + number_ok + uppercase_ok + special_ok

if score == 4:
    print("strong password")
elif score >= 2:
    print("medium password")
else:
    print("weak password")