from pdf2image import convert_from_path
from tqdm import tqdm

import os

def main(pdf_folder, ouput):
    poppler_path = 'C:\\poppler-22.04.0\\Library\\bin' # Replace With Your Own PATH
    docs = os.listdir(pdf_folder)

    for file in tqdm(docs):
        if os.path.isfile(f'{pdf_folder}/{file}'):
            pdf_file = convert_from_path(f'{pdf_folder}/{file}', poppler_path=poppler_path)
            base_filename = f'{pdf_folder}/{file}'.split("/")
            file_parts = base_filename[-1].split(".")
            
            for page in pdf_file:
                page.save(f'{ouput}/{file_parts[0]}.png', 'PNG')

if __name__ == '__main__':
    main('./PDF', './PNG')