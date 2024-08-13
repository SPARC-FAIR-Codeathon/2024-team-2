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
    type: string
    inputBinding:
      position: 2
      prefix: --y_file
outputs:
  yFile:
    type: File
    outputBinding:
      glob: "$(runtime.outdir)/$(inputs.outputFile)"

requirements:
  InlineJavascriptRequirement: {}
  InitialWorkDirRequirement:  # Ensure Python script available in current working directory
    listing:
     - class: File
       basename: "tool_extract_dep_var_sds.py"
       contents: |
         datasetId=262
         versionId=1.1
         outputFile='voltage.txt'
     - class: File
       path: resources/voltage.txt
       basename: "voltage.txt"
       contents: ""

# run the tool
#cwltool tool_extract_dep_var_sds.cwl input_extract_dep_var.yaml
