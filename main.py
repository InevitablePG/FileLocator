from flask import Flask, render_template, url_for
from Locator.FileLocator import FileSearch
from Form import MyForm
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    result = None
    length = None
    if form.validate_on_submit():
        filename = form.filename.data
        root_directory = form.root_directory.data
        check_field = form.check_field.data
        # Use the FileSearch class
        data = FileSearch(filename, root_directory)
        result = data.Search(advanced=check_field)
        length = len(result)
    return render_template('index.html', form=form, result=result, length=length)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
