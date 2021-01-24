def objToDict(objList):
    dataDictList=[]
    for item in objList:
        dataDict={}
        userdataDict ={}
        userObj = item.user
        for key in userObj.__dict__.keys():

            userdataDict[key] = userObj.__dict__[key]
        userdataDict.pop('_sa_instance_state')
        dataDict["user"]=userdataDict
        for key in item.__dict__.keys():
            dataDict[key] = item.__dict__[key]
        dataDict.pop('_sa_instance_state')
        dataDictList.append(dataDict)
    return  dataDictList

def listToTree(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if list[i]["reply_id"] == 0:
                list[i]["reply_list"]=[]
            if list[j]["reply_id"] == list[i]["id"]:
                list[i]["reply_list"].append(list[j])
    print(list)
    return list