import os


def dump_json_temp(new_content):
    if os.path.exists('../bash-scripts/temp.sh'):
        os.remove('../bash-scripts/temp.sh')
    with open('../bash-scripts/temp.sh', 'x'):
        pass
    os.system('chmod +x ../bash-scripts/temp.sh')

    with open('../bash-scripts/temp.sh', 'w') as template_file:
        template_file.write(new_content)
    template_file.close()
