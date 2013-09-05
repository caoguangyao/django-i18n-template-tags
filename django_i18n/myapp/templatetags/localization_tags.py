from django import template
import os
from django.conf import settings #import TEMPLATE_DIRS

register = template.Library()

@register.simple_tag
def localization(key, language_file_name):
    '''
    usage:
    create a language file as localized string configure in your template folder.

    Eg: in templates/chinese:

    '''
    dirs = getattr(settings,'TEMPLATE_DIRS',None)

    print '@16',key,language_file_name
    print '@17',dirs

    for directory in dirs:
        path = os.path.join(directory,language_file_name)
        print '@23',path
        if(get_file(path)):
            value = read_file(path,key)
            if value:
                return value

    #if not find the value,keep it.
    return key 

def read_file(path, key):
    print '@32',path
    fp = open(path)
    for line in fp.readlines():
        k, v = line.split('=')
        k, v = k.strip(), v.strip()
        if k == key:
            return v
    return None

def get_file(path):
    return os.path.isfile(path)
