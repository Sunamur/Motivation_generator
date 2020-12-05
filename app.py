from flask import Flask
import random


app = Flask(__name__)

with open('./obscene-ru.txt', 'r') as f:
    res = f.readlines()
res = [x.strip() for x in res]


def generate_some_bullshit():
    return ' '.join([random.choice(res) for _ in range(10)])


html = '''

<html>
<head>
<meta http-equiv="refresh" content="3">
</head>
<title>Land of innovation</title>
<body>
<h1 style="text-align:center">{}</h1>

</body>
</html>
'''


@app.route('/')
def index():
    some_bs = generate_some_bullshit()
    return html.format(some_bs)


if __name__=='__main__':
    app.run(port=5099)