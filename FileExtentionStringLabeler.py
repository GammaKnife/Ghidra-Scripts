## ###
#  IP: ???
# 
##
# Rename labels of strings that contain defined file extentions to be more descriptive 
# @author ???
# @category Strings
#
# Prerequisites 
#
#   - Preform the Ghidra Ascii Strings Analysis 
#
# Known Limitations
# 
#   - Strings such as ".comment" or similar might be included in labeling
#   - To correct for this behavior you can manually review changed labels or simply update them as you see them
#

from ghidra.program.util import DefinedDataIterator
from ghidra.program.model.symbol import SourceType
from ghidra.program.database.symbol import SymbolManager
import re


file_extensions = [ ".xml", ".htm", ".doc", ".jp", ".png", ".gif", ".js",
                    ".c", ".CPP", ".bin", ".exe", ".bin", ".elf", ".dll" ]

for string in DefinedDataIterator.definedStrings(currentProgram):
    for extention in file_extensions:
        # Get contents of the string excluding the data type information
        name = string.getValue()

        if extention in str(name) and string is not None:

            # Get offset of the string and check if there is already a primary symbol
            address = string.getAddress()
            prime = string.getPrimarySymbol()

            cleaned_string = re.sub(r'[^\x20-\x7e]',r'', str(name))

            if prime is not None:
                
                # Get Primary label of the string, and change the label to the value of the string 
                prime.setName(cleaned_string, SourceType.USER_DEFINED)
                
                # Debug
                print "Changed Label:", address, cleaned_string
            
            else:
                
                # If there is no label, create one
                createLabel(address, cleaned_string, True)
                print "Create New Label:", address, cleaned_string
