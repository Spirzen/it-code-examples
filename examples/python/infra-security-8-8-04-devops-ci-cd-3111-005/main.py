#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True)
        )
    )
    name = module.params['name']
    greeting = f"Hello, {name}!"
    module.exit_json(changed=False, msg=greeting)

if __name__ == '__main__':
    main()
