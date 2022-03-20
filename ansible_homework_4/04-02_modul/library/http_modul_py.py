#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: http_modul_py
author: A.
short_description: module requests http code
description:
  - module requests http code
version_added: 1.0.0
options:
  adress:
    description:
      - uri adress
      - This is a required parameter
    type: str
'''

EXAMPLES = r'''
- name: http module python
  http_modul_py:
    adress: 'https://yandex.ru'
  register: py_result
  connection: local

- name: print result http modul python
  debug:
    msg: "{{ py_result }}"
  
'''

RETURN = r'''
msg:
  description: Errors if occured
  returned: always
  type: str
  sample: ""
result_str:
  description: final string
  returned: always
  type: str
  sample: 200
rc:
  description: Return code
  returned: always
  type: int
  sample: 0
'''

from ansible.module_utils.basic import (
    AnsibleModule
)
import requests

def http_reqest(adress):
    failed = False
    msg = "Success"
    rc = 0
    # Формируем конечную строку
    try:
        response = requests.get(adress)
        result = response.status_code
    except TypeError as e:
        failed = True
        result = ""
        msg = "TypeError"
        rc = 1
    return(failed, result, rc, msg)


def main():
    # Задаем аргументы модуля
    module_args = dict(
        adress=dict(required=True, type='str')
    )
    # Создаем объект - модуль
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    # Получаем из модуля аргументы
    adress = module.params["adress"]
    # Вызываем нашу функцию
    result = http_reqest(adress)
    # Если задача зафейлилась
    if result[0]:
        module.fail_json(changed=False,
                         failed=result[0],
                         result_str=result[1],
                         rc=result[2],
                         msg=result[3])
    # Если задача успешно завершилась
    else:
        module.exit_json(changed=False,
                         failed=result[0],
                         result_str=result[1],
                         rc=result[2],
                         msg=result[3])

if __name__ == "__main__":
    main()
