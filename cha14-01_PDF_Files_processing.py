# *****    IMPORTANT NOTES:
# WHEN USING VIRTUAL ENVIRONMENT AND INSTALLING NEW PACKAGES, THESE PACKAGES
# WILL BE AVAILABLE WHILE EXECUTING THE PYTHON PROGRAMS FROM THE ACTIVATED
# VIRTUAL ENVIRONMENT (venv), If we try to run the program from the Pythn IDLE
# Shell, then we will get the error: "from 'module/package' name import
#         classname ModuleNotFoundError: No module named 'module/package'". i.e:
# "from bs4 import BeautifulSoup ModuleNotFoundError: No module named 'bs4'"
# if we run the program from the activated venv directory with the command:
# python program_namy.py then it will run okay, because the package was
# installed in the venv.
# Now, if we also want to run the program in the Python IDLE shell, then we need
# to run this command in the venv to open en new IDLE from the venv and
# therefore have all the installed packages available: python -m idlelib.idle
# example:
# (web_scraping) PS C:\Python...\cha16\Web..._Project> python -m idlelib.idle


#                      P D F  files processing:
# 1- Create a project directory to contains all PDF programs:
# C:\\PythonBasicsBookExercises\\cha14>mkdir python_pdf_project

# 2- change to the project directory:
# C:\\PythonBasicsBookExercises\\cha14>cd python_pdf_project

# 3- Create a Python virtual environment in this project directory:
# C:\\PythonBasicsBookExercises\\cha14>python -m venv venv --prompt="pdf_project"
"""
C:\\PythonBasicsBookExercises\\cha14\\python_pdf_project>dir
 Volume in drive C is OS
 Volume Serial Number is A889-8647

 Directory of C:\\PythonBasicsBookExercises\\cha14\\python_pdf_project

02/28/2023  08:45 PM    <DIR>          .
02/28/2023  08:45 PM    <DIR>          ..
02/28/2023  08:45 PM    <DIR>          venv
               0 File(s)              0 bytes
               3 Dir(s)  1,806,287,421,440 bytes free """

# 4- Activate the Python virtual environment:
# C:\\PythonBasicsBookExercises\\cha14\\python_pdf_project>venv\\scripts\\activate

# 5- Extracting Text from a PDF file:
"""In this virtual environment, To extract the text from a PDF file, we need to
install the PyPDF2 package"""
# (pdf_project) C:\\PythonBasicsBookExercises\\cha14\\python_pdf_project>python
#                                                      -m pip install PyPDF2

# we can verify the PyPDF2 package with this command:
# (pdf_project) C:\\PythonBasicsBookExercises\\cha14\\python_pdf_project>python
#                                                      -m pip list
# If we already had a Python IDLE opened, ten we will have to restart it before
# we can use the PyPDF2 package.


# 6- OPENING AND READING A PDF FILE:
# We will be using the Pride_and_Prejudice.pdf file located in directory/folder:
#     C:\\Users\\ssshh\\python_pdf_files\\practice_files

# 6.1- In this virtual environment, run a Python IDLE terminal:
# (pdf_project) C:\\PythonBasicsBookExercises\\cha14\\python_pdf_project>python
"""Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information."""

# 6.2- import the PdfReader class from the installed PyPDF2 package and the
# Path from pathlib:
# >>> from PyPDF2 import PdfReader
# >>> from pathlib import Path

# 6.3- Create the path of the pdf file to read:
# >>> pdf_path = (
# ... Path.home() / "python_pdf_files" / "practice_files" / "Pride_and_Prejudice.pdf")

# 6.4- To gather the information about the pdf file (metadata and text) we need to
# create an instance/object of the PdfReade class associated to the pdf_path.
# Also the PdfReader class Opens and Reads the PDF file and makes all PDF file
# information (metadata and text) available through the instantiated object.
# Recall from chapter 12 'Files input and output' that all open files should be
# closed before a program terminates. The PdfReader object does all of this for
# us, so we don't have to worry about opening and closing the PDF file:
# >>> pdf_01_reader_obj = PdfReader(str(pdf_path))   # file is opened
"""the pdf_path is converted to string because the PdfReader function does NOT
know how to read from a pathlib.Path object."""


