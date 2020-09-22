import os
import pydevd_pycharm
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def hello_world():
    msg = 'Okteto hard to use'
    dd = request.form.to_dict()
    print(dd)
    return msg

def attach():
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('0.0.0.0', port=3500, stdoutToServer=True, stderrToServer=True)

if __name__ == '__main__':
  print('Starting hello-world server...')
  # comment out to use Pycharm's remote debugger
  # attach()

  app.run(host='0.0.0.0', port=8080)
