"""Command line entrypoint."""

import sys
from argparse import ArgumentParser

from . import _filter
from ._backport import BooleanOptionalAction  # type: ignore


def _parser() -> ArgumentParser:
    filters = ArgumentParser(add_help=False)
    filters.add_argument(
        "-u",
        "--updates",
        help="Targets about to be updated.",
        default=True,
        action=BooleanOptionalAction,
    )
    filters.add_argument(
        "-c",
        "--creates",
        help="Targets about to be created.",
        default=True,
        action=BooleanOptionalAction,
    )
    filters.add_argument(
        "-d",
        "--destroys",
        help="Targets to be destroyed.",
        default=False,
        action=BooleanOptionalAction,
    )
    filters.add_argument(
        "-n",
        "--noops",
        help="Targets that are up to date.",
        default=False,
        action=BooleanOptionalAction,
    )
    filters.add_argument(
        "-r",
        "--regex",
        help="Regex to select targets.",
    )

    parser = ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("targets", help="List targets", parents=[filters])
    subparsers.add_parser(
        "target", help="Construct -target arguments for xargs.", parents=[filters]
    )
    return parser


def main() -> None:  # pragma: no cover
    """Command line entrypoint."""
    args = _parser().parse_args()
    if args.command == "targets":
        for target in _filter(
            sys.stdin, args.regex, args.creates, args.updates, args.destroys, args.noops
        ):
            print(target)
    elif args.command == "target":
        print(
            "\x00".join(
                f"-target={target}"
                for target in _filter(
                    sys.stdin,
                    args.regex,
                    args.creates,
                    args.updates,
                    args.destroys,
                    args.noops,
                )
            ),
            end="",
        )


if __name__ == "__main__":  # pragma: no cover
    main()