# 6.5- Now that we have created a PdfReader instance, in pdf_01_reader_obj,
# we can use it to gather information about the PDF file. For example, use the
# len(inst.pages) function to get the number of pages in the pdf:
# >>> len(pdf_01_reader_obj.pages)
# 234

"""NOTE: PyPDF2 was adapted from pyPdf package. pyPdf was written in 2005, only
four years after PEP 8 was published.
At that time, many Python programmers were migrating from languages in which
mixedCase was more common. Python accepts mixedCases but is not the
recommendation"""

# 6.6 We can also access some document's information using the .metadata
# attributes:
# >>> pdf_01_reader_obj.metadata
# {'/Title': 'Pride and Prejudice, by Jane Austen', '/Author': 'Chuck',
# '/Creator': 'Microsoft® Office Word 2007', '/CreationDate':
# 'D:20110812174208', '/ModDate': 'D:20110812174208',
# '/Producer': 'Microsoft® Office Word 2007'}

""" The .metadata object contains the PDF file metadata, which is set  when the
PDF is created.
The object returned by .metadata looks like a dictionary, but it's not
really the same thing. We can access each item in the .metadata as an attribute.
For example, to get the author attribute:"""
# >>> pdf_01_reader_obj.metadata.author
# 'Chuck'

# Creator attribute:
# >>> pdf_01_reader_obj.metadata.creator
# 'Microsoft® Office Word 2007'

# Producer attribute:
# >>> pdf_01_reader_obj.metadata.producer
# 'Microsoft® Office Word 2007'

# subject attribute:
# >>> pdf_01_reader_obj.metadata.subject

# title attribute:
# >>> pdf_01_reader_obj.metadata.title
# 'Pride and Prejudice, by Jane Austen'

# author_raw attribute:
# >>> pdf_01_reader_obj.metadata.author_raw
#'Chuck'

# creation_date_raw attribute:
# >>> pdf_01_reader_obj.metadata.creation_date_raw
# 'D:20110812174208'

# mofification_date_raw attribute:
# >>> pdf_01_reader_obj.metadata.modification_date_raw
# 'D:20110812174208'

# creator_raw attribute:
# >>> pdf_01_reader_obj.metadata.creator_raw
# 'Microsoft® Office Word 2007'

"""The PdfReader class provides all the necessary methods and attributes that we
need to access data in a PDF file, exaple extracting Text data:"""

# 7- EXTRACTING TEXT FROM A PAGE:
"""PDF pages are represented in the PyPDF2 package with the PageObject class. We
use the PageObject instances to interact with pages in a PDF file. We don't need
to create our own PageObect instances directly. Instead, we can access them
through the PdfReader object's .pages[] function. example:
    first_page = pdf_01_reader_obj.pages[0]

There are two steps to extracting TEXT from a single PDF page:
1- Get a PageObject with PdfReader.pages[] --> pdf_01_reader_obj.pages[].
2- Extract the TEXT as a string with the PageObject instance's .extract_text()
   method

Pride_and_Prejudice.pdf file has 234 pages. Each page has an index between 0 and
233. We can get the PageObject representing a specific page by passing the
page's index to PdfReader.pages[]:
"""
# >>> first_page_obj = pdf_01_reader_obj.pages[0]
# >>> type(first_page_obj)
# --> <class 'PyPDF2._page.PageObject'>

