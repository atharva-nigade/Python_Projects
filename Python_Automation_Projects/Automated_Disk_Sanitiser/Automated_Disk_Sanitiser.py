import hashlib
import os

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fName in FileName:
            fName = os.path.join(FolderName, fName)
            Checksum = CalculateCheckSum(fName)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fName)
            else:
                Duplicate[Checksum] = [fName]
            
    return Duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        print("Value of Count is :", Count)
        Count = 0

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Deleted File : ", subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0

    print("Total Deleted Files : ", Cnt)


def main():
    DeleteDuplicate()

if __name__ == "__main__":
    main()
