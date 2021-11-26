"""Test cli."""

from unittest.mock import Mock, patch

from tftool.__main__ import main


@patch("argparse._sys.argv", ["tftool", "targets"])
@patch("tftool.__main__._filter", autospec=True)
def test_args(stdin: Mock) -> None:
    """Test argument handling."""
    main()
