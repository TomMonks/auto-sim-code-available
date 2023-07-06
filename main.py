'''
Script to convert a directory of PDFs to a
directory of tdxt files.
'''
from pypdf import PdfReader
import glob

INPUT_DIRECTORY = 'papers'
OUTPUT_DIRECTORY = 'output'

def get_pdf_file_list(subdirectory_name):
    '''
    Returns a list of pdf files from sub dir
    of the current working directory.
    '''
    return glob.glob(f"{subdirectory_name}/*.pdf")

def write_to_text_file(pdf_as_string, file_name):
    '''
    Write pdf string to file
    '''
    with open(f'{OUTPUT_DIRECTORY}/{file_name}.txt', 'w') as f:
        f.write(pdf_as_string)

def pdf_to_string(file_name):
    '''
    Convert a pdf to string
    '''
    # document as string
    doc = ''
    reader = PdfReader(file_name)
    for page in reader.pages:
        doc += page.extract_text()

    # extract only text oriented up
    return doc

def main():
    input_papers = get_pdf_file_list(INPUT_DIRECTORY)
    
    for pdf_file_name in input_papers:
        pdf_as_string = pdf_to_string(pdf_file_name)
        # write to file.
        write_to_text_file(pdf_as_string, 
                           pdf_file_name[len(INPUT_DIRECTORY):-4])

if __name__ == '__main__':
    main()
    