## ###
#  IP: ???
#
##
# Generate a file containing all strings that contain cross references
# @author ???
# @category Strings
#
# Prerequisites
#
#   - Preform the Ghidra Ascii Strings Analysis
#

from ghidra.program.util import DefinedDataIterator
from ghidra.app.util import XReferenceUtil


file_name = currentProgram.getName() + "_Strings_with_xrefs.txt"

with open(file_name, "w") as file_output:
    for string in DefinedDataIterator.definedStrings(currentProgram):
        for ref in XReferenceUtil.getXRefList(string):

            data = string.getValue()
            file_output.write(data + "\n")
    
print "Data written to:", file_name
