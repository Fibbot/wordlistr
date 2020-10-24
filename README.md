beginning of my project to create ongoing wordlists based off burpsuite projects

# extracting urls from burp project:
- under proxy --> http history --> select all --> right click and 'copy urls' --> save this to 'infile'

filter in burp (optional, but cleaner):
- add what you want here, i typically filter out css, gif, png, woff, etc.
- i also will keep it to in-scope items, but that's up to you

# how to run:

python3 wordlistr.py infile outfileName


# Todo:
- create a burp plugin for this
