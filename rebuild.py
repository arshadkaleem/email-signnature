import os

def build_signature(imgs, hrefs, widths, heights, alts):
    css = """<style>
    table { border-collapse: collapse; border-spacing: 0; border: none; }
    td { border: none; padding: 0; margin: 0; vertical-align: top; font-size: 0; line-height: 0; }
    img { display: block; border: none; outline: none; text-decoration: none; }
    a { display: block; border: none; outline: none; text-decoration: none; }
</style>"""

    lw, lh     = widths[0], heights[0]
    rw, hh     = widths[1], heights[1]
    ph         = heights[2]
    eh         = heights[3]
    wh         = heights[4]
    loch       = heights[5]
    blw, bh    = widths[6], heights[6]
    iw         = widths[7:11]

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
{css}
</head>
<body style="margin:0; padding:0;">

<table style="width:800px; border-collapse:collapse; border-spacing:0; border:none;">
    <tr>
        <td style="width:{lw}px; padding:0; margin:0; border:none; vertical-align:top;">
            <a href="{hrefs[0]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                <img src="{imgs[0]}" width="{lw}" height="{lh}" alt="{alts[0]}" style="display:block; width:{lw}px; height:{lh}px; border:none; outline:none;">
            </a>
        </td>
        <td style="width:{rw}px; padding:0; margin:0; border:none; vertical-align:top;">
            <table style="width:{rw}px; border-collapse:collapse; border-spacing:0; border:none;">
                <tr>
                    <td style="padding:0; margin:0; border:none;">
                        <a href="{hrefs[1]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[1]}" width="{rw}" height="{hh}" alt="{alts[1]}" style="display:block; width:{rw}px; height:{hh}px; border:none; outline:none;">
                        </a>
                    </td>
                </tr>
                <tr>
                    <td style="padding:0; margin:0; border:none;">
                        <a href="{hrefs[2]}" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[2]}" width="{rw}" height="{ph}" alt="{alts[2]}" style="display:block; width:{rw}px; height:{ph}px; border:none; outline:none;">
                        </a>
                    </td>
                </tr>
                <tr>
                    <td style="padding:0; margin:0; border:none;">
                        <a href="{hrefs[3]}" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[3]}" width="{rw}" height="{eh}" alt="{alts[3]}" style="display:block; width:{rw}px; height:{eh}px; border:none; outline:none;">
                        </a>
                    </td>
                </tr>
                <tr>
                    <td style="padding:0; margin:0; border:none;">
                        <a href="{hrefs[4]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[4]}" width="{rw}" height="{wh}" alt="{alts[4]}" style="display:block; width:{rw}px; height:{wh}px; border:none; outline:none;">
                        </a>
                    </td>
                </tr>
                <tr>
                    <td style="padding:0; margin:0; border:none;">
                        <a href="{hrefs[5]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[5]}" width="{rw}" height="{loch}" alt="{alts[5]}" style="display:block; width:{rw}px; height:{loch}px; border:none; outline:none;">
                        </a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td colspan="2" style="padding:0; margin:0; border:none;">
            <table style="width:800px; border-collapse:collapse; border-spacing:0; border:none;">
                <tr>
                    <td style="width:{blw}px; padding:0; margin:0; border:none;">
                        <a href="{hrefs[6]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[6]}" width="{blw}" height="{bh}" alt="Legend Group" style="display:block; width:{blw}px; height:{bh}px; border:none; outline:none;">
                        </a>
                    </td>
                    <td style="width:{iw[0]}px; padding:0; margin:0; border:none;">
                        <a href="{hrefs[7]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[7]}" width="{iw[0]}" height="{bh}" alt="{alts[7]}" style="display:block; width:{iw[0]}px; height:{bh}px; border:none; outline:none;">
                        </a>
                    </td>
                    <td style="width:{iw[1]}px; padding:0; margin:0; border:none;">
                        <a href="{hrefs[8]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[8]}" width="{iw[1]}" height="{bh}" alt="{alts[8]}" style="display:block; width:{iw[1]}px; height:{bh}px; border:none; outline:none;">
                        </a>
                    </td>
                    <td style="width:{iw[2]}px; padding:0; margin:0; border:none;">
                        <a href="{hrefs[9]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[9]}" width="{iw[2]}" height="{bh}" alt="{alts[9]}" style="display:block; width:{iw[2]}px; height:{bh}px; border:none; outline:none;">
                        </a>
                    </td>
                    <td style="width:{iw[3]}px; padding:0; margin:0; border:none;">
                        <a href="{hrefs[10]}" target="_blank" style="display:block; border:none; outline:none; text-decoration:none;">
                            <img src="{imgs[10]}" width="{iw[3]}" height="{bh}" alt="{alts[10]}" style="display:block; width:{iw[3]}px; height:{bh}px; border:none; outline:none;">
                        </a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>

