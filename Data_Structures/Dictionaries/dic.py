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
    
    for key,value in person.items():
        print(f"{key} : {value}")
    
    print("\nremoval of Rossi")
    person.pop("Rossi")  
    print() 
    
    for key,value in person.items():
        print(f"{key} : {value}")

def update():
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
    
    person.update({"Hailey" : {
            "age" : 27,
            "location":"Rustenburg",
            "Job" : "Cyber Security Expert"
        }})
    
    for key,value in person.items():
        print(f"{key} : {value}")

def aggression(): 
    total = 0
    dict_aggregate = {
    'Alice': [1, 2, 3],
    'Bob': [4, 5, 6]
    }
    
    for key,value in dict_aggregate.items():
        for i in value:
            total += i
        print(f"{key} : Total = {total}")


if __name__ == "__main__":
    main()
