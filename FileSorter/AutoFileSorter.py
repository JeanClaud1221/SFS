import shutil
import os
class fileObject:
    def __init__(self,name):
        temp=name.split("_z_")
        self.name=temp[1]
        self.extention=temp[0]
    def ats(self):
        return {"Name":self.name,"Ext":self.extention}
    def GetName(self):
        return self.name
    def GetExtention(self):
        return self.extention
    
class Management:
    def __init__(self):
        self.extentions={}
        self.shorthand={"TEST":"C:/Users/jean-claud/Desktop/Test/Output",
                        "AUD":"C:/Users/jean-claud/Desktop/Test/Audio",
                        "TXT":"C:/Users/jean-claud/Desktop/Test/Text"}
        self.source="C:/Users/jean-claud/Desktop/Insert"

    #Check if in the extentions and shorthand section
    def __check_in_extentions(self,ext):
        if ext in self.extentions:
            return True
        return False
    
    def __check_in_shorthand(self,st):
        if st in self.shorthand:
            return True
        return False
    
    #Get the shorthand/extention path section
    def __get_extention_path(self,key):
        if self.__check_in_extentions(key):
            return self.extentions[key]
        return False
    
    def __get_shorthand_path(self,key):
        if self.__check_in_shorthand(key):
            return self.shorthand[key]
        return False

    #adding to extentions and shorthand section
    def add_extention(self,ext,fold):
        if self.__check_in_extentions(ext):
            self.extentions[ext]=fold
            return True
        return False
    
    def add_shorthand(self,short,path):
        if self.__check_in_shorthand(short):
            self.shorthand[short]=path
            return True
        return False
    #Spliting the path string
    def split_string(self,st):
        temp=st.split('_')
        return temp
    #Find where the extention exists 
    def find_prefix(self,pref):
        if self.__check_in_extentions(pref):
            return 1
        elif self.__check_in_shorthand(pref):
            return 2
        else: 
            return 0
        
    
    def BuildDestination(self,FileName):
        f=fileObject(FileName)
        finfo=f.ats()
        extentions=self.split_string(finfo['Ext'])
        pathBuilder=""
        for i in extentions:
            wherePrefixStored=self.find_prefix(i)
            if wherePrefixStored==1:
                pathBuilder+=self.__get_extention_path(i)
            elif wherePrefixStored==2:
                pathBuilder+=self.__get_shorthand_path(i)
            else:
                print("invalid path")
                pathBuilder=""
                break
        pathBuilder+=f"/{finfo['Name']}"
        return pathBuilder
    def main(self):
        listOfFiles=os.listdir(self.source)
        for item in listOfFiles:
            src=self.source+"/"+item
            shutil.move(src,self.BuildDestination(item))

        
                


m=Management()
m.main()

    

    


