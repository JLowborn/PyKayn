from typing import Union

class FileNotFoundException(Exception):
    """Custom exception to raise when the file is not found."""

class Core:

    @staticmethod
    def reader(filename: str) -> Union[str, None]:
        """
        Read the content of a file and return it.

        This function reads the content of a file with the given `filename` and returns it as a string. The file is opened with encoding 'latin-1' for reading. If the file is not found, a `FileNotFoundException` is raised.

        Args:
            filename (str): The name of the file to be read.

        Returns:
            str: The content of the file as a string.

        Raises:
            FileNotFoundException: If the file is not found.
        """
        try:
            with open(filename, 'r', encoding='latin-1') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            raise FileNotFoundException(f"File '{filename}' not found.")