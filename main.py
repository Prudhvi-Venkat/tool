import click
from datetime import datetime
from zoneinfo import ZoneInfo

@click.command()
@click.option('--string', default='Success',help="Help for tool")
@click.option('--repeat', default=1, help="Repeat the print in console")
def main(string, repeat):
    d_t = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    click.echo(string)
    for i in range(repeat):
        """This is a Greeting from Tool"""
        click.echo(str(i+1)+'.'+' Printing in the console : ' + d_t + '')

if __name__ == '__main__':
    main()