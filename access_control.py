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

def main():
    # Example usage of rbac_has_access function
    print("RBAC Example:")
    print(rbac_has_access("Baraa", "files"))
    print(rbac_has_access("Bob", "records"))
    print(rbac_has_access("Alice", "videos"))
    print()

    # Example usage of abac_has_access function
    print("ABAC Example:")
    print(abac_has_access("Baraa", "files"))
    print(abac_has_access("Bob", "videos"))
    print(abac_has_access("Alice", "company records"))
    print()

    # Example usage of dac_has_access function
    print("DAC Example:")
    print(dac_has_access("owner", "files"))
    print(dac_has_access("visitor", "videos"))
    print(dac_has_access("visitor", "company records"))
    print()

    # Example usage of mac_has_access function
    print("MAC Example:")
    print(mac_has_access(3, "videos"))
    print(mac_has_access(4, "company records"))
    print(mac_has_access(2, "videos"))
    print()

if __name__ == "__main__":
    main()