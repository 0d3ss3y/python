import string

def main():
    operational()
    print()
    lookUp()
    print()
    removal()
    print()
    update()
    print()
    aggression()
    print()
    count_letters()
    
def operational():
    person = {"name":"",
              "age" : None,
              "location":"",
              }
    
    person =add(person)
    
    for key, value in person.items():
        print(f"{key} : {value}")
           
def add(person):
    name = "Natalie"
    age = 27
    location = "Pretoria"
    
    person["name"] = name
    person["age"] = age
    person["location"] = location
    
    return person
        
     
 
if __name__ == "__main__":
    main()
