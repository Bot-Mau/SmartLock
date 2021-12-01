import checker
import error


def changeMasterCode():
    flag = True

    count = 0

    print("Changing master passcode...\n")

    while flag:

        enteredCode = input("Enter master passcode: ")

        if checker.compareMasterCode(enteredCode):  # Use the checker class

            print("Enter new code: ")

            newCode = input()

            # Send newCode to OwnerClass to update master passCode

            flag = False

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts


def editName():
    flag = True

    count = 0

    print("Changing master name...\n")

    while flag:

        enteredCode = input("Enter master passcode: ")

        if checker.compareMasterCode(enteredCode):  # Use the checker class

            print("Enter new name: ")

            newName = input()

            # Send newCode to OwnerClass to update master passCode

            flag = False

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts
