import math
import numpy as np
#from pandas.io.json import json_normalize 
import pandas.io.json as pj

def flatten_event(y):
    out = []
    for x in y:
        item = {}
        item.update(x['contexts']['device'])
        item['version'] = x['contexts']['os']['version']
        #dont work with resample: item['created'] = timestring.Date(x['dateCreated'])
        #dont work with resample: item['created'] = dateparser.parse(x['dateCreated'])
        item['created'] = np.datetime64(x['dateCreated'])
        out.append(item)
        #We normalize the list to get the wanted data type pandas.core.frame.DataFrame
        data = pj.json_normalize(out)
    return data