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
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError("implement me")
    
    def props_to_html(self):
        props = ""
        if self.props == None:
            return props
        for key in self.props:
            props = props + f' {key}="{self.props[key]}"'
        return props
