from core import Core
from typing import Union, Dict, List
import re

# FIXME: The code returns only the first receiver in case of more than one. 

class Gmail:
    def __init__(self, filename: str) -> None:
        """
        Initialize Gmail class with email file name.

        Args:
            filename (str): The name of the email file.

        Returns:
            None
        """
        self.header_patterns = {
            "From": [r'From:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b'],
            "Reply-To": [r'Reply-To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b'],
            "To": [r'^To:.*\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b', r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b'],
            "Source IP": [r'spf.*([0-9]{1,3}[\.]){3}[0-9]{1,3}', r'([0-9]{1,3}[\.]){3}[0-9]{1,3}'],
            "SPF": [r'SPF.*(pass|fail)', r'(pass|fail)'],
            "DMARC": [r'DMARC.*(pass|fail)', r'(pass|fail)'],
            "DKIM": [r'DKIM.*(pass|fail)', r'(pass|fail)'],
        }
        self.content = Core.reader(filename)
        self.from_ = self._get_value("From")
        self.replyto = self._get_value("Reply-To")
        self.to = self._get_value("To")
        self.source_ip = self._get_value("Source IP")
        self.spf = self._get_value("SPF")
        self.dmarc = self._get_value("DMARC")
        self.dkim = self._get_value("DKIM")

    def _get_value(self, keyword: str) -> Union[None, List[str]]:
        """
        Extract a header field value from the email content.

        Matches the email content against the regular expression patterns in `header_patterns` for the specified keyword and returns the first match.

        Args:
            keyword (str): The header field to be extracted.

        Returns:
            Union[None, List[str]]: The extracted header field value, or None if no match is found.
        """
        patterns = self.header_patterns[keyword]
        content = self.content
        try:
            for pattern in patterns:
                content = re.search(pattern, content, re.IGNORECASE|re.MULTILINE).group()
            return content
        except AttributeError:
            return

    def get_headers(self) -> Dict[str, Union[str, None]]:
        """
        Read the content of an email file.

        This method uses the `reader` method of the `Core` class to read the content of an email file and returns it as a string.

        Returns:
            dict: A dictionary of email header fields and their values.
        """
        return {
            "From": self.from_,
            "Reply-To": self.replyto,
            "To": self.to,
            "Source IP": self.source_ip,
            "SPF": self.spf,
            "DMARC": self.dmarc,
            "DKIM": self.dkim,
        }

if __name__ == "__main__":
    from pprint import pprint as pp
    gmail = Gmail(filename="/home/rebellion/Área de trabalho/Kain/samples/good_day.eml")
    pp(gmail.get_headers())