from docx import Document
import os


def fill_template(temp_name, re, co, li, te):
    template_path = "Template/{temp}.docx".format(temp=temp_name)
    result_path = "/Users/Samuel/Desktop/Cover_Letter.docx"

    variables = {
        "${RECIPIENT_NAME}": re,
        "${COMPANY_NAME}": co,
        "${LISTING_SOURCE}": li,
        "${TECHNOLOGY}": te,
    }

    document = Document(template_path)

    for v_key, v_value in variables.items():
        for paragraph in document.paragraphs:
            fill(paragraph, v_key, v_value)

    document.save(result_path)


def fill(p, k, v):
    if k in p.text:
        inline = p.runs
        for i in inline:
            if k in i.text:
                i.text = i.text.replace(k, v);
