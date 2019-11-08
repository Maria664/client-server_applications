import yaml

dict_to_yaml = {
    1: [1, 2, 3],
    2: 2,
    3: {1: '€'}
}

with open('file.yaml', 'w') as f1:
    yaml.dump(dict_to_yaml, f1, allow_unicode=True, default_flow_style=False)
