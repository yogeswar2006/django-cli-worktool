import os

def switching_env(target_env):
    env_file_path = os.path.join(os.getcwd(), ".env")

    with open(env_file_path, "r") as f:
        lines = f.readlines()

    current_env = None

    # detect current ENV
    for line in lines:
        if line.startswith("ENV="):
            current_env = line.strip().split("=")[1]

    if current_env == target_env:
        print(f"Already in {target_env} mode!")
        return

    # update ENV and DEBUG
    new_lines = []
    for line in lines:
        if line.startswith("ENV="):
            new_lines.append(f"ENV={target_env}\n")
        elif line.startswith("DEBUG="):
            if target_env == "dev":
                new_lines.append("DEBUG=True\n")
            else:
                new_lines.append("DEBUG=False\n")
        else:
            new_lines.append(line)

    with open(env_file_path, "w") as f:
        f.writelines(new_lines)

    print(f"Switched to {target_env} mode!")