</body>
</html>"""
    return html


base = r'C:\Users\arsha\Desktop\legend-sign'
gh   = 'https://raw.githubusercontent.com/arshadkaleem/email-signnature/refs/heads/main'
dr   = 'https://drrzwc.in/wp-content/uploads/2026/04'

W = [480, 320, 320, 320, 320, 320, 580, 50, 50, 30, 90]
H = [305, 152,  33,  30,  30,  60,  51, 51, 51, 51, 51]

signatures = [
    {
        'file': 'gmail-signature.html',
        'imgs': [
            f'{dr}/01_left_main.jpg', f'{dr}/02_right_header.jpg', f'{dr}/03_right_phone.jpg',
            f'{dr}/04_right_email.jpg', f'{dr}/05_right_website.jpg', f'{dr}/06_right_location.jpg',
            f'{dr}/07_bottom_left.jpg', f'{dr}/08_icon_x.jpg', f'{dr}/09_icon_instagram.jpg',
            f'{dr}/10_icon_tiktok.jpg', f'{dr}/11_icon_linkedin.jpg',
        ],
        'hrefs': [
            'https://legendgroup.sa/', 'https://legendgroup.sa/', 'tel:+966543663939',
            'mailto:s.alqurashi@legendgroup.sa', 'https://legendgroup.sa/', 'https://legendgroup.sa/',
            'https://legendgroup.sa/', 'https://x.com/legendgroupsa',
            'https://www.instagram.com/legendgroupsa',
            'https://www.tiktok.com/@legendgroupsa?_r=1&_t=ZS-917SYeEGeZD',
            'https://www.linkedin.com/company/legend-group-sa/',
        ],
        'alts': ['Legend Group','Sofian Alqurashi CEO','Phone +966 54 366 3939',
                 'Email s.alqurashi@legendgroup.sa','Website www.legendgroup.sa',
                 'King Road Jeddah An-Narjis Riyadh','Legend Group',
                 'X Twitter','Instagram','TikTok','LinkedIn'],
    },
    {
        'file': 'abdullah-sign.html',
        'imgs': [
            f'{gh}/abdullah-slices/01_left_main.jpg', f'{gh}/abdullah-slices/02_right_header.jpg',
            f'{gh}/abdullah-slices/03_right_phone.jpg', f'{gh}/abdullah-slices/04_right_email.jpg',
            f'{gh}/abdullah-slices/05_right_website.jpg', f'{gh}/abdullah-slices/06_right_location.jpg',
            f'{gh}/abdullah-slices/07_bottom_left.jpg', f'{gh}/abdullah-slices/08_icon_x.jpg',
            f'{gh}/abdullah-slices/09_icon_instagram.jpg', f'{gh}/abdullah-slices/10_icon_tiktok.jpg',
            f'{gh}/abdullah-slices/11_icon_linkedin.jpg',
        ],
        'hrefs': [
            'https://legendgroup.sa/', 'https://legendgroup.sa/', 'tel:+966543595900',
            'mailto:a.almakhzoom@legendgroup.sa', 'https://legendgroup.sa/', 'https://legendgroup.sa/',
            'https://legendgroup.sa/', 'https://x.com/legendgroupsa',
            'https://www.instagram.com/legendgroupsa',
            'https://www.tiktok.com/@legendgroupsa?_r=1&_t=ZS-917SYeEGeZD',
            'https://www.linkedin.com/company/legend-group-sa/',
        ],
        'alts': ['Legend Group','Abdullah Almakhzoom COO','Phone +966 54 359 5900',
                 'Email a.almakhzoom@legendgroup.sa','Website www.legendgroup.sa',
                 'King Road Jeddah An-Narjis Riyadh','Legend Group',
                 'X Twitter','Instagram','TikTok','LinkedIn'],
    },
    {
        'file': 'amasi-sign.html',
        'imgs': [
            f'{gh}/amasi-slices/01_left_main.jpg', f'{gh}/amasi-slices/02_right_header.jpg',
            f'{gh}/amasi-slices/03_right_phone.jpg', f'{gh}/amasi-slices/04_right_email.jpg',
            f'{gh}/amasi-slices/05_right_website.jpg', f'{gh}/amasi-slices/06_right_location.jpg',
            f'{gh}/amasi-slices/07_bottom_left.jpg', f'{gh}/amasi-slices/08_icon_x.jpg',
            f'{gh}/amasi-slices/09_icon_instagram.jpg', f'{gh}/amasi-slices/10_icon_tiktok.jpg',
            f'{gh}/amasi-slices/11_icon_linkedin.jpg',
        ],
        'hrefs': [
            'https://legendgroup.sa/', 'https://legendgroup.sa/', 'tel:+966543595966',
            'mailto:a.alfarsi@legendgroup.sa', 'https://legendgroup.sa/', 'https://legendgroup.sa/',
            'https://legendgroup.sa/', 'https://x.com/legendgroupsa',
            'https://www.instagram.com/legendgroupsa',
            'https://www.tiktok.com/@legendgroupsa?_r=1&_t=ZS-917SYeEGeZD',
            'https://www.linkedin.com/company/legend-group-sa/',
        ],
        'alts': ['Legend Group','Amasi Alfarsi Account Manager','Phone +966 54 359 5966',
                 'Email a.alfarsi@legendgroup.sa','Website www.legendgroup.sa',
                 'King Road Jeddah An-Narjis Riyadh','Legend Group',
                 'X Twitter','Instagram','TikTok','LinkedIn'],
    },
    {
        'file': 'sofian-sign.html',
        'imgs': [
            f'{gh}/sofian-slices/01_left_main.jpg', f'{gh}/sofian-slices/02_right_header.jpg',
            f'{gh}/sofian-slices/03_right_phone.jpg', f'{gh}/sofian-slices/04_right_email.jpg',
            f'{gh}/sofian-slices/05_right_website.jpg', f'{gh}/sofian-slices/06_right_location.jpg',
            f'{gh}/sofian-slices/07_bottom_left.jpg', f'{gh}/sofian-slices/08_icon_1.jpg',
            f'{gh}/sofian-slices/09_icon_2.jpg', f'{gh}/sofian-slices/10_icon_3.jpg',
            f'{gh}/sofian-slices/11_icon_4.jpg',
        ],
        'hrefs': [
            'https://legendgroup.sa/', 'https://legendgroup.sa/', 'tel:+966543663939',
            'mailto:s.alqurashi@legendgroup.sa', 'https://legendgroup.sa/', 'https://legendgroup.sa/',
            'https://legendgroup.sa/', 'https://www.tiktok.com/@legendgroupsa?_r=1&_t=ZS-917SYeEGeZD',
            'https://www.linkedin.com/company/legend-group-sa/',
            'https://www.instagram.com/legendgroupsa',
            'https://x.com/legendgroupsa',
        ],
        'alts': ['Legend Group','Sofian Alqurashi CEO','Phone +966 54 366 3939',
                 'Email s.alqurashi@legendgroup.sa','Website www.legendgroup.sa',
                 'King Road Jeddah An-Narjis Riyadh','Legend Group',
                 'TikTok','LinkedIn','Instagram','X Twitter'],
    },
]

for sig in signatures:
    content = build_signature(sig['imgs'], sig['hrefs'], W, H, sig['alts'])
    path = os.path.join(base, sig['file'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {sig["file"]}')

print('All done!')
