from optparse import OptionParser  
import os
import json
from collections import OrderedDict
TARGET_DIR = "E:/develop/code/CocosNew/FuGou/customer_config"

def addKey(key , value):
    for targetFile in os.listdir(TARGET_DIR):
        if os.path.isfile(os.path.join(TARGET_DIR, targetFile)): 
            continue    
        targetFile = os.path.join(TARGET_DIR , targetFile , 'config.json')  
        data = None
        with open(targetFile , 'r') as f:
            text = f.read()
            configData = json.loads(text)
            if not configData.has_key(key):
                configData[key] = value
            data = json.dumps(configData,sort_keys=True, ensure_ascii=False , indent=4, separators=(',', ': '))
        with open(targetFile , 'w') as o:
            if data :
                o.write(data.encode("utf-8"))

def addVersion(bigVersionEnv):
    for targetFile in os.listdir(TARGET_DIR):
        if os.path.isfile(os.path.join(TARGET_DIR, targetFile)): 
            continue    
        targetFile = os.path.join(TARGET_DIR , targetFile , 'config.json')  
        data = None
        with open(targetFile , 'r') as f:
            text = f.read()
            configData = json.loads(text, object_pairs_hook=OrderedDict)
            targetKey = 'bigVersion_' + bigVersionEnv
            if configData.has_key(targetKey):
                configData[targetKey] = int(configData[targetKey]) + 1
            data = json.dumps(configData,sort_keys=False, ensure_ascii=False , indent=4, separators=(',', ': '))
        with open(targetFile , 'w') as o:
            if data :
                o.write(data.encode("utf-8"))
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-k' , '--targetKey' , dest = "targetKey")
    parser.add_option('-v' , '--targetValue' , dest = "targetValue")
    parser.add_option('-b' , '--bigVersionEnv' , dest = "bigVersionEnv")
    (option , args) = parser.parse_args()

    targetKey = option.targetKey
    targetValue = option.targetValue
    bigVersionEnv = option.bigVersionEnv
    if not bigVersionEnv:
        addKey(targetKey , targetValue)
    else:
        addVersion(bigVersionEnv.upper())