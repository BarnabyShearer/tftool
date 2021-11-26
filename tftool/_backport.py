# type: ignore

from argparse import Action


class BooleanOptionalAction(Action):
    """Backported from Python 3.9."""

    def __init__(
        self,
        option_strings,
        dest,
        default=None,
        type=None,
        choices=None,
        required=False,
        help=None,
        metavar=None,
    ):
        """Init."""

        _option_strings = []
        for option_string in option_strings:
            _option_strings.append(option_string)

            if option_string.startswith("--"):
                option_string = "--no-" + option_string[2:]
                _option_strings.append(option_string)

        if help is not None and default is not None:  # pragma: no cover
            help += " (default: %(default)s)"

        super().__init__(
            option_strings=_option_strings,
            dest=dest,
            nargs=0,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        """Call."""
        if option_string in self.option_strings:  # pragma: no cover
            setattr(namespace, self.dest, not option_string.startswith("--no-"))

    def format_usage(self):  # pragma: no cover
        """Help."""
        return " | ".join(self.option_strings)
