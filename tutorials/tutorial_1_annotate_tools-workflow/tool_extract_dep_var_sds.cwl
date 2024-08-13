cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, ../tool_extract_dep_var_sds.py]
inputs:
  x_file:
      type: File
      inputBinding:
          position: 1
<<<<<<< HEAD:tutorials/tutorial_1_annotate_tools-workflow/tool_extract_dep_var_sds.cwl
          prefix: --xFile
  outputFile:
    type: string
    inputBinding:
      position: 2
      prefix: --outputFile
=======
          prefix: --x_file

>>>>>>> 628e10f00e2ef94ec25584c0dd9f96d542a1b0fd:tutorials/tutorial_5_assemble_workflow/resources/tools/tool_extract_dep_var_sds.cwl
outputs:
  y_file:
      type: File

