import random
import os

# Ensure the output directory exists so the script doesn't crash
if not os.path.exists('output'):
    os.makedirs('output')

quotes = [ 
    'Keep going, success is near!',
    'Dream big, work hard!',
    'Code, build, repeat!', 
    'Stay curious, stay learning!',
    'Automation makes life easier!' 
] 

# Pick a random quote
quote = random.choice(quotes) 

# Save to the file
with open('output/freestyle_quote.txt', 'w') as f: 
    f.write(quote) 

print(f"Generated Quote: {quote}")
