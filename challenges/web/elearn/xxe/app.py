from flask import Flask, request
from lxml import etree

app = Flask(__name__)


@app.route('/cert/verify', methods=['GET', 'POST'])
def cert_verify():
    parsed_xml = None
    if request.method == 'POST':
        xml = request.form['data']
        parser = etree.XMLParser(no_network=False, dtd_validation=True)
        try:
            doc = etree.fromstring(bytes(xml, encoding='utf8'), parser)
            parsed_xml = etree.tostring(doc)
            return {'status': 'success', 'message': 'Certificate verified'}
        except Exception as e:
            return {'status': 'error', 'error': 'Unable to parse XML', 'message': str(e)}
    return {'app_name': 'Elearn Certificate Verification (Deprecated)',
            'message': 'Fields required: data'}


if __name__ == "__main__":
    app.run(debug=True)
