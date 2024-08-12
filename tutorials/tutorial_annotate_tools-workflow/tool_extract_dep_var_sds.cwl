cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, tool_extract_dep_var_sds.py]
inputs:
  x_file:
      type: File
      inputBinding:
          position: 1
          prefix: --x_file
outputs: []

#requirements:
#  InitialWorkDirRequirement:  # Ensure Python script available in current working directory
#    listing:
#     - class: File
#       basename: "tool_extract_dep_var_sds.py"
#       content: |
#         x_file: 'outputs/time.txt'

# run the tool
#cwltool tool_extract_dep_var_sds.cwl input_extract_dep_var.yaml
