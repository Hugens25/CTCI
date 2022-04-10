from datastructures.linkedlist import LinkedList

def intersection(l1: LinkedList, l2: LinkedList):
    smaller_list = l1 if len(l1) <= len(l2) else l2
    bigger_list = l2 if l1 == smaller_list else l1

    smaller_list_node = smaller_list.head
    bigger_list_node = bigger_list.head

    smaller_list_nodes = []

    while smaller_list_node:
        smaller_list_nodes.append(smaller_list_node)
        smaller_list_node = smaller_list_node.next
    
    while bigger_list_node:
        if bigger_list_node in smaller_list_nodes:
            matching_nodes = [node for node in smaller_list_nodes if bigger_list_node is node]
            if matching_nodes:
                return matching_nodes[0]
        bigger_list_node = bigger_list_node.next