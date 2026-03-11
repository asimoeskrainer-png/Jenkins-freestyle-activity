quotes = [ 
'Keep going, success is near!',
'Dream big, work hard!',
'Code, build, repeat!', 
'Stay curious, stay learning!',
'Automation makes life easier!' 
] 
quote = random.choice(quotes) 
with open('output/freestyle_quote.txt', 'w') as f: 
    f.write(quote) 
print(f"Generated Quote: {quote}") 