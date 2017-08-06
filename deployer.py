import json, os, subprocess

default_config = json.load(open("config.json"))
subprocess.call([
    "wget",
    "-r",
    "-p",
    "-np",
    "-k",
    default_config['site'],
    "--adjust-extension"
])

print("--------------------------------push pages--------------------------------")
os.chdir(default_config['site'])

if not os.path.exists(".git"):
    subprocess.call([
        'git',
        'init'
    ])

subprocess.call([
    'git',
    'config',
    'user.name',
    default_config['user'],
])
subprocess.call([
    'git',
    'config',
    'user.email',
    default_config['email']
])
subprocess.call([
    'git',
    'remote',
    'add',
    'origin',
    default_config['repo']
])
subprocess.call([
    'git',
    'add',
    '-A'
])
subprocess.call([
    'git',
    'commit',
    '-m',
    'update blog'
])
subprocess.call([
    'git',
    'push',
    'origin',
    'master'
])