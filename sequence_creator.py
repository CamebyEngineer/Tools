#! /usr/bin/python3

"""Mining Sequence Generator. 
    Author: C Saunders
    Created: March 2018
    Contact: chris.saunders@yancoal.com.au

    Purpose
        Simplify the creation of mining sequence generation for the XPAC 
        long term model. 

    Version 
        Verison 1 

    Description
        Requires a list of validation blocks to be exported from XPAC.
        and saved in the script directory as 'mine plan.csv'.
        Delivers output to stdout which needs ot be redirected to a file. 
    
    Requirements
        'mine plan.csv' must be in the format C, Strip, Block>Seam, Pil Number
        Otherwise you'll need to rename the row indexes for the dictionary

    Todo
        * Consider parseing arguements for location of inputs and outputs.
        * Consider comandline access to generator sequence function.
            -> that's a dumb idea. 
        * Consider reformating to if name = '__main__' format.
        * General Code Cleanup / Check if compliant with PEP 8
        * Crap! Need to teach it to count backwards. B68 --> B01
"""

import csv

SeamList = ["KG1",
            "KG2",
            "KG3",
            "KG4",
            "MA1U",
            "MA1",
            "MA2T",
            "MA2B",
            "MA3U",
            "MA3",
            "MA4",
            "NG1U",
            "NG1L",
            "NG2",
            "NG3",
            "NG4",
            "NG5",
            "NG6",
            "KG7"]


with open("mine plan.csv") as infile:
    reader = csv.reader(infile)
    mydict = {f'{rows[1]}\\{rows[2]}\\{rows[3]}\\{rows[4]}':rows[5] for rows in reader}

def generateSequence(startStrip, endStrip, startBlock, endBlock):
    for strip in range (startStrip, endStrip+1):
        for block in range(startBlock, endBlock+1):
            for seam in SeamList:
                miningseam = f'C\\S{strip:02d}\\B{block:02d}\\{seam}'
                if miningseam in mydict:
                    print(f'1{mydict[miningseam]}:{miningseam},214 Wash')



# use statements of the format
# generateSequence(startStrip, endStrip, startBlock, endBlock):
# Easiest way after that would be to run in terminal and redirect to output.
# use python3 sequence_generator.py > output.txt


#LtWash 1
####################################################################################################
# PIT 1
# keep from previous
# Pit 2
for strip in range(907,912):                    # drop in center pit
    generateSequence( strip, strip, 57, 68)     # blocks 57-68
    generateSequence( strip, strip, 1, 6)       # then back over the block 1 line
for strip in range(1,63):                       # continue past strip 1 
    generateSequence( strip, strip, 57, 68)     # blocks 57-68
    generateSequence( strip, strip, 1, 6)       # then back over the block 1 line

# #LtWash 2
# ####################################################################################################
# # PIT 1
# generateSequence( 25, 45, 15, 28)             # drop in on eastern pit
# generateSequence( 46, 89, 20, 28)             # step in to leave behind smaller pit to minimise final void.
# # PIT 2
# generateSequence( 14, 70, 45, 56)             # drop in on western most edge pit. 
# # PIT 3  
# generateSequence( 46, 89, 15, 19)             # last pit — small one between cdm and eastern pit.
