from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher


def clean_db(graph):
    graph.delete_all()


def show_all(node_matcher):
    results = node_matcher.match("Person")
    for f in results:
        print(f)
    print("========================")


def add_node_rel(graph):
    peter = Node("Person", "student", name="Peter", age=25, gender="male")
    kelly = Node("Person", "player", name="Kelly", age=20, gender="female")
    kary = Node("Person", "student", name="Kary", age=25, gender="female")
    alia = Node("Person", "officer", name="alia", age=23, gender="female")
    graph.create(peter)
    graph.create(kelly)
    graph.create(kary)
    graph.create(alia)

    aFriendRel = Relationship(kary, 'friends_of', peter)
    aFriendRel['years'] = 2
    graph.create(aFriendRel)


def update(graph):
    kary = Node("Person", "student", name="Kary", age=25, gender="female")
    peter = Node("Person", "student", name="Peter", age=25, gender="male")
    aFriendRel = Relationship(kary, 'friends_of', peter)
    aFriendRel['years'] =2
    graph.push(aFriendRel)


def search_node(node_matcher):
    result = node_matcher.match("Person", gender="female").first()
    print(result)


def search_rel(rel_matcher):
    kary = node_matcher.match("Person", name="Kary").first()
    peter = node_matcher.match("Person", name="Peter").first()
    result = rel_matcher.match((kary, peter)).first()
    print(result)


try:
    graph = Graph("localhost:7474", username="neo4j", password="amy920420")
    node_matcher = NodeMatcher(graph)
    rel_matcher = RelationshipMatcher(graph)
except:
    print("An exception occurred")
    raise

clean_db(graph)
add_node_rel(graph)
show_all(node_matcher)
print("\n********************\nUpdate the graph\n")
update(graph)
show_all(node_matcher)
search_node(node_matcher)
search_rel(rel_matcher)




