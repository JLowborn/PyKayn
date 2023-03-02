import email
import os


class Export:
    def __init__(self) -> None:
        """
        ### Initializes a new instance of the Export class.

        The constructor creates a new 'exported' directory within the current
        working directory, if it doesn't already exist, to store exported files.
        """
        self.directory = os.path.join(os.getcwd(), "exported")
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def get_attachments(self, content: str) -> None:
        """
        ### Extracts attachments from email

        Extracts any attachments found within the email content and saves them
        to the 'exported' directory.

        #### Args:
            content (str): The raw text content of the email message.

        #### Returns:
            None
        """
        msg = email.message_from_string(content)

        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") is None:
                continue

            filename = part.get_filename()

            with open(os.path.join(self.directory, filename), "wb") as output:
                output.write(part.get_payload(decode=True))
