#!/usr/local/bin/python3

print("Content-Type: text/html")
print()
import cgi

form = cgi.FieldStorage()
data = form.getvalue('origin_file')

html_buffer   = open("index.html").read()

print html_buffer % data
print('''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form action="index.py" method="post" enctype="multipart/form-data">
            <input type="file" name="origin_file">
            <input type="submit">
        </form>
    </body>
</html>

''')
# print('''sdfs
# <!doctype html>
# <html>
# <head>
#   <title>WEB1 - Welcome</title>
#   <meta charset="utf-8">
# </head>
# <body>
#   <h1><a href="index.html">WEB</a></h1>
#   <ol>
#     <li><a href="1.html">HTML</a></li>
#     <li><a href="2.html">CSS</a></li>
#     <li><a href="3.html">JavaScript</a></li>
#   </ol>
#   <h2>WEB</h2>
#   <p>The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991.
#   </p>
# </body>
# </html>
# ''')
