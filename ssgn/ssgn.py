import glob
from itertools import chain
import os

from jinja2 import Environment, FileSystemLoader
import pypandoc

def get_output_path(source_dir, source_path, destination_dir):
    return os.path.join(destination_dir, os.path.relpath(source_path, start=source_dir))

def convert_to_html(markdown_string):
    return pypandoc.convert_text(markdown_string, "html", format="md")

