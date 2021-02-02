from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    try:
        data = json.loads(request.data)
        alerts = data['alerts']
        for item in alerts:
            print('SEND SMS: ' + str(item))
            alertname=item["labels"]["alertname"]
            namespace=item["labels"]["namespace"]
            pod_name=item["labels"]["pod_name"]
            severity=item["labels"]["severity"]
            summary=item["annotations"]["summary"]
            print(alertname,namespace,pod_name,severity,summary)
    except Exception as e:
        print(e)
    return 'ok'
