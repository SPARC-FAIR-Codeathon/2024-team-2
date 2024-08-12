cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, tool_extract_dep_var_sds.py]
inputs:
  xFile:
      type: File
      inputBinding:
          position: 1
          prefix: --x_file
  outputFile:
    type: File
    inputBinding:
      position: 2
      prefix: --y_file
outputs:
    yFile:
      type: File
      outputBinding:
        glob: $(input.outputFile)

# run the tool
#cwltool tool_extract_dep_var_sds.cwl input_extract_dep_var.yaml
