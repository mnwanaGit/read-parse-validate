import glob
import json

# -----------------------------------
#  validate json
# -----------------------------------

def removeQuotes(string):
    pass

def validate(salary):
    try:
        sid = salary["sid"],
        ID = salary["id"],
        pos = salary["position"],
        create_a = salary["created_at"],
        create_m = salary["created_meta"],
        upd_a = salary["updated_at"],
        upd_m = salary["updated_meta"],
        meta = salary["meta"],
        name = salary["name"],
        title = salary["title"],
        dep_name = salary["department_name"],
        reg = salary["regular"],
        retro = salary["retro"],
        other = salary["other"],
        ot = salary["overtime"],
        ir = salary["injured"],
        detail = salary["detail"],
        quinn = salary["quinn"],
        tot_earnings = salary["total_earnings"],
        z = salary["zip"]

    except Exception as e:
        return False
    return True

# -----------------------------------
#  parse json function
# -----------------------------------

# load file and parse json
def readJson(file):
    with open(file) as p:
        return json.load(p)

# -----------------------------------
#  loop files, parse, validate
# -----------------------------------
pattern = './data/*/*.json'
data = []

for file in glob.glob(pattern):
    data.append(file) #append into something called data

for file in data:
    salaries = readJson(file)

#validate here
    for salary in salaries:
        print('file:', file, '- validation:', validate(salary))