from flask import Flask
from bp_tasks import bp as bp_task

app = Flask(__name__)
app.config['SECRET_KEY']="Oh no, Cisco Packet Tracer"
app.register_blueprint(bp_task)

if __name__ == "__main__":
    app.run(debug=True)