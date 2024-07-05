import os
from bs4 import BeautifulSoup


xml_dir = 'xml'
config_dir = 'containers'
xml_files = os.listdir(xml_dir)

for xml_file in xml_files:
    with open(f'{xml_dir}/{xml_file}', 'r') as f:
        try:
            soup = BeautifulSoup(f.read(), 'xml')
        except:
            print(f'Error parsing {xml_file}')
            continue
    name = soup.find('Name').text
    repo = soup.find('Repository').text
    parameters = soup.find_all('Config')
    for p in parameters:
        if p.get('Type') == 'Port':
            if p.get('Default') == '':
                p['Default'] = p.get('Target')
    ports = [{'name': p.get('Name').upper().replace(' ','_'),'target':p.get('Target'), 'value':p.get('Default'), 'mode': p.get('Mode')} for p in parameters if p.get('Type') == 'Port']
    variables = [{'target':p.get('Target'), 'value':p.get('Default')} for p in parameters if p.get('Type') == 'Variable']
    volumes = [{'name': p.get('Name').upper().replace(' ','_'), 'target':p.get('Target'), 'value':p.get('Default')[9:]} for p in parameters if p.get('Type') == 'Path']

    run_cmd = 'COMMAND="docker run -d --name={{NAME}} '
    for port in ports:
        port["name"].replace('/', '_').replace(' ', '_').replace('-', '_').replace('.', '_').replace('(', '').replace(')', '').replace('"', '').replace("'", '')
        run_cmd += f'-p {{{{{port["name"]}}}}}:{port["target"]}/{port["mode"]} '
    for volume in volumes:
        volume["name"].replace('/', '_').replace(' ', '_').replace('-', '_').replace('.', '_').replace('(', '').replace(')', '').replace('"', '').replace("'", '')
        run_cmd += f'-v {{{{{volume["name"]}}}}}:{volume["target"]} '
    for variable in variables:
        if variable["target"] != 'UMASK' and variable["target"] != 'PUID' and variable["target"] != 'PGID':
            run_cmd += f'-e {variable["target"]}={{{{{variable["target"]}}}}} '
        else:
            run_cmd += f'-e {variable["target"]}={variable["value"]} '
    file_content = f'{run_cmd}{repo}"\n'


    file_content += f'NAME={name}\n'

    for p in ports:
        if p['value'] == '':
            p['value'] = 'CUSTOM_VALUE'
        file_content += f'{p["name"]}={p["value"]}\n'


    for v in variables:
        if ' ' in v['value']:
            v['value'] = '"'+"'"+v["value"]+"'"+'"'
        if v['value'] == '':
            v['value'] = '"'+"''"+'"'
        if v["target"] != 'UMASK' and v["target"] != 'PUID' and v["target"] != 'PGID':
            file_content += f'{v["target"]}={v["value"]}\n'

    for v in volumes:
        v['name'] = v['name'].replace('/', '_').replace(' ', '_').replace('-', '_').replace('.', '_').replace('(', '').replace(')', '').replace('"', '').replace("'", '')
        if 'DOCKER' in v["name"]:
            file_content += f'{v["name"]}=/var/run/docker.sock\n'
        if v['value'] == '':
            v['value'] = f'/appdata/{name}'
        if v['name'] in file_content:
            continue
        file_content += f'{v["name"]}={v["value"]}\n'

    file_content = file_content.replace(':_/', '_')
    with open(f'{config_dir}/{name.lower()}.conf', 'w') as f:
        f.write(file_content)