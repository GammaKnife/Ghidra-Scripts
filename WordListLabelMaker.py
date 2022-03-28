## ###
#  IP: ???
# 
##
# Check strings in a progrm for suspect or interesting words and create a sub-label named interesting_string
# @author ???
# @category Strings
#
# Prerequisites 
#
#   - Preform the Ghidra Ascii Strings Analysis 
#

from ghidra.program.util import DefinedDataIterator
from ghidra.program.model.symbol import SourceType
from ghidra.program.database.symbol import SymbolManager


# List of strings to look for
interesting_strings = [ "shell", "username", "password", "exe", "gets", "strcpy", "stpcopy",
                    "spritf", "http", "aes", "des", "cert", "admin" ]

# Name of new sublabel
new_label = "interesting_string"

for string in DefinedDataIterator.definedStrings(currentProgram):
    for interesting_string in interesting_strings:
        
        # Get contents of the string excluding the data type information
        name = string.getValue()


        if interesting_string in str(name).lower() and string is not None:

            # Get offset of the string and check if there is already a primary symbol
            address = string.getAddress()
            prime = string.getPrimarySymbol()

            if prime is not None:
                
                # Create a new non-primary label 
                createLabel(address, new_label, False)
                
                # Debug
                print "Created New Label:", address 
            
            else:
                
                # If there is no primary symbol associated with it, create one
                createLabel(address, new_label, True)
                print "Created New Label:", address
