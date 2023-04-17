my_string   = " this is a test string "
my_list     = [" this is", " ", "a test ", "list" ]

#oneliner:
#print([x.strip() for x in my_string]) 

def my_func(x):
    #oneliner:
    print([y.strip() for y in x]) 

my_func(my_string)
my_func(my_list)

print(list(my_string))
