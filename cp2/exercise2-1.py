txt = [ 'yes no no',
        'no yes no',
        'no no no']

print (True for item in txt if 'yes' in item)
