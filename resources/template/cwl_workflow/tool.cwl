cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, tool.py]
inputs:
  input_folder:
    type: Directory
    inputBinding:
      position: 1
      prefix: --input-folder
  output_folder:
    type: Directory
    inputBinding:
      position: 2
      prefix: --output-folder
outputs: []
#outputs:
#  sds_dicom:
#    type: Directory
#    outputBinding:
##      glob: $(inputs.output_folder.path)/sds_dicom
##      glob: "./*"

#requirements:
#  InlineJavascriptRequirement: {}


# run the tool
#cwltool tool.cwl --input_folder ../resources/example_raw_dataset --output_folder ./digraph
