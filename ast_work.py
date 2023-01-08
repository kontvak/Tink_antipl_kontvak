
f = open("C:/Users/Admin/Desktop/Tinkoff/0antiplagiat/plagiat/files/scorer.py",'r' )
text = f.read()

import ast


def get_classes(path):
    with open(path) as fh:
       root = ast.parse(fh.read(), path)
    classes = []
    func = []
    names = []
    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)

        if isinstance(node, ast.FunctionDef):
            func.append(node.name)

        if isinstance(node, ast.Name):
            names.append(node.name)

    return classes, func, names

print(get_classes("C:/Users/Admin/Desktop/Tinkoff/0antiplagiat/plagiat/files/scorer.py"))



