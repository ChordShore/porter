class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Super() to_html function is Not Implemented!")
    
    def props_to_html(self):
        if self.props is None:
            return None
        
        result = ""
        for attribute in self.props:
            result += f"{attribute}=\"{self.props[attribute]}\" "
        if result[-1] == " ":
            result = result[0: -1]
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode self.tag is None!")
        if self.children is None:
            raise ValueError("ParentNode self.children is None!")
        result = f"<{self.tag}>"
        for child in self.children:
            if child is LeafNode:
                result += child.to_html()
            else:
                temp = self
                self = child
                return result + self.to_html() + f"</{temp.tag}>"
        return result

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode self.value is None!")
        if self.tag == None:
            return self.value
        if self.props_to_html():
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        return super().props_to_html()