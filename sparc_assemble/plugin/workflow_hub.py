import requests
from zipfile import ZipFile
import os
from urllib.parse import urlparse, parse_qs


class WorkflowHub:
    def __init__(self, zip_url):
        """
        Initialize the WorkflowHub with the provided configuration.

        :param config: Dictionary containing zip_url, local_zip_path, and output_directory.
        """
        self._zip_url = zip_url

    def download_zip_file(self, url: str, local_filename: str) -> None:
        """
        Downloads a ZIP file from a specified URL and saves it locally.

        :param url: URL of the ZIP file to download.
        :param local_filename: Local file path where the ZIP file will be saved.
        """

        try:
            # Download the file
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(local_filename, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f"ZIP file downloaded successfully and saved as '{local_filename}'.")
            else:
                print(f"Failed to download the file. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred while downloading the file. Error: {e}")


    def unzip_folder(self, zip_path: str, output_dir: str) -> None:
        """
        Extracts all files from a ZIP archive to a specified directory.

        :param zip_path: Path to the ZIP file.
        :param output_dir: Directory where the files will be extracted.
        """
        try:
            with ZipFile(zip_path, 'r') as zip_file:
                # Ensure output directory exists
                os.makedirs(output_dir, exist_ok=True)

                # Extract all files to the output directory
                zip_file.extractall(output_dir)

                print(f"All files from the ZIP archive have been extracted to '{output_dir}'.")
        except Exception as e:
            print(f"An error occurred while processing the ZIP archive. Error: {e}")

    def generate_zip_filename(self, url: str) -> str:
        """
        Generates a ZIP filename based on the URL.

        :param url: URL of the ZIP file.
        :return: Generated ZIP filename.
        """
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # Extract workflow ID and version from URL parameters
        workflow_id = parsed_url.path.split('/')[2]  # Assuming the path structure is /workflows/{id}/ro_crate
        version = query_params.get('version', ['1'])[0]  # Default to '1' if not specified

        # Create a formatted ZIP filename
        zip_filename = f"workflow-{workflow_id}-{version}.crate"
        return zip_filename


if __name__ == "__main__":
    zip_url = "https://workflowhub.eu/workflows/776/ro_crate?version=1"
    workflow_hub = WorkflowHub(zip_url)

    # generate ZIP filename
    zip_filename = workflow_hub.generate_zip_filename(zip_url)
    local_zip_path = zip_filename+'.zip'

    # Download the ZIP file
    workflow_hub.download_zip_file(zip_url, local_zip_path)

    # Unzip the entire contents of the ZIP archive
    output_directory = zip_filename
    workflow_hub.unzip_folder(local_zip_path, output_directory)
