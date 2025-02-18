class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props

    def __eq__(self, html_node):
        return (self.tag == html_node.tag and
             self.value == html_node.value and
             self.children == html_node.children and
             self.props == html_node.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError("implement me")
    
    def props_to_html(self):
        props = ""
        if self.props == None:
            return props
        for key in self.props:
            props = props + f' {key}="{self.props[key]}"'
        return props


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        children = None
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

   
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        value = None
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        html = f"<{self.tag + self.props_to_html()}>"
        for node in self.children:
            html += node.to_html()
        html += f"</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    