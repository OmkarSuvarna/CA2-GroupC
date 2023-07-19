from hospital import app

# so we do not need to set enviornment variable again, can run directly using python
if __name__ == '__main__':
    app.run(debug=True)


#  reference taken from https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/08-Posts
# i.e. how to create routes, models, forms, __init__
# the code in the repository is of a blog site and we have implemented an information system for hospital