from typing import Union
import argparse
import os

from kain import Outlook, Gmail, Zimbra, Proton
from kain.constants import *


def main() -> None:
    # The main function
    args = parse_args()

    if not args.no_banner:
        banner()

    service = create_service(*args.file, *args.service)
    headers = service.get_headers()

    for k, v in headers.items():
        color = RED if v == "fail" else GREEN
        print(f"{color}{'[' + k + ']':<15}{RESET} {v}")


def parse_args() -> None:
    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Parse EML files.")
    parser.add_argument("-f", "--file", required=True, nargs=1, metavar="FILENAME",
                        help="email header file to be parsed", type=validate_file)
    parser.add_argument("-s", "--service", required=True, nargs=1, metavar="SERVICE",
                        help="email provider to be used", choices=("outlook", "zimbra", "proton", "gmail"))
    parser.add_argument("-o", "--output", required=False, nargs=1,
                        metavar="FILENAME", help="output results to a json file")
    parser.add_argument("--no-banner", required=False,
                        action='store_true', help="don't show banner")
    args = parser.parse_args()

    return args


def create_service(file: str, service: str) -> Union[Outlook, Zimbra, Proton, Gmail]:
    # Create email instance
    if service == "outlook":
        return Outlook(file)
    elif service == "zimbra":
        return Zimbra(file)
    elif service == "proton":
        return Proton(file)
    elif service == "gmail":
        return Gmail(file)


def validate_file(file) -> str:
    # Validate file existence
    if not os.path.exists(file):
        raise argparse.ArgumentError(f"{file} does not exist")
    return file


def banner() -> None:
    # Prints a banner
    print(f"{GREEN} __________          ____  __.        .__          \n",
          "\______   \ ___.__.|    |/ _|_____   |__|  ____   \n",
          " |     ___/<   |  ||      <  \__  \  |  | /    \  \n",
          " |    |     \___  ||    |  \  / __ \_|  ||   |  \ \n",
          " |____|     / ____||____|__ \(____  /|__||___|  / \n",
          "            \/             \/     \/          \/  \n",
          f"  v1.0            EML Parser{RESET}\n")


def run() -> None:
    # Calling the main function
    main()


if __name__ == "__main__":
    run()
