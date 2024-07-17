import os
import re
from bs4 import BeautifulSoup

def clean(text):
    return text.replace('/', '_').replace(' ', '_').replace('-', '_').replace('.', '_').replace('(', '').replace(')', '').replace('"', '').replace("'", '').replace(':_/', '_')


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

    for p in ports:
        p['name'] = clean(p['name'])

    for i in range(len(ports)):
        if ports[i]['name'].isdigit() and ports[i]['name'] == ports[i+1]['name']:
            ports[i]['name'] = f"TCP_{ports[i]['name']}"
            ports[i+1]['name'] = f"UDP_{ports[i+1]['name']}"
        elif ports[i]['name'].isdigit():
            ports[i]['name'] = f"PORT_{ports[i]['name']}"

    for v in variables:
        v['target'] = clean(v['target'])
    for v in volumes:
        v['name'] = clean(v['name'])
        

    run_cmd = 'COMMAND="docker run -d --name={{NAME}} --restart={{RESTART_POLICY}} '
    for port in ports:
        run_cmd += f'-p {{{{{port["name"]}}}}}:{port["target"]}/{port["mode"]} '
    for volume in volumes:
        if "DOCKER" in volume["name"]:
            volume['name'] = 'DOCKER_SOCKET'
        run_cmd += f'-v {{{{{volume["name"]}}}}}:{volume["target"]} '
    for variable in variables:
        if variable["target"] != 'UMASK' and variable["target"] != 'PUID' and variable["target"] != 'PGID':
            run_cmd += f'-e {variable["target"]}={{{{{variable["target"]}}}}} '
        else:
            run_cmd += f'-e {variable["target"]}={variable["value"]} '
    file_content = f'{run_cmd}{repo}"\n'
    

    pattern = r'\{\{([^}]+)\}\}'
    matches = re.findall(pattern, file_content)

    # matches = [x for i, x in enumerate(matches) if x not in matches[:i]]
    parameters = [{'name': m, 'value': ''} for m in matches]
    
    for p in parameters:
        if p['name'] in [x['name'] for x in ports]:
            p['value'] = ports[[x['name'] for x in ports].index(p['name'])]['value']
        if p['name'] in [x['target'] for x in variables]:
            p['value'] = variables[[x['target'] for x in variables].index(p['name'])]['value']
        if p['name'] in [x['name'] for x in volumes]:
            p['value'] = volumes[[x['name'] for x in volumes].index(p['name'])]['value']
            
        if p['name'] == 'NAME':
            p['value'] = name
        if p['name'] == 'DOCKER_SOCKET':
            p['value'] = '/var/run/docker.sock'
        file_content += f'{p["name"]}={p["value"]}\n'

    file_content += 'RESTART_POLICY=unless-stopped'
    with open(f'{config_dir}/{name.lower()}.conf', 'w') as f:
        f.write(file_content)


