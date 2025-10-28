# SES-DocGuard Rules Configuration

This directory contains YAML files that define the rules for the ASD STE (Error-detection ruleset for Technical Publications). The rules are designed to ensure compliance with various standards and guidelines for technical documentation, specifically focusing on CMMs, ESMs, AMMs, SBs, and related deliverables.

## File Structure

- **asd_ste_ruleset_example.yaml**: This file provides an example configuration of the ASD STE ruleset. It includes various checks such as mandatory field presence, formatting and style consistency, specification compliance, and more.

## Usage

To add new rules or modify existing ones, create a new YAML file in this directory following the structure outlined in the example file. Each rule should include the following fields:

- **rule_id**: A unique identifier for the rule.
- **severity**: The severity level of the rule (e.g., low, medium, high).
- **example_violation**: An example of a violation for this rule.
- **correction_template**: Suggested corrections for the violation.

Ensure that any new rules added are accompanied by corresponding unit tests in the `tests/rules_tests/` directory.

## Important Notes

- All rules must be documented clearly to facilitate understanding and maintenance.
- Regular updates to the ruleset may be necessary to adapt to new standards or feedback from users.
- Ensure that any changes to the rules are reflected in the documentation and communicated to the team.