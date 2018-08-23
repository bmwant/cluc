import click
from terminaltables import AsciiTable


class Table(object):
    def __init__(self, *, header=None, data=None):
        self.header = header
        self.data = data

    def print(self):
        data = []
        if self.header is not None:
            data.append(self.header)
        if self.data is not None:
            data.extend(self.data)

        tbl = AsciiTable(data)
        click.echo(tbl.table)
