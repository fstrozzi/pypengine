import yaml
import re

def parse_yaml(yaml_file):
     with open(yaml_file) as f:
        return yaml.load(f)

def extract_variables(line):
    variables = []
    for match in re.finditer('<(\S+)>',text):
        variables.append(match.group(0).replace(">",'').replace('<',''))
        return variables

#def substitute_variable(variable,steps,resources):
