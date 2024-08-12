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
    outputFile:
        type: File
        inputBinding:
            position: 3
            prefix: --outputFile
outputs:
    xFile:
        type: Directory
        outputBinding:
            glob: $(input.outputFile)

requirements:
    InitialWorkDirRequirement:
        listing:
          - class: File
            basename: "tool_extract_indep_var_sds.py"
            contents: |
                datasetId=262
                versionId=1.1
                outputFile='time.txt'

# run the tool
#cwltool tool_extract_indep_var_sds.cwl input_extract_indep_var.yaml
