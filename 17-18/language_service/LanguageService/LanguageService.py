import pycld2
from flask import Flask, jsonify, request

"""
If i understood correctly, the way the Flask Doc
recommends creating Flask apps is on module level,
which is why this solution feels slightly hacky.
"""

app = Flask(__name__)

@app.route('/langdetect/', methods=['GET'])
def languageDetection():
    """
    Calls the language detection API and returns the data as JSON
    :return: JSON response
    """
    detect = pycld2.detect(request.args.get("text"))
    # output is a multidimensional tuple, fields can be accessed by index, like a list.
    out = {
        "reliable": detect[0],
        "language": detect[2][0][0],
        "short": detect[2][0][1],
        "prob": detect[2][0][2]
    }
    # jsonifies the dictionary and returns
    return jsonify(out)

if __name__ == "__main__":
    app.run(debug=True)
