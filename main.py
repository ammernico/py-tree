from icecream import ic

DATA = [
        {"version": 4},
        {"meta-format": "mp4"},
        {"meta-size": "1000mb"},
        {"meta-size-gigabyte": "1gb"},
        {"meta-tags": "dog"},
        {"meta-tags-lastchanged": "today"}
]


class nested:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.location = self.split_key(key)

    def split_key(self, key):
        key = key.split("-")
        return key

    def display(self):
        ic(self.key)
        ic(self.val)
        ic(self.location)


class Node:
    def __init__(self, name):
        self.name = name
        self.entries = []
        self.next = []

    def display(self, name=""):
        name = f"{name}->{self.name}"
        print(name)
        for nest in self.entries:
            print("key:\t\t", nest.key)
        for node in self.next:
            print("next node\t", node.name)
        for node in self.next:
            node.display(name)


def main():
    # create the objects
    objects = []
    for e in DATA:
        for key, val in e.items():
            print(key)
            e = nested(key, val)
            objects.append(e)

    # create the node tree
    """
    ->root
    next node        version
    next node        meta
    ->root->version
    key:             version
    ->root->meta
    next node        format
    next node        size
    next node        tags
    ->root->meta->format
    key:             meta-format
    ->root->meta->size
    key:             meta-size
    next node        gigabyte
    ->root->meta->size->gigabyte
    key:             meta-size-gigabyte
    ->root->meta->tags
    key:             meta-tags
    next node        lastchanged
    ->root->meta->tags->lastchanged
    key:             meta-tags-lastchanged
    """

    root = Node("root")

    for nest in objects:
        nest.display()
        last_node = root

        #for order in nest.location:
        while True:
            order = nest.location[0]
            # the current node doesn't exist yet
            index = get_node_index(last_node, order)
            if index is None:
                new_node = Node(order)
                # append the new node to the last node
                last_node.next.append(new_node)
                last_node = last_node.next[-1]
            # the node already exists, just jump to the next node
            else:
                last_node = last_node.next[index]

            # reached location, make entry
            if len(nest.location) == 1:
                last_node.entries.append(nest)
                last_node = root
                break
            else:
                nest.location.pop(0)

    root.display()
    return 0


def get_node_index(node: Node, name: str) -> int:
    for n in range(0, len(node.next)):
        if node.next[n].name == name:
            # the node was found, return the index
            return n
    # the node doens't exist
    return None 




if __name__ == "__main__":
    main()
