def try1():
    try:
        print(x)
    except:
        print("An exception occurred")
        
################ raises a NameError and another for other errors##########################
def try2_manyError():
    try:
      print(x)
    except NameError:
     print("Variable x is not defined")
    except:
        print("Something else went wrong")
        
# try2_manyError()
##################Else###################
def try3_Else():
#     You can use the else keyword to define a block of code to be executed if no errors were raised:
# In this example, the try block does not generate any error:
    try:
        print("Hello")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")
# try3_Else()

##################Finally###################
def try4_Finally():
    # Try to open and write to a file that is not writable:

    try:
        f = open("demofile.txt")
        try:
            f.write("Lorum Ipsum")
        except:
          print("Something went wrong when writing to the file")
        finally:
            f.close()
    except:
         print("Something went wrong when opening the file")


# try4_Finally()



###########Raise an exception#############
#Raise an error and stop the program if x is lower than 0:


def try5_Raise():
    x = -1

    if x < 0:
        raise Exception("Sorry, no numbers below zero")

# try5_Raise()
############RAise a type error###################
def try6_typeError():
    x = "hello"

    if not type(x) is int:
      raise TypeError("Only integers are allowed")

# try6_typeError()






