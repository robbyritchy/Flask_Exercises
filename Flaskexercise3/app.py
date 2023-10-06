from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
registered_users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        organization = request.form.get('organization')

  
        if not name or not organization:
            return "Both name and organization are required. Please go back and try again."
        if organization not in ["Organization A", "Organization B", "Organization C", "Organization D", "Organization E"]:
            return "Invalid organization. Please select a valid organization."

        registered_users[name] = organization
        return redirect('/registered_users')

    return render_template('registration.html')

@app.route('/registered_users')
def show_registered_users():
    return render_template('registered_users.html', registered_users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)

