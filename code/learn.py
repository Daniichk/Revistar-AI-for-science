# import block
import wikipedia 
# wikipedia settings
wikipedia.set_lang("en")
#input section
term = input()
# opening of the file 
with open('1.txt','r') as file:
    content = file.readlines()
# tokenization
tokens = re.findall(r"\w+|[^\w\s]", content)
def get_defenition(term):
    try:
        return wikipedia.summary(term, sentences=5)
    except:
        return "Sorry, I don't find your term in my base"

    