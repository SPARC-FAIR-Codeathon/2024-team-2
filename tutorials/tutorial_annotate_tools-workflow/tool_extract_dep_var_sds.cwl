cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, tool_extract_dep_var_sds.py]
inputs:
    xFile:
        type: File
        inputBinding:
            position: 1
            prefix: --xFile
    outputFile:
        type: File
        inputBinding:
            position: 2
            prefix: --outputFile

outputs:
    yFile:
        type: File
        outputBinding:
            glob: $(input.outputFile)

requirements:
    InitialWorkDirRequirement:
        listing:
          - class: File
            basename: "tool_extract_dep_var_sds.py"
            contents: |
                xFile='time.txt'
                outputFile='voltage.txt'

# run the tool
#cwltool tool_extract_dep_var_sds.cwl input_extract_dep_var.yaml
