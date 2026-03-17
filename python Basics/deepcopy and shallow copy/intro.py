# shallow copy doesn't make chnges in both inner and outer object hence we need to use deepcopy
# also it does not look over inner objects,outer object nte copy mathre create ayyindavollu

# deep copy works under nested collection


# copy.py>deepcopy
# csv.pyDictReader

from copy import deepcopy

arun_fvt_food=[
    {"meal_type":"break_fast","meal":"dosa"},
    {"meal_type":"lunch","meal":"fish meal"},
    {"meal_type":"dinner","meal":"fried rice"}
]
hari_fvt_food= deepcopy(arun_fvt_food)
hari_fvt_food[0]["meal"]="idly"

print("arun",arun_fvt_food)
print("hari",hari_fvt_food)