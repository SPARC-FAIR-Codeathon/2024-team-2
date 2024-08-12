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
outputs: []

requirements:
  InitialWorkDirRequirement:  # Ensure Python script available in current working directory
    listing:
     - class: File
       basename: "tool_extract_indep_var_sds.py"
       contents: |
         datasetId=262
         versionId=1.1

# run the tool
#cwltool tool_extract_indep_var_sds.cwl input_extract_indep_var.yaml
