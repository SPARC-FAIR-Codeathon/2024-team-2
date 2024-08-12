cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, tool_extract_dep_var_sds.py]
inputs:
  x:
    type:
      type: array
      items: float
    inputBinding:
      position: 1
      prefix: --x_file
outputs: []

requirements:
  InitialWorkDirRequirement:  # Ensure Python script available in current working directory
    listing:
     - class: File
       basename: "tool_extract_dep_var_sds.py"
       content: |
         x: np.loadtxt('outputs/time.txt', delimiter=',')

# run the tool
#cwltool tool_extract_dep_var_sds.cwl --x x
