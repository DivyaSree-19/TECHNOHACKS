import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@_*^$#"
length_pass=int(input("enter a length of ur password: "))
a="".join(random.sample(password,length_pass))
print(f"Your password is {a}")
