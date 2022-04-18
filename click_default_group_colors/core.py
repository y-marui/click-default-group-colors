"""DefaultGroupColors: Combination of `DefaultGroup` and `HelpColorsGroup`."""
from click_default_group import DefaultGroup
from click_help_colors import HelpColorsGroup


class DefaultGroupColors(DefaultGroup, HelpColorsGroup):
    """Combination of `DefaultGroup` and `HelpColorsGroup`."""

    def __init__(self,
                 default_if_no_args: bool = None,
                 help_headers_color: str = None,
                 help_options_color: str = None,
                 options_custom_colors: str = None,
                 *args,
                 **kwargs):
        """Combine of `DefaultGroup` and `HelpColorsGroup`.

        Parameters
        ----------
        default_if_no_args : bool, optional
            resolves to the default command if no arguments passed.,
            by default None
        help_headers_color : str, optional
            `help_headers_color`, by default None
        help_options_color : str, optional
            `help_options_color`, by default None
        options_custom_colors : str, optional
            `options_custom_colors`, by default None
        """
        super(DefaultGroup, self).__init__(*args, **kwargs)
        super(HelpColorsGroup, self).__init__(*args, **kwargs)

        self.default_if_no_args = default_if_no_args
        self.help_headers_color = help_headers_color
        self.help_options_color = help_options_color
        self.options_custom_colors = options_custom_colors
