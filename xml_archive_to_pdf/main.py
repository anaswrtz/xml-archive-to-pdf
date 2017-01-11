"""
xml-archive-to-pdf

Usage:
    xml-archive-to-pdf (-i <xml_file>) (-o <pdf_file>)

Options:
    -h --help  aide
    -i <xml_file>, --input <xml_file>
    -o <pdf_file>, --output <pdf_file>
"""

from docopt import docopt
#from .settings import *
from .utils import build_pdf
import sys


def main():
    try:
        args = docopt(__doc__)
        xml_file = args["--input"]
        pdf_file = args["--output"]
        build_pdf(xml_file, pdf_file)
    except Exception as e:
        sys.stderr.write(str(e))

if __name__ == "__main__":
    main()
