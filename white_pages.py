print ("\n\nWelcome!")
print """
\nThis program creates text file if you
type in some informations.
It won't take too long...

Enjoy!
"""
response = raw_input("*** To continue, press ENTER. ***")

if response == "":
    filename = raw_input("\nFirst, set a Filename:")
    print"""

    --------------------------------------------------------
    Informations you typed in will be saved in the text file
    with a filename you just set right before.
    --------------------------------------------------------

    Now you will type in informations of three people you want...
    """
    with open (filename, "w") as f:

        per1 = raw_input("First person's name:")
        f.write(per1 + "\n")
        birth1 = raw_input("First person's birthday:")
        f.write(birth1 + "\n")
        pnum1 = raw_input("First person's phonenumber:")
        f.write(pnum1 + "\n\n\n")

        per2 = raw_input("Second person's name:")
        f.write(per2 + "\n")
        birth2 = raw_input("Second person's birthday:")
        f.write(birth2 + "\n")
        pnum2 = raw_input("Second person's phonenumber:")
        f.write(pnum2 + "\n\n\n")

        per3 = raw_input("Third person's name:" )
        f.write(per3 + "\n")
        birth3 = raw_input("Third person's birthday:")
        f.write(birth3 + "\n")
        pnum3 = raw_input("Third person's phonenumber:")
        f.write(pnum3 + "\n\n\n")

    print ("Thank you. Check the file if it's all saved.")
    f.close()
