import checker
import error


def initializeUI():


#All the commands needed to initialize and start the UI for the program 

def showMasterUI():
    flag = True

    count = 0

    while flag:

        enteredCode = input("Enter master passcode: ")

        if checker.compareMasterCode(enteredCode):

        #Display all master UI settings and options

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts


def showSettingsUI():
    flag = True

    count = 0

    while flag:

        enteredCode = input("Enter master passcode: ")
        
        if checker.compareMasterCode(enteredCode):

        # Display all settings UI settings and options, only available to master user

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts

