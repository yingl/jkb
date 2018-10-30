import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fi',
                        '--filein',
                        type=str)
    parser.add_argument('-fo',
                        '--fileout',
                        type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    fi = args.filein
    fo = args.fileout
    with open(fi, 'r', encoding='utf-8') as fi:
        text = fi.read()
        text = text.replace('<h2>', '## ')
        text = text.replace('</h2>', '')
        text = text.replace('<strong>', '<b>')
        text = text.replace('</strong>', '</b>')
        text = text.replace('<p>', '')
        text = text.replace('</p>', '')
        text = text.replace('<ul>', '')
        text = text.replace('</ul>', '')
        text = text.replace('<ol>', '')
        text = text.replace('</ol>', '')
        text = text.replace('<li>', '')
        text = text.replace('</li>', '')
        text = text.replace('<center>', '')
        text = text.replace('</center>', '')
        with open(fo, 'w+', encoding='utf-8') as fo:
            fo.write(text)