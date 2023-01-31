import sys
import re

def usage():
    """
    Prints the usage message for the script.
    """
    print("Usage: python email_parser.py [service] [file]\n\nServices:\n  outlook If your eml was exported from Outlook.\n  gmail If your eml was exported from Gmail.\n  proton If your eml was exported from ProtonMail.\n  zimbra If your eml was exported from zimbra. Zimbra's files may show some errors.")

def parse_outlook(file):
    """
    Parses an eml file exported from Outlook and prints out its important headers.
    
    Args:
        file (str): Path to the eml file to be parsed.
    """
    with open(file, "r") as f:
        content = f.read()

    from_email = re.search(r'From:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content).group()
    from_email = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', from_email).group()
    print("[FROM]\t\t\t", from_email)

    replyto = re.search(r'Reply-To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content)
    if replyto:
        replyto = replyto.group()
        replyto = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', replyto).group()
        print("[Reply-To]\t\t", replyto)

    to_email = re.search(r'To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content).group()
    to_email = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', to_email).group()
    print("[TO]\t\t\t", to_email)

    source_ip = re.search(r'spf.*([0-9]{1,3}[\.]){3}[0-9]{1,3}', content)
    if source_ip:
        source_ip = source_ip.group()
        source_ip = re.search(r'([0-9]{1,3}[\.]){3}[0-9]{1,3}', source_ip).group()
        print("[IP]\t\t\t", source_ip)

    spf = re.search(r'spf.*(pass|fail)', content)
    if spf:
        spf = spf.group()
        spf = re.search(r'(pass|fail)', spf).group()
        print("[SPF]\t\t\t", spf)

def parse_gmail(file):
    """
    Parses an eml file exported from Gmail and prints out its important headers.
    
    Args:
        file (str): Path to the eml file to be parsed.
    """
    with open(file, "r") as f:
        content = f.read()

    from_email = re.search(r'Delivered-To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content).group()
    from_email = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', from_email).group()
    print("[Delivered-To]\t\t", from_email)

    return_path = re.search(r'Return-Path:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content)
    if return_path:
        return_path = return_path.group()
        return_path = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', return_path).group()
        print("[Return-Path]\t\t", return_path)

    sender = re.search(r'Sender:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content)
    if sender:
        sender = sender.group()
        sender = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', sender).group()
        print("[Sender]\t\t", sender)

    x_original_to = re.search(r'X-Original-To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content)
    if x_original_to:
        x_original_to = x_original_to.group()
        x_original_to = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', x_original_to).group()
        print("[X-Original-To]\t", x_original_to)

def parse_proton(file):
    """
    Parses an eml file exported from ProtonMail and prints out its important headers.
    
    Args:
        file (str): Path to the eml file to be parsed.
    """
    with open(file, "r") as f:
        content = f.read()

    from_email = re.search(r'From:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content).group()
    from_email = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', from_email).group()
    print("[FROM]\t\t\t", from_email)

    replyto = re.search(r'Reply-To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content)
    if replyto:
        replyto = replyto.group()
        replyto = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', replyto).group()
        print("[Reply-To]\t\t", replyto)

    to_email = re.search(r'To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content).group()
    to_email = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', to_email).group()
    print("[TO]\t\t\t", to_email)

    source_ip = re.search(r'Received:.*\b[0-9]{1,3}(\.[0-9]{1,3}){3}\b', content)
    if source_ip:
        source_ip = source_ip.group()
        source_ip = re.search(r'\b[0-9]{1,3}(\.[0-9]{1,3}){3}\b', source_ip).group()
        print("[IP]\t\t\t", source_ip)

    encryption = re.search(r'Encryption:.*\b(TLS|SSL)\b', content)
    if encryption:
        encryption = encryption.group()
        encryption = re.search(r'\b(TLS|SSL)\b', encryption).group()
        print("[Encryption]\t\t", encryption)

def parse_zimbra(file):
    """
    Parses an eml file exported from Zimbra and prints out its important headers.
    
    Args:
        file (str): Path to the eml file to be parsed.
    """
    with open(file, "r") as f:
        content = f.read()

    from_email = re.search(r'From:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content).group()
    from_email = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', from_email).group()
    print("[FROM]\t\t\t", from_email)

    replyto = re.search(r'Reply-To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content)
    if replyto:
        replyto = replyto.group()
        replyto = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', replyto).group()
        print("[Reply-To]\t\t", replyto)

    to_email = re.search(r'To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', content).group()
    to_email = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', to_email).group()
    print("[TO]\t\t\t", to_email)

    source_ip = re.search(r'spf.*([0-9]{1,3}[\.]){3}[0-9]{1,3}', content)
    if source_ip:
        source_ip = source_ip.group()
        source_ip = re.search(r'([0-9]{1,3}[\.]){3}[0-9]{1,3}', source_ip).group()
        print("[IP]\t\t\t", source_ip)

    spf = re.search(r'spf.*(pass|fail)', content)
    if spf:
        spf = spf.group()
        spf = re.search(r'(pass|fail)', spf).group()
        print("[SPF]\t\t\t", spf)

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
