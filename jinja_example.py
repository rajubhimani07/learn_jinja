import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./template")
templateEnv = jinja2.Environment(loader=templateLoader, extensions=['jinja2.ext.loopcontrols', 'jinja2.ext.do'])
TEMPLATE_FILE = "template.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
with open("data/test.csv", "rt") as file_reader:
    file_data = file_reader.read()
template_output = template.render(file_data=file_data)
with open("template_output/out.csv", "wt") as file_writer:
    file_writer.write(template_output)
