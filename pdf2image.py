import fitz
import os
import numpy as np

def pdf2image(filepath = '', zoom = 0.5, dpi = 100):
    '''
    Converts a given file to a set of images - one for each page
    '''
    filename = filepath
    pdf_file = fitz.open(filename)
    pdf_images = {}
    for page_index in range(pdf_file.page_count):
        try:
            page = pdf_file.load_page(page_index)
            mat = fitz.Matrix(zoom,zoom)
            pix = page.get_pixmap(matrix=mat,dpi=dpi)
            #get number of components in pixmap
            num_components  = len(pix.samples)

            img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height,pix.width,num_components))[:,:,0]

            pdf_images[page_index] = img_array
        except Exception as e:
            print(str(filename)+'>'+str(e))
            return None
    return pdf_images