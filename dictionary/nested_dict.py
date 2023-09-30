# Adding dictionaries to a parent dictionary
my_family={
    "child1" : {
        "name" : "Aayush"
    },

    "child2" : {
        "name" : "Aarushi"
    }
}

# or 
child1 = {
    "name" : "Aayush"
}

child2 = {
    "name" : "Aarushi"
}
my_family = {
    "child1" : child1,
    "child2" : child2
}

# To access item in a nested dictionary
print(my_family["child1"]["name"])