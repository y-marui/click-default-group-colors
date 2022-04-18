# Click Default Group Colors
Combine `DefaultGroup` and `HelpColorsGroup` for click.

## Usage
```
import click
from click_default_group_colors import DefaultGroupColors

@click.group(cls=DefaultGroupColors,
             default_if_no_args=True)
def cli():
    pass

@cli.command(default=True)
def create():
    click.echo('create')

@cli.command()
def delete():
    click.echo('delete')
```
For more detail see base pacakges below.
* [click\-contrib/click\-default\-group: Extends click\.Group to invoke a command without explicit subcommand name\.](https://github.com/click-contrib/click-default-group)
* [click\-contrib/click\-help\-colors: Colorization of help messages in Click](https://github.com/click-contrib/click-help-colors)
