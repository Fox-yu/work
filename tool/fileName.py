import os
import re

#list
android_name = []
ios_name = []
pc_name = []
pcweb_name = []
androidweb_name = []
iosweb_name = []
other_name = []

str_file = os.getcwd()  # 当前脚本路径
for root,appnames,files in os.walk(str_file):
    break
print("请选择应用序号：")
for i in range(len(appnames)):
    print(i,appnames[i])
num = int(input())
type = input("是否输入版本号：(y/n)?\n")

def main():
    for dirpaths, dirnames, filenames in os.walk(str_file + "\\" + appnames[num]):
        for filename in filenames:
            # print(filename)
            if ".pcap" in filename:
                filename = filename.split(".")[0].replace("-", "").replace("_", "")  # 以“.”为分割点获取文件名
                if re.findall("android|Android|ANDROID", filename):
                    android_file = re.split("android|Android|ANDROID", filename)[1]
                    android_name.append(android_file)
                    for line in android_name:
                        if re.findall("web|WEB|Web", line):
                            android_name.remove(line)
                if re.findall("ios|Ios|IOS", filename):
                    ios_file = re.split("ios|Ios|IOS", filename)[1]
                    ios_name.append(ios_file)
                    for line in ios_name:
                        if re.findall("web|WEB|Web", line):
                            ios_name.remove(line)
                if re.findall("pc|PC|Pc", filename):
                    pc_file = re.split("pc|PC|Pc", filename)[1]
                    pc_name.append(pc_file)
                    for line in pc_name:
                        if re.findall("web|WEB|Web", line):
                            pc_name.remove(line)
                if re.findall("pcweb|Pcweb|PCweb|PCWEB", filename):
                    pcweb_file = re.split("pcweb|Pcweb|PCweb|PCWEB", filename)[1]
                    pcweb_name.append(pcweb_file)
                if re.findall("androidweb|Androidweb|ANDROIDWEB|AndroidWeb|androidWeb", filename):
                    androidweb_file = re.split("androidweb|Androidweb|ANDROIDWEB|AndroidWeb|androidWeb", filename)[1]
                    androidweb_name.append(androidweb_file)
                if re.findall("iosweb|Iosweb|IOSWEB|IOSWeb|IosWeb|iosWeb", filename):
                    iosweb_file = re.split("iosweb|Iosweb|IOSWEB|IOSWeb|IosWeb|iosWeb", filename)[1]
                    iosweb_name.append(iosweb_file)
                if re.findall("other", filename):
                    other_file = re.split("other", filename)[1]
                    other_name.append(other_file)
    def fileContent():
        android_action = ['\n', "## Android " + android_version, '']
        ios_action = ['\n', "## IOS " + ios_version, '']
        pc_action = ['\n', "## PC", '']
        pcweb_action = ['\n', "## PCweb", '']
        androidweb_action = ['\n', "## AndroidWeb", '']
        iosweb_action = ['\n', "## IOSWeb", '']
        other_action = ['\n', "## OTHER", '']
        for i in range(len(android_name)):
            Str_android = str(i + 1) + ". " + android_name[i] + "（）："
            android_action.append(Str_android)
        # print(android_action)
        for i in range(len(ios_name)):
            Str_ios = str(i + 1) + ". " + ios_name[i] + "（）："
            ios_action.append(Str_ios)
        for i in range(len(pc_name)):
            Str_pc = str(i + 1) + ". " + pc_name[i] + "（）："
            pc_action.append(Str_pc)
        # print(ios_action)
        for i in range(len(pcweb_name)):
            Str_pcweb = str(i + 1) + ". " + pcweb_name[i] + "（）："
            pcweb_action.append(Str_pcweb)
        # print(pcweb_action)
        for i in range(len(androidweb_name)):
            Str_androidweb = str(i + 1) + ". " + androidweb_name[i] + "（）："
            androidweb_action.append(Str_androidweb)
        # print(androidweb_action)
        for i in range(len(iosweb_name)):
            Str_iosweb = str(i + 1) + ". " + iosweb_name[i] + "（）："
            iosweb_action.append(Str_iosweb)
        for i in range(len(other_name)):
            Str_other = str(i + 1) + ". " + other_name[i] + "（）："
            other_action.append(Str_other)
        # print(iosweb_action)
        title = ["# " + appnames[num]]
        # print(content)
        createFile = appnames[num] + '.md'
        file = open(createFile, 'w', encoding='utf-8')
        for line in title:
            file.write(line + '\n')
        if len(android_action) > 3:
            for line in android_action:
                file.write(line + '\n')
        if len(ios_action) > 3:
            for line in ios_action:
                file.write(line + '\n')
        if len(pc_action) > 3:
            for line in pc_action:
                file.write(line + '\n')
        if len(pcweb_action) > 3:
            for line in pcweb_action:
                file.write(line + '\n')
        if len(androidweb_action) > 3:
            for line in androidweb_action:
                file.write(line + '\n')
        if len(iosweb_action) > 3:
            for line in iosweb_action:
                file.write(line + '\n')
        if len(other_action) > 3:
            for line in other_action:
                file.write(line + '\n')
        file.close()
    fileContent()

if type == "y":
    android_version = input("输入Android版本：\n")
    ios_version = input("输入IOS版本：\n")
    main()
elif type == "n":
    android_version = str("null")
    ios_version = str("null")
    main()
else:
    print("请输入正确的格式")
