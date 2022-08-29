from io import BufferedReader
import click

from .funcs.reverse import reverse_str
from .funcs.overturn import overturn_str


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """***Manipulate strings with Python***"""
    mode_commands = ["REVERSE", "OVERTURN", "WORKFILE"]
    if ctx.invoked_subcommand is None:
        click.echo("Specify one of the commands :\n")
        print(*mode_commands, sep="\n")


@main.command("REVERSE")
@click.option(
    "-w",
    multiple=False,
    required=True,
    type=str,
    help="The string to get reversed",
    nargs=1,
)
def reverse(w: str):
    """Takes a string as argument and print it back as reversed"""
    print("".join(reverse_str(w)))


@main.command("OVERTURN")
@click.option(
    "-r",
    multiple=False,
    required=True,
    type=str,
    help="The string to get overturned",
    nargs=1,
)
def overturn(r: str):
    """Takes a string as argument and print it back as overturned"""
    print(overturn_str(r))


@main.command("WORKFILE")
@click.option(
    "-f",
    multiple=False,
    required=True,
    type=click.File('rb'),
    help="The file containing the content to print",
    nargs=1,
)
def workfile(f: BufferedReader):
    """Takes a file and prints its content"""
    for line in f:
        print(line.decode("UTF-8"))


if __name__ == "__main__":
    main(obj={})
