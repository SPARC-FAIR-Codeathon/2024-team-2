To populate a knowledge graph:

1. Put the json tools description in the resources/tools folder (see tools_description template.json for the structure)
2. Run the following command from the main folder of the project (where the requirements.txt file is located):
``` 
python populate_knowledge_graph.py ----ontology resources/EDAM.owl --tool_library resources/tools --save_KG_path resources/KG.json
```