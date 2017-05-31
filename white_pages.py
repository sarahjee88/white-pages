print ("\n\nWelcome!") # Print single line
print """
\nThis program creates text file if you
type in some informations.
It won't take too long...

Enjoy!
""" # Print multiple lines

response = raw_input("*** To continue, press ENTER. ***") # Make variable called response with line of texts

if response == "": # If variable eqauls nothing, run the codes below
    filename = raw_input("\nFirst, set a Filename:") # Make variable called filename with line of texts
    print"""

    --------------------------------------------------------
    Informations you typed in will be saved in the text file
    with a filename you just set right before.
    --------------------------------------------------------

    Now you will type in informations of three people you want...
    """ # Print multiple lines
    with open (filename + ".txt", "w") as f: # Open file with name that user set, and write

        per1 = raw_input("First person's name:") # Make variable called per1 with line of texts
        f.write(per1 + "\n") # Type in per1 with newline inside the text file
        birth1 = raw_input("First person's birthday:") # Make variable called birth1 with line of texts
        f.write(birth1 + "\n") # Type in birth1 with newline inside the text file
        pnum1 = raw_input("First person's phonenumber:") # Make variable called pnum1 with line of texts
        f.write(pnum1 + "\n\n\n") # Type in pnum1 with multiple newlines inside the text file

        per2 = raw_input("Second person's name:") # Make variable called per2 with line of texts
        f.write(per2 + "\n") # Type in per2 with newline inside the text file
        birth2 = raw_input("Second person's birthday:") # Make variable called birth2 with line of texts
        f.write(birth2 + "\n") # Type in birth2 with newline inside the text file
        pnum2 = raw_input("Second person's phonenumber:") # Make variable called pnum2 with line of texts
        f.write(pnum2 + "\n\n\n") # Type in pnum2 with multiple newlines inside the text file

        per3 = raw_input("Third person's name:" ) # Make variable called per3 with line of texts
        f.write(per3 + "\n") # Type in per3 with newline inside the text file
        birth3 = raw_input("Third person's birthday:") # Make variable called birth3 with line of texts
        f.write(birth3 + "\n") # Type in birth3 with newline inside the text file
        pnum3 = raw_input("Third person's phonenumber:") # Make variable called pnum3 with line of texts
        f.write(pnum3 + "\n\n\n") # Type in pnum3 with multiple newlines inside the text file

    print ("Thank you. Check the file if it's all saved.") # Print single line
    f.close() # Save and close the file
