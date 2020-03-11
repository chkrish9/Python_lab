"Go to https://catalog.umkc.edu/course-offerings/graduate/comp-sci/and fetch the course name and overview of"
"course.Hint:Use BeautifulSoup package. "

# imports
import requests
from bs4 import BeautifulSoup

# Fetch html from URL
html = requests.get('https://catalog.umkc.edu/course-offerings/graduate/comp-sci/')
# Parsing the HTML
bsObj = BeautifulSoup(html.content, "html.parser")

# Printing the title
print(bsObj.title.getText())

# Getting all course blocks which div has class name courseblock
courses = bsObj.find_all("div", {"class": "courseblock"})

# Iterating each course block and fetch the course name and description.
for block in courses:
    print("---------------------------------------------------------------")
    print("Course title : " + block.findChildren("span", {"class": "title"})[0].getText())
    print("Course desc : " + block.findChildren("p", {"class": "courseblockdesc"})[0].getText())
    print("---------------------------------------------------------------")
