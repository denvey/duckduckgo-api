from flask import Flask, request
from duckduckgo_search import ddg
app = Flask(__name__)


@app.route('/search')
def search():  # put application's code here
    keywords = request.args.get('q')
    print(request.args.get('max_results'))
    region = request.args.get('region') or 'cn-zh'
    safesearch = request.args.get('safesearch') or 'moderate'
    max_results = int(request.args.get('max_results') or "3")
    results = ddg(keywords, region, safesearch, max_results=max_results)
    print(results)
    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0')
