"""Test filtering Terraform plan."""

from io import StringIO

from tftool import _filter


def test_filter() -> None:
    """Test filtering."""
    assert (
        list(
            _filter(
                StringIO(
                    """{
  "resource_changes": [
    {
      "address": "somthing.main",
      "change": {
        "actions": ["create"]
      }
    },
    {
      "address": "somthing.else",
      "change": {
        "actions": ["create"]
      }
    },
    {
      "address": "somthing.main2",
      "change": {
        "actions": ["no-op"]
      }
    }
  ]
}"""
                ),
                "main",
                True,
                True,
                True,
                False,
            )
        )
        == ["somthing.main"]
    )
