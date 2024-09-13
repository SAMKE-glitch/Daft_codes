from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            name, value = attr
            if value is None:
                value = "None"
            print(f"-> {name} > {value}")
    
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            name, value = attr
            if value is None:
                value = "None"
            print(f"-> {name} > {value}")

# instantiate the parser
parser = MyHTMLParser()

# take input
n = int(input())
html_code = ""
for _ in range(n):
    html_code += input()

# feed the HTML content to the parser
parser.feed(html_code)

