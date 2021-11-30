import checker
import error


def addGuestCode():
    flag = True

    count = 0

    print("Adding guest code...\n")

    while flag:

        enteredCode = input("Enter master passcode: ")

        if checker.compareMasterCode(enteredCode):  # Use the checker class

            print("Enter new guest code: ")

            flag = False

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts


def changeGuestCode():
    flag = True

    count = 0

    print("Changing guest code...\n")

    while flag:

        enteredCode = input("Enter master passcode: ")

        if checker.compareMasterCode(enteredCode):  # Use the checker class

            print("Enter new guest code: ")

            newCode = input()

            # Send newCode to OwnerClass to update guest passcode

            flag = False

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts


def addGuestName():
    flag = True

    count = 0

    while flag:

        enteredPasscode = input("Enter master passcode: ")

        if checker.compareMasterCode(enteredPasscode):  # Use the checker class

            print("Enter new guest name: ")

            newName = input()

            # Send newName to logs to add the guest name

            flag = False

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts


def removeGuestName():
    flag = True

    count = 0

    while flag:

        enteredPasscode = input("Enter master passcode: ")

        if checker.compareMasterCode(enteredPasscode):  # Use the checker class

            print("Enter guest name: ")

            newName = input()

            # Send newName to logs to remove the guest name

            flag = False

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts


def editGuestName():
    flag = True

    count = 0

    while flag:

        enteredPasscode = input("Enter master passcode: ")

        if checker.compareMasterCode(enteredPasscode):  # Use the checker class

            print("Editing Guest Name\n")

            removeGuestName()

            addGuestName()

            flag = False

        else:

            print("Incorrect passcode...\n")

            count += 1

            error.error(count)  # Sending count number to the Error class to check for attempts
