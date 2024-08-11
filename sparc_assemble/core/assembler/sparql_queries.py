import owlready2 as owl

from owlready2.namespace import Ontology


def find_methods_from_request(ontology: Ontology, request: str) -> list[list[str]]:
    """
    Query ontology to find methods with request including in comment. Return methods with their inputs and outputs
    grouped.
    For now: comment matching very strict. In the future: request should be close to method description (flexibility).
    Args:
        ontology (Ontology): an owl ontology
        request (str): request from the user
    Returns:
        List of ['method', 'input1,input2,...', 'output,...']
    """
    sparql_query = """PREFIX edam: <%s>
        SELECT ?label_operation (GROUP_CONCAT(?label_input; separator=", ") as ?inputs) (GROUP_CONCAT(?label_output; separator=", ") as ?outputs)
        {?operation rdf:type edam:operation_0004 .
        ?operation rdfs:label ?label_operation .
        ?operation edam:has_input ?input .
        ?input rdfs:label ?label_input .
        ?operation edam:has_output ?output .
        ?output rdfs:label ?label_output .
        FILTER REGEX(?label_output, ".*%s.*", "i")} 
        GROUP BY ?label_operation
        """ % (ontology.base_iri, request)
    return list(owl.default_world.sparql(sparql_query))


def find_inferred_inputs(ontology: Ontology, input_str: str) -> list[list[str]]:
    """
    Query ontology to find methods with output = input (i.e. find methods that can compute input). Return methods with
    their inputs and outputs grouped.
    Args:
        ontology: an owl ontology
        input_str (str): label of an input
    Returns:
        List of ['method', 'input1,input2,...', 'output,...']
    """
    sparql_query = """PREFIX edam: <%s>
                SELECT ?label_operation (GROUP_CONCAT(?label_input; SEPARATOR=", ") AS ?inputs) (GROUP_CONCAT(?label_output; separator=", ") as ?outputs)
                {?current_input rdfs:label '%s' .
                ?operation edam:has_output ?current_input .
                ?operation rdfs:label ?label_operation .
                ?operation edam:has_output ?output .
                ?operation edam:has_input ?input .
                ?input rdfs:label ?label_input .
                ?output rdfs:label ?label_output} 
                GROUP BY ?operation
                """ % (ontology.base_iri, input_str)
    return list(owl.default_world.sparql(sparql_query))


def find_method_cwl(ontology: Ontology, method: str) -> list[list[str]]:
    """
    Query ontology to retrieve cwl file for the corresponding method through 'isDefinedBy' property.
    Args:
        ontology: an owl ontology
        method (str): label of a method
    Returns:
        List of ['path to cwl file']

    """
    sparql_query = """PREFIX edam: <%s>
        SELECT ?cwl
        {edam:%s rdfs:isDefinedBy ?cwl .}
        """ % (ontology.base_iri, method)
    return list(owl.default_world.sparql(sparql_query))


def find_all_tools(ontology: Ontology) -> list[list[str]]:
    """
    Query ontology to find all methods. Return methods with their inputs and outputs grouped.
    Args:
        ontology: an owl ontology
    Returns:
        List of ['method', 'input1,input2,...', 'output,...']
    """
    sparql_query = """PREFIX edam: <%s>
        SELECT ?label_operation (GROUP_CONCAT(?label_input; separator=", ") as ?inputs) (GROUP_CONCAT(?label_output; separator=", ") as ?outputs)
        {?operation rdf:type edam:operation_0004 .
        ?operation rdfs:label ?label_operation .
        ?operation edam:has_input ?input .
        ?input rdfs:label ?label_input .
        ?operation edam:has_output ?output .
        ?output rdfs:label ?label_output} 
        GROUP BY ?label_operation
        """ % ontology.base_iri
    return list(owl.default_world.sparql(sparql_query))
