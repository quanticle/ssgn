from unittest.mock import (
    call,
    patch
)


from ssgn.ssgn import (
    convert_to_html,
)

class TestSSGN:
    
    @patch('pypandoc.convert_text')
    def test_convert_to_html(self, patched_convert_text):
        output = convert_to_html("# test markdown")
        patched_convert_text.assert_called_once_with("# test markdown", "html", format="md")
