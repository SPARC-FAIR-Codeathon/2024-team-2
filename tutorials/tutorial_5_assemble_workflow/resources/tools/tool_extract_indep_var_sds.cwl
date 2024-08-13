cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, tool_extract_indep_var_sds.py]
inputs:
  datasetId:
    type: float
    inputBinding:
      position: 1
      prefix: --datasetId
  versionId:
    type: float
    inputBinding:
      position: 2
      prefix: --versionId

outputs:
  x_file:
      type: File


