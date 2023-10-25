import PyPDF2

# Nazwy plików PDF
plik1 = './Lab_02/projekty.pdf'
plik2 = './Lab_02/app-prop-pickle.pdf'
plik_wynikowy1 = './Lab_02/wynik1.pdf'
plik_wynikowy2 = './Lab_02/wynik2.pdf'

def merge(plik1, plik2, plik_wynikowy="./Lab_02/output.pdf", reverse=False):
    pdf_merger = PyPDF2.PdfMerger()
    if reverse:
        pdf_merger.append(plik2)
        pdf_merger.append(plik1)
    else:
        pdf_merger.append(plik1)
        pdf_merger.append(plik2)
    pdf_merger.write(plik_wynikowy)
    pdf_merger.close()
    

merge(plik1,plik2,plik_wynikowy1)
merge(plik1,plik2,plik_wynikowy2, True)
        