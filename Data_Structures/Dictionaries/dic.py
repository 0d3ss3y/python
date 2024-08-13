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
    
def lookUp():
    person = {
        "Natalie" : {
            "age": 27,
            "location" : "Pretoria",
            "Job" : "Doctor"
        },
        
        "Samuel" : {
            "age" : 22,
            "location" : "Midrand",
            "Job" : "Data Scientist"
        },
        
        "Rossi" : {
            "age" : 22,
            "location":"Rustenburg",
            "Job" : "Farmer"
        }
        
    }
    
    search(person)
    
def search(people):
    looking = "Samuel"
    
    for key,value in people.items():
        if key == looking:
            print(f"Looking up : {key}")
            for item,info in value.items():
                print(f"{item} : {info}")
        
     
 
if __name__ == "__main__":
    main()
