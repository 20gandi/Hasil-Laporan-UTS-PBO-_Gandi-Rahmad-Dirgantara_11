from template_engine import parse_template, compile_template

fl=open('dokumen/template.html', 'r') as fl:
    template_text = fl.read()

data_parameter = {
    'nama': 'Gandi Rahmad Dirgantara',
    'beras': ['Premium', 'Radja', 'Enak']
}

# Kompilasi template
tokens = parse_template(template_text)
output = compile_template(tokens, data_parameter)
print(output)
