import re


print('Enter the run command')
run_command = input('> ')

ports = [[port[0], f'{port[0]}{port[2]}' if port[2] else port[0]] for port in re.findall(r'-p (\d+):(\d+)(/(tcp|udp))?', run_command)]
volumes = [list(volume) for volume in re.findall(r'-v (\S+):(\S+)', run_command)]
variables = [list(variable) for variable in re.findall(r'-e (\S+)=(\S+)', run_command)]


file = 'COMMAND="docker run -d --name={{NAME}} --restart={{RESTART_POLICY}} '

for port in ports:
    port[0] = f'PORT_{port[0]}'
    file += f'-p {{{{{port[0]}}}}}:{port[1]} '
for volume in volumes:
    if volume[1] == '/var/run/docker.sock':
        volume[0] = 'DOCKER_SOCKET'
    else:
        volume[0] = volume[1].replace('/', '_').upper()
        if volume[0].startswith('_'):
            volume[0] = volume[0][1:]
    file += f'-v {{{{{volume[0]}}}}}:{volume[1]} '
for variable in variables:
    if variable[0] != 'UMASK' and variable[0] != 'PUID' and variable[0] != 'PGID':
        variable[1] = variable[0]
        file += f'-e {variable[0]}={{{{{variable[1]}}}}} '
    else:
        file += f'-e {variable[0]}={variable[1]} '
        variables.remove(variable)

file += run_command.split()[-1]+'"'+"\n"
name = run_command.split('/')[-1]
file += f"NAME={name}\n"
for port in ports:
    file += f"{port[0]}={port[1]}\n"
for volume in volumes:
    file += f"{volume[0]}={volume[1]}\n"
for variable in variables:
        file += f"{variable[0]}={variable[1]}\n"

file += 'RESTART_POLICY=unless-stopped'

with open(f'{name}.conf', 'w') as f:
    f.write(file)
