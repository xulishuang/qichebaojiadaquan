'''
Created on 2017-1-13

@author: xuls
'''
from PIL import Image 
import os

PATH2=os.path.dirname(os.getcwd())

def classfiy_histogram(image1,image2,size = (256,256)):     
    image1 = image1.resize(size).convert("RGB")   
    g = image1.histogram()     
    image2 = image2.resize(size).convert("RGB")   
    s = image2.histogram()     
    assert len(g) == len(s),"error"     
    data = []    
    for index in range(0,len(g)):        
        if g[index] != s[index]:            
            data.append(1 - abs(g[index] - s[index])/max(g[index],s[index]) )       
        else:            
            data.append(1)    
    print(sum(data)/len(g))
    
def compare(image):  
    image1 = Image.open(PATH2+"\\aw\\image\\expected\\"+image+".png")  
    image2 = Image.open(PATH2+"\\aw\\image\\actual\\"+image+".png") 
    print(image+"-differ:")
    classfiy_histogram(image1,image2,size = (256,256))
    

if __name__ == "__main__":
    '''Search'''
    compare("image01")
    compare("image02")
    compare("image03")
    compare("image04")
    compare("image05")
    compare("image06")
    compare("image07")
    compare("image08")
#     
    '''BusinessChance'''
    compare("image11")
    compare("image12")
    compare("image13")
    compare("image14")
     
    '''CarContrast'''
    compare("image21")
    compare("image22") 
      
    '''FriendsToHelp'''
    compare("image31")
    compare("image32")
    compare("image33")
    compare("image34")
    compare("image35")
    compare("image36")
    compare("image37")
    compare("image38")
    compare("image39")
    compare("image3a")
    compare("image3b")
    compare("image3c")
    compare("image3d")
    compare("image3e")
    
    '''SendTopic'''
    compare("image41")
    compare("image42")
    compare("image43")
    compare("image44")
    compare("image45")
    compare("image46")
    compare("image47")
    compare("image48")
    
    
    