from CV_prompt import candidate_getter
from CV_metadata_extractor import metadata_finder
from flask import Flask, json, request, jsonify



app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True



@app.route('/candidate', methods=['POST'])
def get_candidate():
    app.logger.debug("JSON received...")
    app.logger.debug(request.json)
    if request.headers['Content-Type'] == 'application/json':
        content=request.json
        position_label=content['label']
        skills=content['skills']
        CV_directory=content['directory']
        candidate=candidate_getter(CV_directory, skills, position_label)
        return jsonify(candidate)
    else:
        return "no json received"


@app.route('/metadata', methods=['POST'])
def get_metadata():
    app.logger.debug("JSON received...")
    app.logger.debug(request.json)
    if request.headers['Content-Type'] == 'application/json':
        content=request.json
        CV_directory=content['directory']
        metadata=metadata_finder(CV_directory)
        return jsonify(metadata)
    else:
        return "no json received"


if __name__ == "__main__":
    app.run('127.0.0.1', port=80)
