"""Reading and writing the Archive file.

YOU IMPLEMENT THIS FILE.

The file format is CSV with no header row. One record per line, five fields
separated by commas, in this order:

    id ,title,city,year,condition
    MS001,Tarikh al-Sudan,Timbuktu,1655,fragile

Remember Session 1: a file is one long line of characters. The comma
separates fields; the newline separates records. Nothing else is doing
any work.
"""

import csv
from archive.validation import validate_record
from archive.errors import MalformedRecordError



FIELD_NAMES = ["id", "title", "city", "year", "condition"]

def parse_line(line):
    """Parse one CSV line into a record dictionary."""
    row = next(csv.reader([line])) 
    #I turn line into a list using the "[]" 
    #csv.reader is what they called an iterator, not an actual array, it is an iterator that iterates through the rows of a csv file
    #apparently, csv.reader views the strings as separators of lines...
    # apparently, when next asks for the next element, it gets all elements instead
    # The rest of this function is basic-ish from then on                     
    if len(row) != len(FIELD_NAMES):
        raise MalformedRecordError("Record must contain five fields")

    try:
        year = int(row[3])
    except ValueError:
        raise MalformedRecordError("Year must be an integer")

    record = {
        "id": row[0],
        "title": row[1],
        "city": row[2],
        "year": year,
        "condition": row[4],
    }

    return record        
    


def load_archive(path):
    """Read the file at `path` and return (valid_records, rejected_lines).

    valid_records   list of dicts that passed validate_record
    rejected_lines  list of the ORIGINAL line strings that did not — either
                    because they were malformed, or because validation
                    rejected them

    A file that does not exist is not an error. It means the archive is new.
    Return ([], []) and DO NOT raise. Your program must start on a machine
    where nobody has saved anything yet.

    Blank lines are skipped silently.

    Returns (list, list).
    """
    raise NotImplementedError("load_archive")


def save_archive(path, records):
    """Write every record to `path` as CSV, one per line, no header.

    Field order is FIELD_NAMES. The file is overwritten, not appended to.

    Returns None.
    """
    raise NotImplementedError("save_archive")
