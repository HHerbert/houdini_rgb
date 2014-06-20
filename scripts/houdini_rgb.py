'''
Created on 09/06/2014

@author: herbert
'''

import hou

##########  global variables ############
blackShader = hou.node('/shop/constant_black')
redShader = hou.node('/shop/constant_red')
greenShader = hou.node('/shop/constant_green')
blueShader =  hou.node('/shop/constant_blue')


def blackAssign():
############ create black shader ####
    if blackShader.name() == "constant_black":
        blackShader.destroy()
        constant = hou.galleries.galleryEntries('constant')[0]
        constant.createChildNode(hou.node("/shop")).setName('constant_black')
        hou.parmTuple('/shop/constant_black/difclr').set((0,0,0))
    else:
        constant = hou.galleries.galleryEntries('constant')[0]
        constant.createChildNode(hou.node("/shop")).setName('constant_black')
        hou.parmTuple('/shop/constant_black/difclr').set((0,0,0))    

############# select objects assign black shader ##################    
    candidateObjects = hou.parm('vobject')
    canEval = candidateObjects.eval()
    allNodes = hou.node("/obj").recursiveGlob(canEval, filter=hou.nodeTypeFilter.ObjGeometry)
    #print allNodes   
    for i in allNodes:
        objNode = hou.node("/obj/" + str(i))
        print i
        objNode.setParms({"/obj/" + str(i) + "/shop_materialpath": '/shop/constant_black'})

blackAssign()

########################## red matte ###################################################3
def rAssign():
    
    #### create red shader ####
    if redShader.name() == "constant_red":
        redShader.destroy()
        constant = hou.galleries.galleryEntries('constant')[0]
        constant.createChildNode(hou.node("/shop")).setName('constant_red')
        hou.parmTuple('/shop/constant_red/difclr').set((1,0,0))
    else:
        constant = hou.galleries.galleryEntries('constant')[0]
        constant.createChildNode(hou.node("/shop")).setName('constant_red')
        hou.parmTuple('/shop/constant_red/difclr').set((1,0,0))
        
    ##### assign red shader #####
    redParm = hou.parm('red_matte')
    redList = redParm.eval()
    allNodes = hou.node("/obj").recursiveGlob(redList, filter=hou.nodeTypeFilter.ObjGeometry)
    #print allNodes   
    for i in allNodes:
        objNode = hou.node("/obj/" + str(i))
        print i
        objNode.setParms({"/obj/" + str(i) + "/shop_materialpath": '/shop/constant_red'})
 

rAssign() 
    
#################################### green matte #####################################################
def gAssign():
    
    #### create red shader ####
    if greenShader.name() == "constant_green":
        greenShader.destroy()
        constant = hou.galleries.galleryEntries('constant')[0]
        constant.createChildNode(hou.node("/shop")).setName('constant_green')
        hou.parmTuple('/shop/constant_green/difclr').set((0,1,0))
    else:
        constant = hou.galleries.galleryEntries('constant')[0]
        constant.createChildNode(hou.node("/shop")).setName('constant_green')
        hou.parmTuple('/shop/constant_green/difclr').set((0,1,0))
        
    ##### assign red shader #####
    greenParm = hou.parm('green_matte')
    greenList = greenParm.eval()
    allNodes = hou.node("/obj").recursiveGlob(greenList, filter=hou.nodeTypeFilter.ObjGeometry)
    #print allNodes   
    for i in allNodes:
        objNode = hou.node("/obj/" + str(i))
        print i
        objNode.setParms({"/obj/" + str(i) + "/shop_materialpath": '/shop/constant_green'})
 
gAssign() 

############################### blue matte ###################################################
def bAssign():
    
    #### create red shader ####
    if blueShader.name() == "constant_blue":
        blueShader.destroy()
        constant = hou.galleries.galleryEntries('constant')[0]
        constant.createChildNode(hou.node("/shop")).setName('constant_blue')
        hou.parmTuple('/shop/constant_blue/difclr').set((0,0,1))
    else:
        constant = hou.galleries.galleryEntries('constant')[0]
        constant.createChildNode(hou.node("/shop")).setName('constant_blue')
        hou.parmTuple('/shop/constant_blue/difclr').set((0,0,1))
        
    ##### assign red shader #####
    blueParm = hou.parm('blue_matte')
    blueList = blueParm.eval()
    allNodes = hou.node("/obj").recursiveGlob(blueList, filter=hou.nodeTypeFilter.ObjGeometry)
    #print allNodes   
    for i in allNodes:
        objNode = hou.node("/obj/" + str(i))
        print i
        objNode.setParms({"/obj/" + str(i) + "/shop_materialpath": '/shop/constant_blue'})
 
bAssign() 

