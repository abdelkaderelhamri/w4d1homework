"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""
import re
with open('regex_test.txt') as f:
    data = f.read()
    #print(data)
    my_string ="Abraham Lincoln,Andrew P Garfield,Connor Milliken,Jordan Alexander Williams,Madonna,programming is cool"
# Creating our groups in our pattern
pattern_name = re.compile('([A-Z][\w]+) ?([A-Z][\w]*)? ([A-Z][\w]+)')
                                #group1         group2
found_names = pattern_name.findall(my_string)
#print(found_names)

for name in my_string.split(','):
    match = pattern_name.search(name)
    if match: 
        if match.group(2):
            print(match.group(1), match.group(2), match.group(3))
        elif not match.group(2):
            print(match.group(1), match.group(3)) 
      
    else:
        print("Not a valid name")
    