"""Now we can extract the page's text with PageObject.extract_text() method: """
# >>> first_page_obj.extract_text()
# Output:
"""' \\n \\nThe Project Gutenberg EBook of Pride and Prejudice, by Jane Austen
\\n \\nThis eBook is for the use of anyone anywhere at no cost and with
\\nalmost no restrictions whatsoever.  You may copy it, give it away or
\\nre-use it under the terms of the Project Gutenberg License included
\\nwith this eBook or online at www.gutenberg.org  \\n \\n \\nTitle: Pride and
Prejudice  \\n \\nAuthor: Jane Austen  \\n \\nRelease Date: August 26, 2008
[EBook #1342]  \\n[Last updated: August 11, 2011]  \\n \\nLanguage: Eng lish \\n
\\nCharacter set encoding: ASCII  \\n \\n*** START OF THIS PROJECT GUTENBERG EBOOK
PRIDE AND PREJUDICE ***  \\n \\n \\n \\n \\nProduced by Anonymous Volunteers, and
David Widger  \\n \\n \\n \\n \\n \\n \\nPRIDE AND PREJUDICE  \\n \\nBy Jane Austen  \\n
\\n \\n \\nContents  '"""
# NOTE: Depending on how a PDF file is encoded, text read from the PDF might
# include unexpected characters or may not include line breaks. This is one of
# the downsides to reading text from a PDF. In the real world, we may find
# ourself doing some manual cleanup when reading text from a PDF.

"""Every PdfReader object has a .pages attribute that we can use to iterate over
all of the pages in the PDF in order"""
# >>> for page in pdf_01_reader_obj.pages:
# ...     print(f"*** PAGE: {page.extract_text()}")


# Below is an example to implement changing to a new working directory, this
# was copied from another program in case we need to play changing the cwd using
# the os.getcwd() and changing it with os.chdir(new_dir_path):
""" # 2- Extract a single file to the current working directory which is:

# 2.0: get current working directory information
import os
current_working_dir = os.getcwd()

# now change the Current Working directory to zipped_dir_path
os.chdir(zipped_dir_path)  # change cwd to the path indicated.
# extract file1.py, into the new cwd:
print(f"\\nfile1.py -os.listdir(zipped_dir_path) --> \\
{os.listdir(zipped_dir_path)}")
---> file1.py -os.listdir(zipped_dir_path) --> ['all', 'data', 'file_zipped.zip',
'Users'] 
# The last directory "Users" is the one containig the extracted file. """

print(f"hello world!!!!!")


# Putting all together in a program:
# Note this program need to run from the activated virtual environment because
# the venv contains the packages PyPDF2 used to handle PDF files:
# (pdf_project) C:\PythonBasicsBookExercises\cha14\python_pdf_project>python \
#                                           cha14-01_PDF_Files_processing.py

from pathlib import Path  # pathlib package is in the base Python env.
from PyPDF2 import PdfReader  # PyPDF2 was installed in the venv.

# Create the path for the PDF file to process:
pdf_path = (
    Path.home() / "python_pdf_files" / "practice_files" / "Pride_and_Prejudice.pdf"
)


# To gather the information about the pdf file (metadata and text) we need to
# create an instance of the PdfReader class associated to the pdf_path. Also the
# PdfReader class Opens and Reads the PDF file and makes all PDF file
# information (metadata and text) available through the instantiated object.
# Recall from chapter 12 'Files input and output' that all open files should be
# closed before a program terminates. The PdfReader object does all of this for
# us, so we don't have to worry about opening and closing the PDF file:
pdf_01_reader_obj = PdfReader(str(pdf_path))  # file is opened
"""the pdf_path is converted to string because the PdfReader function does NOT
know how to read from a pathlib.Path object."""


output_file_path = (
    Path.home()
    / "python_pdf_files"
    / "practice_files"
    / "output_files"
    / "Pride_and_Prejudice.txt"
)

with output_file_path.open(mode="w") as output_file:
    title = pdf_01_reader_obj.metadata.title
    num_pages = len(pdf_01_reader_obj.pages)

    output_file.write(f"{title} \nNumber of pages: {num_pages}")

    for page in pdf_01_reader_obj.pages:
        text = page.extract_text()
        output_file.write(text)

print("*** Successfully processed my first PDF file ***")


# Section 14.1 Review Exercises:
from pathlib import Path
from PyPDF2 import PdfReader

# 1-
# - create path of the PDF file to process:
pdf_file_path = Path.home() / "python_pdf_files" / "practice_files" / "zen.pdf"

# - Create a PDF reader object:
zen_pdf_obj = PdfReader(str(pdf_file_path))

