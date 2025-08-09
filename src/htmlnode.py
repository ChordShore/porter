class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
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
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value)
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props_to_html():
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        return super().props_to_html()