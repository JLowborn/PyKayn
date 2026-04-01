# Python Kain

## Description:
Kain is a specialized metadata parser built in Python, designed to streamline the analysis of .eml files during digital forensic investigations. It automates the extraction of critical security headers and authentication records, providing investigators with a clear view of an email's origin and integrity.

## Key Features:

- Authentication Parsing: Extract and validate SPF, DKIM, and DMARC records.  
- Origin Tracking: Quickly identify the Source IP and sender addresses.  
- Multi-Platform Support: Tailored syntax handling for Gmail, Outlook, Proton, and Zimbra.  
- Forensic Efficiency: Designed to reduce manual header analysis time.

**Note:** This is an early-stage tool. While optimized for major providers, parsing variations may occur with EML files from unsupported services.

## Quick Start :man_technologist::

**`kain.py -s <service> -f <file>`**

The **`-s`** indicates which service provided the EML file. Current available service options are **Outlook**, **Gmail**, **Proton** or **Zimbra**. The
**`-f`** indicates which file will be parsed.

![Demo](https://user-images.githubusercontent.com/64245567/217329028-cbfa8923-2d20-410b-8d5b-de29526208d2.png)

## Credits :star::
All credits goes to the original tool creator and the original repository can be found [here](https://github.com/rf-peixoto/kain).
