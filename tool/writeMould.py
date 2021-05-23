#!/usr/bin/python
#coding=utf-8
import json
import re
#获取数据
def getResultString(listName):
    path="output_define.cfg"
    f=open(path,'rb')
#print(f.read())
    fileData=f.read()
    f.close()
    topData=re.findall('OUTPUT_LIST:(.*?)";',fileData.decode('utf-8'),re.S)
    topDataString=topData[0].replace('\n','')
    topDataList=re.findall(',(.*?)\[(.*?)\]',topDataString,re.S)
    # print(topDataList)
#大协议英文名词和协议值字典
    topEngDict=dict(topDataList)
    fieldBody=re.split(r'}',fileData.decode('utf-8'))
    fieldPart=re.findall('(.*?)=(.*?);',fieldBody[1],re.S)
    # print(fieldPart)
#for top in fieldPart:
    #print(top[0].replace('\n',''))
    fieldJSONString=""
    for fieldContent in fieldPart:
        fieldFlag=38
        fieldString=fieldContent[1].replace('\n\t','').replace('\n','')
        filedList=re.findall('"(.*?)"',fieldString,re.S)
        if fieldContent[0].replace('\n','').strip() in topEngDict.keys():
            for field in filedList:
                fieldJSON='{'+'"TopProtocolEnglishName":"'+fieldContent[0].replace('\n','')+'","TopProtocolCode":'+topEngDict[fieldContent[0].replace('\n','').strip()]+',"TopProtocolFlag":'+str(fieldFlag)+',"FieldEnglishName":"'+field+'"}'
                fieldFlag+=1
                fieldJSONString=fieldJSONString+fieldJSON+','
    # print(fieldJSONString)
    dataJSON=json.loads('{"fieldStringList":['+fieldJSONString.strip(',')+']}')
    return dataJSON[listName]
# #删除文件最后一行
# def deleteEnd():
#     file_old = open('powershell.json', 'r', encoding="utf-8")
#     lines = [i for i in file_old]
#     del lines[-1]
#     file_old.close()
#     file_new = open('powershell.json', 'w', encoding="utf-8")
#     file_new .write(''.join(lines))
#     file_new .close()
# #最后一行加"}"
# def addEnd():
#     file_old = open('powershell.json', 'a', encoding="utf-8")
#     file_old.write("\n"+"}")
#     file_old.close()


if __name__=="__main__":
    dataList=getResultString("fieldStringList")
    file_path = "/root/PR/Share/etc/.vscode/code-字段.code-snippets"
    file = open(file_path,'w')
    file.write("{")
    for data in dataList:
        jsonString='"'+str(data["TopProtocolEnglishName"]).strip()+'_'+str(data["FieldEnglishName"])+'": {"prefix":"'+str(data["TopProtocolEnglishName"]).strip()+'_'+str(data["FieldEnglishName"])+'",'+'"body": ["#'+str(data["FieldEnglishName"])+'","N_('+str(data["TopProtocolFlag"])+')="]}'
        #print(jsonString)
        #dataDict = json.loads(jsonString)
        file.write("\n"+jsonString+",")
            #json.dump(jsonString,f)
    file.write("\n"+"}")
    file.close()