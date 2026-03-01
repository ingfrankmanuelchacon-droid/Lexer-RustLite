# ast_nodes.py
class ASTNode:
    pass

class AssignNode(ASTNode):
    def __init__(self, ident, expr):
        self.ident = ident
        self.expr = expr

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class IfNode(ASTNode):
    def __init__(self, cond, then_stmt, else_stmt=None):
        self.cond = cond
        self.then_stmt = then_stmt
        self.else_stmt = else_stmt

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

class IdentNode(ASTNode):
    def __init__(self, name):
        self.name = name

class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value