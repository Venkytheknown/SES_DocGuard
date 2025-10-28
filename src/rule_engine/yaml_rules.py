def load_yaml_rules(yaml_file):
    import yaml

    with open(yaml_file, 'r') as file:
        rules = yaml.safe_load(file)

    return rules

def apply_yaml_rules(text_content, rules):
    results = []
    
    for rule in rules:
        rule_id = rule.get('rule_id')
        rule_description = rule.get('description')
        severity = rule.get('severity')
        check_function = rule.get('check_function')

        if check_function and callable(check_function):
            violation = check_function(text_content)
            if violation:
                results.append({
                    'rule_id': rule_id,
                    'rule_description': rule_description,
                    'severity': severity,
                    'evidence_snippet': violation
                })

    return results

def validate_with_rules(text_content, rules_dir='./configs/rules'):
    import os

    results = []
    for rule_file in os.listdir(rules_dir):
        if rule_file.endswith('.yaml'):
            rules = load_yaml_rules(os.path.join(rules_dir, rule_file))
            validation_results = apply_yaml_rules(text_content, rules)
            results.extend(validation_results)

    return results