# ---------------------------------------------
# import package to read json
# ---------------------------------------------
import json

# ---------------------------------------------
#  write function to load file and parse json
# ---------------------------------------------

def readJson(file):

    with open(file) as f:
        data = json.load(f)

    return data
# ---------------------------------------------
#  call 'readJson', load salaries
# ---------------------------------------------

salaries = readJson('data.json')

# ---------------------------------------------
#  print all salaries
# ---------------------------------------------
#print(salaries)
# ---------------------------------------------
# loop through list, only print salary field
# ---------------------------------------------
for salary in salaries['data']:
   print(float(salary[18]))

# ---------------------------------------------
#  add all salaries
# ---------------------------------------------
   
print()

sal_count = 0

for salary in salaries['data']:
   sal_count += float(salary[18])

print(sal_count)
