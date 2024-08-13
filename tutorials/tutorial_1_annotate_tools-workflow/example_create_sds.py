import sparc_flow

new_tool = sparc_flow.Tool()

# name of your tool
new_tool.set_tool_name("tool_extract_indep_var_sds_test")

# directory of where your tool was saved
new_tool.set_tool_dir(".")

# creates sds dataset in the first file path argument, whilst duplicating the contents of the
# second file path argument in dataset > primary > tools
new_tool.create_sds("../resources/tutorial_1_resources/mock_dataset", ".")
