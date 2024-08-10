cwlVersion: v1.2
class: Workflow
inputs:
  input_folder:
    type: Directory

  output_folder:
    type: Directory

outputs: []


steps:
  # step 1
  import:
    run: tool.cwl
    in:
      input_folder: input_folder
      output_folder: output_folder
    out: []
