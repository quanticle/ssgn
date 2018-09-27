import pypandoc
from jinja2 import Environment, FileSystemLoader

def convert_to_html(markdown_string):
    return pypandoc.convert_text(markdown_string, "html", format="md")

def render_template(input_text, template):
    pass
