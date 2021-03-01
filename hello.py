#!/usr/bin/env python
"""This is a click command line appliation. First make executable by terminalling chmod +x hello.py"""

import click

from myutils.util import add


@click.command()
@click.option("--value1")
@click.option("--value2")
def calculate(value1, value2):
    """This adds two numbers"""
    result = add(value1, value2)
    click.echo(click.style(f"Adding number: {value1}, {value2}", fg="red"))
    click.echo(click.style(f"Result: {result}", fg="blue"))


if __name__ == "__main__":
    calculate()
