my_string   = " this is a test string "
my_list     = [" this is", " ", "a test ", "list" ]

#print([x.strip() for x in my_string]) #oneliner

def my_func(x):
    print([y.strip() for y in x]) #oneliner

my_func(my_string)
my_func(my_list)
