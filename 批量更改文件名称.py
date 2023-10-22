import os
import shutil

def ReNamefilesInfo(Path, oldInfo, newInfo):
    allitems = os.listdir(Path)
    for item in allitems:
        itemPath = os.path.join(Path, item)
        if os.path.isdir(itemPath):
            ReNamefilesInfo(itemPath, oldInfo, newInfo)
        else:
            newitem = item.replace(oldInfo, newInfo)
            newitemPath = os.path.join(Path, newitem)
            shutil.move(itemPath, newitemPath)

# TODO 设置Path的值(设置根目录)
Path = ""
# TODO 设置oldInfo,newInfo的值（设置需要删除的文件，非文件夹）
oldInfo = ""
newInfo = ""

# 调用ReNamefilesInfo()函数进行文件删除
ReNamefilesInfo(Path, oldInfo, newInfo)

print('文件已全部重命名')
