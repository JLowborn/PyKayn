from kain import Gmail
import sys

def main(args):
    """
    Main function of the script. Calls the appropriate parser based on the service specified in the command line arguments.
    
    Args:
        args (List[str]): Command line arguments passed to the script.
    """
    if len(args) != 3:
        usage()
        sys.exit(1)

    service = args[1]
    file = args[2]

    try:
        with open(file, 'r') as f:
            _ = f.read()
    except FileNotFoundError:
        print(f"Error: The file {file} could not be found.")
        sys.exit(1)

    if service == "outlook":
        parse_outlook(file)
    elif service == "gmail":
        parse_gmail(file)
    elif service == "proton":
        parse_proton(file)
    elif service == "zimbra":
        parse_zimbra(file)
    else:
        print("Invalid service:", service)
        usage()
        sys.exit(1)

    

if __name__ == "__main__":
    main(sys.argv)