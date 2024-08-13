cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, ../tool_extract_dep_var_sds.py]
inputs:
  x_file:
      type: File
      inputBinding:
          position: 1
          prefix: --x_file

outputs:
  y_file:
      type: File

