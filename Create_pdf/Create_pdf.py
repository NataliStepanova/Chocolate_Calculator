import jinja2
import pdfkit


def create_pdf(vsego: int, kakao: int, maslo: int, pudra: int, fat_vsego: int, filename: str):
    data_for_template = {
        'vsego': str(vsego),
        'kakao': str(kakao),
        'maslo': str(maslo),
        'pudra': str(pudra),
        'fat_vsego': str(fat_vsego)
    }

    template_loader = jinja2.FileSystemLoader('./')

    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('./Create_pdf/Template.html')

    output_text = template.render(data_for_template)

    config = pdfkit.configuration(
        wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_string(
        output_text, './recipes/' + filename + '.pdf', configuration=config)
