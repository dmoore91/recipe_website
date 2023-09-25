from yattag import Doc

def generate_index():
    doc, tag, text = Doc().tagtext()

    with tag('h1'):
        text('Hello world!')

    print(doc.getvalue())


if __name__ == '__main__':
    generate_index()
