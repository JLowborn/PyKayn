# Kain Python

Kain is a comprehensive metadata parser designed specifically for parsing EML files. It provides an efficient means of obtaining crucial information, including SPF, DMARC, DKIM, source IP, and addresses, to aid in forensic investigations. It is important to note that the syntax of EML files may vary based on the email service they were exported from. Currently, Kain supports Outlook, Gmail, Zimbra, and Proton syntax, however it may not be compatible with EML files from other sources. Additionally, this is an early version of the tool and there may be some errors present. Nevertheless, it is a valuable tool for forensic experts.

![Demo](https://user-images.githubusercontent.com/64245567/217329028-cbfa8923-2d20-410b-8d5b-de29526208d2.png)

## Usage :man_technologist::

**`kain.py -s <service> -f <file>`**

The **`-s`** indicates which service provided the EML file. Current available service options are **Outlook**, **Gmail**, **Proton** or **Zimbra**. The
**`-f`** indicates which file will be parsed.

[![asciicast](https://asciinema.org/a/6LOYenBNZv4XmHOywU2OGL3ir.svg)](https://asciinema.org/a/6LOYenBNZv4XmHOywU2OGL3ir)

## Credits :star::
All credits goes to the original tool creator and the original repository can be found [here](https://github.com/rf-peixoto/kain).
