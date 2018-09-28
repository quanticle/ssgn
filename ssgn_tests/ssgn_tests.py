from unittest.mock import (
    call,
    patch
)


from ssgn.ssgn import (
    convert_to_html,
    get_output_path
)

class TestSSGN:
    
    @patch('pypandoc.convert_text')
    def test_convert_to_html(self, patched_convert_text):
        output = convert_to_html("# test markdown")
        patched_convert_text.assert_called_once_with("# test markdown", "html", format="md")

    def test_get_output_filename_flat(self):
        output_filename = get_output_path("input", "input/foo.md", "output")
        assert output_filename == "output/foo.md"

    def test_get_output_filename_nested(self):
        output_filename = get_output_path("input", "input/foo/bar/test.md", "output")
        assert output_filename == "output/foo/bar/test.md"

    
