from __future__ import division
from math import *
numTilings = 8
  
def tilecode(x,y,tileIndices):
    
    for i in range(0,numTilings):
        
        #Moving x and y based on the tile
        newX = x + (0.6*(1/8))*i
        newY = y + (0.6*(1/8))*i
        
        #Finding out which tile the new X and Y fall into 
        newX = newX /0.6
        newY = newY/0.6
        
        #Moving the index of new x to match the array index
        newX = newX + (121*i)
        
        #Flooring answers to see which tile x and y are in 
        newX = floor(newX)
        newY = floor(newY)
        
        #Counting up from x based on y
        tileIndices[i] = newX + (11 * newY )
        
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
