import owlready2 as owl
import os
import json
import argparse

from owlready2.namespace import Ontology
from owlready2 import Thing as Individual


class KG:

    def __init__(self, ontology, tool_library):
        self._ontology = ontology
        self._tool_library = tool_library

    def create(self, save_kg_path):
        pass
