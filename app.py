from flask import Flask, request

app = Flask(__name__)


@app.route("/textSimilarity")
def textSimilarity():
    string1 = request.args.get('sample1')
    string2 = request.args.get('sample2')

    set1 = set(string1.split())
    set2 = set(string2.split())
    intset = set1.intersection(set2)
    result = float(len(intset)) / (len(set1) + len(set2) - len(intset))

    return 'The similiarity metric between the two texts is: ' + str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
