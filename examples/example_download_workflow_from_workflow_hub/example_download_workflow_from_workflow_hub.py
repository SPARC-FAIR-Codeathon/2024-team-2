
from sparc_assemble.plugin.workflow_hub import WorkflowHub

if __name__ == "__main__":
    zip_url = "https://workflowhub.eu/workflows/776/ro_crate?version=1"
    workflow_hub = WorkflowHub(zip_url)

    # generate ZIP filename
    zip_filename = workflow_hub.generate_zip_filename(zip_url)
    local_zip_path = zip_filename + '.zip'

    # Download the ZIP file
    workflow_hub.download_zip_file(zip_url, local_zip_path)

    # Unzip the entire contents of the ZIP archive
    output_directory = zip_filename
    workflow_hub.unzip_folder(local_zip_path, output_directory)