import PythonLexer
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

class PythonDepthBreadth(object):
    tokenizer = PythonLexer.PythonLexer()
    tokenizer.build()

    python_code_tree = None
    python_function_tree = None

    def analyze_python_code(self, code):
        tokens = self.tokenizer.tokenize_indent(code)
        self.python_code_tree = Node("python_code_tree", indent = -1)
        indent = 0
        current_node = self.python_code_tree

        for token in tokens:
            if(token.type == 'NEWLINE'):
                indent = 0
                continue
            if(token.type == 'INDENT'):
                indent = len(token.value)
                continue
            if(token.type in ['IF','ELIF','ELSE','FOR','WHILE','CLASS','DEF','MATCH','CASE','WITH']):
                while(True):
                    if(current_node.indent < indent):
                        current_node = Node(token.value+"+"+str(token.lexpos), indent = indent, parent=current_node)
                        break
                    else:
                        current_node = current_node.parent

        # for pre, fill, node in RenderTree(self.python_code_tree):
        #     print("%s%s" % (pre, node.name))


    def analyze_python_function(self, code):
        tokens = self.tokenizer.tokenize_indent(code)
        self.python_function_tree = Node("python_function_tree", indent = -1)
        indent = 0
        current_node = self.python_function_tree

        for token in tokens:
            if(token.type == 'NEWLINE'):
                indent = 0
                continue
            if(token.type == 'INDENT'):
                indent = len(token.value)
                continue
            if(token.type == 'FUNCTION'):
                while(True):
                    if(current_node.indent < indent):
                        current_node = Node(token.value, indent = indent, parent=current_node)
                        break
                    else:
                        current_node = current_node.parent

        # for pre, fill, node in RenderTree(self.python_function_tree):
        #     print("%s%s" % (pre, node.name))


    def print_conditional(self):
        conditional_list = []
        nodes = self.python_code_tree.root.descendants
        for node in nodes:
            if(node.name.split('+')[0] == 'if'):
                breadth = 1
                for sib in node.siblings:
                    if(int(node.name.split('+')[1]) < int(sib.name.split('+')[1]) and sib.name.split('+')[0] == 'if'):
                        break
                    elif(int(node.name.split('+')[1]) < int(sib.name.split('+')[1]) and sib.name.split('+')[0] in ['elif','else']):
                        breadth += 1
                conditional_list.append([node.name,breadth])
        return conditional_list


    def print_loop(self):
        loop_list = []
        height = 0
        nodes = [self.python_code_tree.root]
        while(len(nodes) != 0):
            new_nodes = []
            for node in nodes:
                if(node.name.split('+')[0] in ['for','while']):
                    loop_list.append([node.name, height])
                    new_nodes += [node]
                else:
                    nodes += list(node.children)
            nodes = []
            for node in new_nodes:
                nodes += list(node.children)
            height += 1

        for loop in loop_list:
            loop[1] = height-loop[1]-1
        
        return loop_list
                

    def print_function(self):
        function_list = []
        repeat_check = []
        for func in self.python_function_tree.children:
            if(func.name in repeat_check):
                continue
            recursion = False
            children = []
            for child in func.children:
                children.append(child.name)
            if(func.name in children):
                recursion = True
            function_list.append([func.name, len(children), recursion])
            repeat_check.append(func.name)

        return function_list
        