# 2- To print the number of pages in the zen_pdf_obj:
print(f"Zen pdf file number of pages: {len(zen_pdf_obj.pages)}")

# 3- Print the first page of zen.pdf file:
first_page = zen_pdf_obj.pages[0]
print(f"\nfirst page of zen.pdf --> {first_page.extract_text()}")


# 14.2 Extracting Pages From a PDF
"""In this lesson we will learn how to extract a page or a range of pages
from an existing PDF an save then to a new PDF.

First, we let see the PdfWriter class: We use the PdfWriter class to create
a new PDF file. Let's explore this class and learn the steps needed to
create a PDF using PyPDF2.
In the IDLE import the PdfWriter class and create a new instance/object
called pdf_file_writer: """
from PyPDF2 import PdfWriter

pdf_file_writer = PdfWriter()

"""
PdfWriter objects are like blank PDF files. We need to add some pages to
them before can save them to a file. Go and add a blank page to the created
pdf_file_writer: """

page = pdf_file_writer.add_blank_page(width=72, height=72)

"""The width and height parameters are required and determine te dimensions of the
page in units called points. One point equals 1/72 of an inch, so the above code
adds a one-inche-square blank page to the page pdf_file_writer object:
.add_blank_page() function returns a new PageObject instance representing the
page that was added to the PdfWriter (pdf_file_writer):
>>> type(page)
<class 'PyPDF2._page.PageObject'>

In this example, we hve assigned the PageObject instance returned by the
.add_blank_page() method to the 'page' variable, but in practice we don't
usually need to do this. That is, we usually call the .add_blank_page() method
without assigning the return value to anything:"""
######pdf_file_writer.add_blank_page(width=72, height=72)

# 1-: import the Path class:
from pathlib import Path

"""To WRITE the content of a pdf_file_writer to a PDF file, we have to pass a file
object in binary write mode to the pdf_file_writer.write() method:
1-: use the WITH with a path to an EXISTING OUTPUT file:"""
with Path("C:/Users/ssshh/python_pdf_files/practice_files/output_files/blank.pdf").open(
    mode="wb"
) as output_file:
    # Write/save the pdf_file_writer object to the output_file:
    pdf_file_writer.write(output_file)
    print(f"*** Successfully a blank page to the blank.pdf file ")
"""Response: --> (False, <_io.BufferedWriter name='C:\\Users\\ssshh\\
               python_pdf_files\\practice_files\\output_files\\blank.pdf'>)
The above write the pdf_file_writer content to the existing blank.pdf file. Now
if we open the blank.pdf file with a PDF reader software, such as Adobe Acrobat,
then we will see a document with a single blank one-inche-square page.

*** IMPORTANT NOTE: We saved the PDF file by passing the file
object (output_file) to the PdfWriter object's .write() method, not to the file
object's .write() method.
This is important because the following (all the way around code) won't work:
>>> with Path("C:/Users/ssshh/python_pdf_files/practice_files/
                output_files/blank.pdf").open(mode="wb") as output_file:
        output_file.write(pdf_file_writer)

This approach seems backward to many new programmers, so make sure we avoid this
mistake.
NOTE: PdfWriter objects can write to new PDF files, but they can't create new
content from scratch other than blank pages. This might seen like a big
problem, but in many situations, we don't need to create new content. Often,
we will work with pages extracted from PDF files that we have opened with a
PdfReader instance. Secton 14.8 will teach how to create PDF files from scratch.             

In the eample above, thre were three steps to create a new PDF FILE using PyPDF2:
1- Create a PdfWriter instance.
2- Add one or more pages to the PdfWriter instance.
3- Write to a file using the PdfWriter.write().
We will see this patter over and over as we learn various ways to add pages to a
PdfWriter instance.
"""
# Practicing the above exercise to see if append another blank page. Here,
# opening the output file as writte/append will be the same because the append
# occurs in the PdfWriter and the is moved to the output file:
pdf_file_writer.add_blank_page(width=360, height=360)  # 2- adding to PdfWriter
out_file_path = Path(
    "C:/Users/ssshh/python_pdf_files/practice_files/output_files/blank.pdf"
)
with out_file_path.open(mode="wb") as output_file_2:
    pdf_file_writer.write(output_file_2)  # 3- Write to a file using PdfWriter
    print(f"*** Successfully ANOTHER blank page to the blank.pdf file ")


