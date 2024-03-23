from jinja2 import Template

with open('jinja.j2') as f:
    tmpl = Template(f.read())
    
output = tmpl.render(
    page_title = 'Reread Me Book Rental',
    title_list = ["The Tale of Two Cities",
                  "Gone with the Wind",
                  "For Whom the Bell Tolls",
                  "Troy"]
)

# print to console
print(output)

# save to file
with open("jinja.html", "w") as fh:
    fh.write(output)

