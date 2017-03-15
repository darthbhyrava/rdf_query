# Sriharsh Bhyravajjula
# Script to query RDF using SPARQL - conditionals and negations.
import rdflib

graph = rdflib.Graph()
graph.load("file:///home/darthbhyrava/3-2/NLA/rdf_tutorials/americans.ttl",format = "turtle")

# Find the names (labels) of all persons.
#
# for row in graph.query(
#     'select ?name where { ?schema a foaf:Person . \
#     ?schema rdfs:label ?name }'):
#     print (row.name)



# List out all occupations
#
# for row in graph.query(
#     'select ?ocp where { ?schema a foaf:Person .\
#     ?schema mydb:occupation ?ocp . \
#     }'):
#     print (row.ocp)



# Find all persons with "Mogroby" in family name
#
# for row in graph.query(
#     'select ?persons where { ?schema a foaf:Person . \
#      ?schema foaf:familyName "Mogroby" .\
#      ?schema rdfs:label ?persons .\
#     }'):
#     print row.persons



# Find names of all people with note "x"
#
# for row in graph.query(
#     'select ?names where { ?schema a foaf:Person . \
#     ?schema mydb:note "x" . \
#     ?schema rdfs:label ?names }'):
#     print (row.names)



# Find all persons who have a death age.
#
# for row in graph.query(
#     'select ?name ?age where { ?schema a foaf:Person . \
#     ?schema mydb:deathAge ?age . \
#     ?schema rdfs:label ?name }'):
#     print(row.name+" died at "+row.age)



# Find me all the persons who have any note except 'x'
#
# for row in graph.query(
#     'select ?name where { ?schema a foaf:Person . \
#     ?schema mydb:note ?note . \
#     ?schema rdfs:label ?name . \
#     MINUS {?schema mydb:note "x"} }'):
#     print (row.name)



# Find all daughter relations
#
# for row in graph.query(
#     'select ?daughter ?parent where { ?schema a foaf:Person .\
#     ?schema mydb:daughterOf ?parent_schema . \
#     ?schema rdfs:label ?daughter . \
#     ?parent_schema rdfs:label ?parent}'):
#     print (row.daughter+" is the daughter of "+row.parent)



# Find all wives and their husbands
# 
# for row in graph.query(
#     'select ?wife ?hub where { ?schema a foaf:Person . \
#     ?schema mydb:wifeOf ?hub_schema . \
#     ?schema rdfs:label ?wife .\
#     ?hub_schema rdfs:label ?hub }'):
#     print (row.wife+" is the wife of "+row.hub)



# Find all sons who are still alive
#
# for row in graph.query(
#     'select ?son where { ?schema a foaf:Person . \
#     ?schema mydb:sonOf ?parent .\
#     ?schema rdfs:label ?son .\
#     MINUS { ?schema schema:deathDate ?date } }'):
#     print (row.son)



# Who is the daughter of "Mirzan Marie" whose occupation is "ex US Consular Agent".
#
# for row in graph.query(
#     'select ?dau where { ?mm rdfs:label "Mirzan Marie" .\
#     ?schema mydb:daughterOf ?mm .\
#     ?schema mydb:occupation "ex US Consular Agent" .\
#     ?schema rdfs:label ?dau} '):
#     print (row.dau)