import sys
import actionner

def main():
    # Check if the user gave arguments with the command
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "help"):
            actionner.help()
        elif(sys.argv[1] == "check"):
            actionner.check()
        elif(sys.argv[1] == "add"):
            if(len(sys.argv) > 2):
                actionner.add(sys.argv[2])
            else:
                print("Please specify a host to add")
        elif(sys.argv[1] == "list"):
            actionner.list()
        elif(sys.argv[1] == "remove"):
            if(len(sys.argv) > 2):
                actionner.remove(sys.argv[2])
            else:
                print("Please specify a host to remove")
        else:
            print("Unknown command")
            print("Use the 'help' command to see a list of available commands")
    # If the user didn't give any arguments, ask for a command
    else:
        actionner.help()
        print()
        command = input("What do you want to do?: ")
        print()
        args = command.split()

        if(args[0] == "help"):
            actionner.help()
        elif(args[0] == "add"):
            if(len(args) > 1):
                actionner.add(args[1])
            else:
                print("Please specify a host to add")
        elif(args[0] == "check"):
            actionner.check()
        elif(args[0] == "list"):
            actionner.list()
        elif(args[0] == "remove"):
            if(len(args) > 1):
                actionner.remove(args[1])
            else:
                print("Please specify a host to remove")
        else:
            print("Unknown command")
            print("Use the 'help' command to see a list of available commands")

# Main
if(__name__ == "__main__"):
    main()


    
    
    

