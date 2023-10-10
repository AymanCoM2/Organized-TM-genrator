import os
import PyPDF2
from docx2pdf import convert
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


def add_page_numbers(input_pdf, output_pdf):
    pdf = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()
    total_pages = len(pdf.pages)
    for page_num in range(total_pages):
        page = pdf.pages[page_num]
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        page_number_text = f"Page {page_num + 1} Out Of {total_pages}"
        can.drawString(10, 10, page_number_text)
        can.save()
        packet.seek(0)
        page_number_pdf = PyPDF2.PdfReader(packet)
        page.merge_page(page_number_pdf.pages[0])  # Use merge_page instead
        pdf_writer.add_page(page)
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)
    return output_pdf


def combineParts(fileNamesList):
    pdfFiles = []
    for docx_file in fileNamesList:
        convert(docx_file)
        pdf_file = docx_file.replace('.docx', '.pdf')
        print(f"Converted {docx_file} to {pdf_file}")
        pdfFiles.append(pdf_file)
    merger = PyPDF2.PdfMerger()
    for pdf_file in pdfFiles:
        merger.append(pdf_file)
    merged_pdf_path = "result.pdf"
    merger.write(merged_pdf_path)
    merger.close()
    fname = add_page_numbers(merged_pdf_path, "result_with_page_numbers.pdf")
    return fname