# EXTRACTING A SINGLE PAGE FROM A PDF AND CREATING A NEW PDF file:
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

input_pdf_path = (
    Path.home() / "python_pdf_files" / "practice_files" / "Pride_and_Prejudice.pdf"
)
output_pdf_path = Path(
    "C:/Users/ssshh/python_pdf_files/practice_files/output_files/first_page.pdf"
)

input_pdf_reader = PdfReader(str(input_pdf_path))
first_page = input_pdf_reader.pages[0]

output_pdf_writer = PdfWriter()
output_pdf_writer.add_page(first_page)  # 2- adding to PdfWriter

with output_pdf_path.open(mode="wb") as output_file:
    output_pdf_writer.write(output_file)  # 3- Write to a file using PdfWriter
    print(f"\nSuccessfully added First Page")


# EXTRACTING A MULTIPLE PAGES FROM A PDF AND CREATING A NEW PDF file:
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# define files paths:
input_pdf_path = (
    Path.home() / "python_pdf_files" / "practice_files" / "Pride_and_Prejudice.pdf"
)
output_pdf_path = Path(
    "C:/Users/ssshh/python_pdf_files/practice_files/output_files/multp_page.pdf"
)

# define the PdfReader and PdfWriter objects:
input_pdf_reader = PdfReader(str(input_pdf_path))
output_pdf_writer = PdfWriter()

# Extract the multiple pages from the input PdfReader
for n in range(1, 4):
    page = input_pdf_reader.pages[n]
    output_pdf_writer.add_page(page)

# print total of page in PdfWriter:
print(f"\nTotal pages in PdfWriter object --> 3 = {len(output_pdf_writer.pages)}")

# Add extracted pages to the output PdfWriter:
with output_pdf_path.open(mode="wb") as output_file:
    output_pdf_writer.write(output_file)
    print(f"\nSuccessfully create a Multiple Pages file")


#  Using slice notation on the PdfReader object:
# Another way to extract multiple pages from a PDF is to take adavantage of the
# fact that PdfReader.pages supports slice notation. Let's redo the previous
# exercise using .pages slice instead of looping over a range object:
# create a new PdfWriter object:
new_pdf_writer = PdfWriter()

# new output pdf file:
new_output_pdf_path = Path(
    "C:/Users/ssshh/python_pdf_files/practice_files/output_files/sliced_page.pdf"
)


# loop over the input_pdf_reader.pages slice from indice 1 to 4:
for page in input_pdf_reader.pages[1:4]:  # slice, extract page 1, 2 and 3
    new_pdf_writer.add_page(page)

# write the content of the new_pdf_writer to the output file:
with new_output_pdf_path.open(mode="wb") as output_file:
    new_pdf_writer.write(output_file)
    print(f"\nSuccessfully create a Scliced Pages file")

""" Sometimes you need to extract every page from a PDF. We can use the methods
illustrated above to do this, but PyPDF2 provides a shortcut, PdfWriter
instances have n .append_pages_from_reader() method that we can use to append
pages from a PdfReader instance.
To use .append_pages_from_reader(), pass a PdfReader instance to the method's
reader parameter. For example, the following code copy every page from the Pride
and Prejudice PDF to a PdfWriter instance:"""

all_pages_pdf_writer = PdfWriter()
all_pages_pdf_writer.append_pages_from_reader(input_pdf_reader)

# output file for all pages:
all_pages_output_pdf_path = Path(
    "C:/Users/ssshh/python_pdf_files/practice_files/output_files/all_pages.pdf"
)

# write content in the PdfWriter to the output file:
with all_pages_output_pdf_path.open(mode="wb") as output_file:
    all_pages_pdf_writer.write(output_file)
    print(f"\nSuccessfully create a ALL Pages file")
