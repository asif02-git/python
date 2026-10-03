# lab2_task4.py

def build_profile(**details):
    print("\n" + "="*25)
    print("      PROFILE CARD      ")
    print("="*25)
    for key, value in details.items():
        print(f"{key.capitalize():<12}: {value}")
    print("="*25)

build_profile(name="Ravi", age=21, city="Hyderabad", hobby="Cricket")
build_profile(name="Sita", profession="Engineer", city="Bangalore")


OUTPUT:

#       PROFILE CARD      

# Name        : Ravi
# Age         : 21
# City        : Hyderabad
# Hobby       : Cricket
#       PROFILE CARD      
# Name        : Sita
# Profession  : Engineer
# City        : Bangalore

