## ###
#  IP: ???
#
##
# Create 2 files of identifed strings in 2 ghidra instances and compares them
# @author ???
# @category Strings
#
# Prerequisites
#
#   - Preform the Ghidra Ascii Strings Analysis
#   - Install GNU Core Utils
#
# Known Limitations
#
#   - GNU Core Utils is kind of a hassle to get to work on windows

from ghidra.program.util import DefinedDataIterator
import subprocess

# Global Vars
otherProgram = askProgram("Choose a program to compare to")
program_1 = currentProgram.getName()
program_2 = otherProgram.getDomainFile().getName()


def write_and_sort(output_file, program):
    
    num_of_lines = 0
    
    # Output Strings into 2 files for comparison 
    with open(output_file, "w") as file_output:
        for string in DefinedDataIterator.definedStrings(program):
            
            num_of_lines = num_of_lines + 1
            data = string.getValue()
            file_output.write(data + "\n")

    subprocess.Popen(["sort -u " + output_file + " -o " + output_file], stdout=subprocess.PIPE, shell=True).wait()


def compare_strings(otherProgram):

    output_file_1 = currentProgram.getName() + "_Strings.txt"
    output_file_2 = otherProgram.getDomainFile().getName() + "_Strings.txt"

    write_and_sort(output_file_1, currentProgram)
    write_and_sort(output_file_2, otherProgram)

    # Compare Strings
    proc = subprocess.Popen(["comm -12 " + output_file_1 + " " + output_file_2], stdout=subprocess.PIPE, shell=True)
    
    with open("shared_strings.txt", "w") as shared_strings_file:
        shared_strings_file.writelines(proc.communicate()[0])


# Get strings in first and second program
compare_strings(otherProgram)
