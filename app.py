from flask import Flask, render_template, request

app = Flask(__name__)

# Define your access control functions here
def rbac_has_access(user_name, resource):
    roles = {
        "role1": {"files": "read_only", "records": "read_write"},
        "role2": {"files": "read_write", "records": "read_write"}
    }

    def get_users(role):
        if role == "role1":
            return ["Baraa", "Ayat"]
        elif role == "role2":
            return ["Alice", "Bob"]
        else:
            return []

    for role, permissions in roles.items():
        if user_name in get_users(role) and resource in permissions:
            access_type = roles[role][resource]
            return f"{user_name} belongs to {role} and has {access_type} access to {resource}."
    return f"{user_name} does not have access to {resource}."

def abac_has_access(user_name, resource):
    jobs = {
        "managers": {"files": "read_write", "videos": "read_write"},
        "staff": {"files": "read_only", "videos": "read_only"}
    }

    def get_users(job):
        if job == "managers":
            return ["Baraa", "Ayat"]
        elif job == "staff":
            return ["Alice", "Bob"]
        else:
            return []

    for job, permissions in jobs.items():
        if user_name in get_users(job) and resource in permissions:
            access_type = jobs[job][resource]
            return f"{user_name} in {job} has {access_type} access to {resource}."
    return f"{user_name} does not have access to {resource}."

def dac_has_access(user_type, resource_name):
    resources = {
        "files": "public",
        "videos": "public",
        "company records": "private",
    }

    if resource_name in resources:
        if user_type == "owner":
            return f"User ({user_type}) has access to the {resource_name} resource."
        elif user_type == "visitor" and resources[resource_name] == "public":
            return f"User ({user_type}) has access to the {resource_name} resource."
        else:
            return f"User ({user_type}) does not have access to the {resource_name} resource."
    else:
        return f"Resource '{resource_name}' not found."

def mac_has_access(user_security_level, resource):
    RESOURCES = {
        "videos": 3,
        "company records": 4
    }

    if resource in RESOURCES:
        resource_security_level = RESOURCES[resource]
        if user_security_level >= resource_security_level:
            return f"User with security level {user_security_level} has access to {resource} with security level {resource_security_level}"
        else:
            return f"User with security level {user_security_level} does not have access to {resource} with security level {resource_security_level}"
    else:
        return "Resource not found"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/abac', methods=['GET', 'POST'])
def abac():
    if request.method == 'POST':
        user_name = request.form['user_name']
        resource = request.form['resource']
        result = abac_has_access(user_name, resource)
        return render_template('result.html', result=result)
    return render_template('abac.html')

@app.route('/rbac', methods=['GET', 'POST'])
def rbac():
    if request.method == 'POST':
        user_name = request.form['user_name']
        resource = request.form['resource']
        result = rbac_has_access(user_name, resource)
        return render_template('result.html', result=result)
    return render_template('rbac.html')

@app.route('/dac', methods=['GET', 'POST'])
def dac():
    if request.method == 'POST':
        user_type = request.form['user_type']
        resource_name = request.form['resource_name']
        result = dac_has_access(user_type, resource_name)
        return render_template('result.html', result=result)
    return render_template('dac.html')

@app.route('/mac', methods=['GET', 'POST'])
def mac():
    if request.method == 'POST':
        user_security_level = int(request.form['user_security_level'])
        resource = request.form['resource']
        result = mac_has_access(user_security_level, resource)
        return render_template('result.html', result=result)
    return render_template('mac.html')

if __name__ == '__main__':
    app.run(debug=True)
