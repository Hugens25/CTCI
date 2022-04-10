from datastructures.linkedlist import LinkedList

def loop_detection(ll: LinkedList):
    node = ll.head
    nodes = []
    while node:
        if node in nodes:
            matching_nodes = [matched_node for matched_node in nodes if node is matched_node]
            if matching_nodes:
                return matching_nodes[0]
        nodes.append(node)
        node = node.next