class Node:
    def _init_(self, id, holderval, l, r, require):
        self.id = id
        self.holderval = holderval
        self.l = l
        self.r = r
        self.require = require

def TraversalInorder(roonodeT):
    if roonodeT == None:
        return
    TraversalInorder(roonodeT.l)
    print(f"{roonodeT.id} {roonodeT.holderval}")
    TraversalInorder(roonodeT.r)

def token(roonodeT, NodeCS):
    if NodeCS == roonodeT.id:
        print(roonodeT.id)
        roonodeT.holderval = roonodeT.id
        return
    elif NodeCS < roonodeT.id:
        roonodeT.holderval = (roonodeT.l).id
        print(f"{roonodeT.id}->")
        roonodeT = roonodeT.l
        token(roonodeT, NodeCS)
    elif NodeCS > roonodeT.id:
        roonodeT.holderval = (roonodeT.r).id
        print(f"{roonodeT.id}->")
        roonodeT = roonodeT.r
        token(roonodeT, NodeCS)

def NodeTinsert(nodeNew, roonodeT):
    if nodeNew.id > roonodeT.id:
        if roonodeT.r == None:
            roonodeT.r = nodeNew
            nodeNew.holderval = roonodeT.id
        else:
            NodeTinsert(nodeNew, roonodeT.r)
    if nodeNew.id < roonodeT.id:
        if roonodeT.l == None:
            roonodeT.l = nodeNew
            nodeNew.holderval = roonodeT.id
        else:
            NodeTinsert(nodeNew, roonodeT.l)

if _name_ == "_main_":
    roonodeT = None
    nodeNew = None
    node1 = None
    n = 5
    nodeT = 3
    idValue = 0
    arr = [1, 2, 3, 4, 5]
    NodeCS = 2
    option = 0

    roonodeT = Node(nodeT, nodeT, None, None, None)
    node1 = Node(None, None, None, None, None)
    for i in range(n):
        idValue = arr[i]
        nodeNew = Node(idValue, None, None, None, None)
        if i == nodeT:
            i += 1
        NodeTinsert(nodeNew, roonodeT)
    TraversalInorder(roonodeT)
    token(roonodeT, NodeCS)

