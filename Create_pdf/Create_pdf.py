import jinja2
import pdfkit


def create_pdf(vsego: int, proc_kakao: int, proc_maslo: int, kakao: int, maslo: int, pudra: int, fat_vsego: int, ccal: int, prot: int, fat: int, carb: int, filename: str):
    data_for_template = {
        'vsego': str(vsego),
        'proc_kakao': str(proc_kakao),
        'proc_maslo': str(proc_maslo),
        'kakao': str(kakao),
        'maslo': str(maslo),
        'pudra': str(pudra),
        'fat_vsego': str(fat_vsego),
        'ccal': str(ccal),
        'prot': str(prot),
        'fat': str(fat),
        'carb': str(carb)

    }

    template_loader = jinja2.FileSystemLoader('./')

    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('./Create_pdf/Template.html')

    output_text = template.render(data_for_template)

    config = pdfkit.configuration(
        wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_string(
        output_text, './recipes/' + filename + '.pdf', configuration=config)

    print('Ваш рецепт сохранен в ./recipes/' + filename + '.pdf')
