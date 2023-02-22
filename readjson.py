import json

components = json.load(open('components.json'))
print(components[0], type(components[0]))
portfolio = json.load(open('portfolio.json'))
print(portfolio[components[0]], type(portfolio[components[0]]))

