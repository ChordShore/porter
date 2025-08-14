import unittest

from convert_markdown_to_html_node import *

class TestConvertMarkdownToHTMLNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = convert_markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = """
# Heading 1

normal text

## Heading 2

normal text

### Heading 3

normal text

#### Heading 4

normal text

##### Heading 5

normal text

###### Heading 6

normal text

"""

        node = convert_markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Heading 1</h1><p>normal text</p><h2>Heading 2</h2><p>normal text</p><h3>Heading 3</h3><p>normal text</p><h4>Heading 4</h4><p>normal text</p><h5>Heading 5</h5><p>normal text</p><h6>Heading 6</h6><p>normal text</p></div>")

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = convert_markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
> quote text

normal text

> quote text 1
> quote text 2

normal text

"""

        node = convert_markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>quote text</blockquote><p>normal text</p><blockquote>quote text 1 quote text 2</blockquote><p>normal text</p></div>"
            )

    def test_unordered_list(self):
        md = """
- list text

normal text

- list text
- list text

"""

        node = convert_markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>list text</li></ul><p>normal text</p><ul><li>list text</li><li>list text</li></ul></div>"
            )
        
    def test_ordered_list(self):
        md = """
1. list text

normal text

1. list ```text```
2. list text

- list ```text```
- list text

"""

        node = convert_markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>list text</li></ol><p>normal text</p><ol><li>list <code>text</code></li><li>list text</li></ol><ul><li>list <code>text</code></li><li>list text</li></ul></div>"
            )



if __name__ == "__main__":
	unittest.main()