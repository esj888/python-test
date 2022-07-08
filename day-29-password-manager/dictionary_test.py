website_dict = {
    "first site": {
        "email": "email@gmail.com",
        "password": "G6y8h9%eF7lvp*a"
    },
    "second site": {
        "email": "num2@email.com",
        "password": "GV3kz1(hkh3X$"
    },
    "third site": {
        "email": "3@3.com",
        "password": "a04PQi3dv+pc%*"
    },
    "amazon": {
        "email": "email@gmail.com",
        "password": "u%4whc1Gmi(Q8+d4n"
    }
}

print(type(website_dict))
print(website_dict)

# print sites
print("*** websites ***")
for sites in website_dict.keys():
    print(sites)

# print email
print("*** email ***")
email = website_dict["amazon"]["email"]
print(type(email))
print(email)

# print password
print("*** password ***")
pass1 = website_dict["amazon"]["password"]
print(type(pass1))
print(pass1)
