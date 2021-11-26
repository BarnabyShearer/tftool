"""Ergonomic utilities for the terraform CLI."""

import json
import re
from typing import Any, Iterable, Optional, TextIO

JSON = Any


def _filter(
    plan: TextIO,
    regex: Optional[str],
    creates: bool,
    updates: bool,
    destroys: bool,
    noops: bool,
) -> Iterable[str]:
    for resource in json.load(plan)["resource_changes"]:
        if {"create": creates, "update": updates, "no-op": noops, "delete": destroys}[
            resource["change"]["actions"][0]
        ]:
            if not regex or re.search(regex, resource["address"]):
                yield resource["address"]
