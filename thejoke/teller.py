import sh

from thejoke import punchline

def tell():
    out = sh.echo(punchline())
    print out
