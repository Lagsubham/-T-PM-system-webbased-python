Requirement:
    1. pip install pyparsing pydot
    2. graphviz.exe cmake

SETTINGS.py:
    1. GRAPH_MODELS = {
        'all_applications' : True,
        'group_models': True,
        }
         # at end
    2.  'django_extensions',
        # in installed apps 

python manage.py graph_models -a > erd.dot
python manage.py graph_models --pydot -a -g -o erd.pdf
