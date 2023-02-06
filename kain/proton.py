class Proton:
    def __init__(self, file):
        self.file = file
        self.from_ = self._get_value("From: ")
        self.replyto = self._get_value("Received: from").split(" ")[3]
        self.to = self._get_value("To: ")
        self.source_ip = self._get_value("SPF").split(" ")[0]
        self.spf = self._get_value("spf").split(" ")[7].split("=")[1]
        self.dmarc = self._get_value("dmarc").split(" ")[7].split("=")[1]
        self.dkim = self._get_value("dkim=").split(" ")[7].split("=")[1]

    def _get_value(self, keyword):
        value = None
        with open(self.file) as f:
            for line in f:
                if keyword in line:
                    value = line.strip()
                    break
        return value

    def get_email_header(self):
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
    gmail = Gmail("/home/rebellion/Área de trabalho/Kain/samples/hi.eml")