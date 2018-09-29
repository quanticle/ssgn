import glob
from itertools import chain
import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
import pypandoc

def get_input_files(source_dir):
    """
    Recursively traverses `source_dir` and gets all the *.md and *.markdown files

    Input:
        source_dir (str): the path to the source dir

    Output:
        iterator which yields all the *.md and *.markdown files, recursively, from the directory tree rooted at
        `source_dir`
    """
    parent_path = Path(source_dir)
    md_files = parent_path.glob("**/*.md")
    markdown_files = parent_path.glob("**/*.markdown")
    return chain(md_files, markdown_files)

def get_output_path(source_dir, source_path, destination_dir):
    """
    Turns an input path into an output path.

    Input:
        source_dir (str): the path to the source dir
        source_path (str): the path to a file underneath `source_dir`
        destination_dir (str): the path to the destination directory

    Output:
        A new path rooted at destination dir.

    Example: 
        get_output_path("source", "source/foo/bar/baz.txt", "dest") => "dest/foo/bar/baz.txt"
    """

    return os.path.join(destination_dir, os.path.relpath(source_path, start=source_dir))

def convert_to_html(markdown_string):
    return pypandoc.convert_text(markdown_string, "html", format="md")

