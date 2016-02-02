import json
import six

from meetup.api import API_SERVICE_FILES
from meetup.util import multikeysort

OMIT_SERVICE = ['CreateBatch', 'Widget', 'WidgetQuery']


def api_calls_to_rst(service_dict):
    common_parameters = {
        'omit': 'Retrieve all default fields excluding those specified',
        'offset': 'The starting page for results to return. For example, when page = 10, specifying ' +
                  '"offset=0" will bring back records 1-10, "offset=1" will bring records 11-20, etc.',
        'order': 'How to order the results, in this case by # of members. To reverse the sorting order, ' +
                 'you include the parameter "desc=desc" or "desc=true"',
        'only': 'Retrieve only those fields specified',
        'page': 'The page size (maximum number of results in each response) to use on the results',
        'desc': 'Reverses the sorting order, when you include the parameter "desc=desc" or "desc=true"',
    }
    output = []
    for service_name in sorted(six.iterkeys(service_dict)):
        service_details = service_dict.get(service_name)
        parameters = []
        service_output = []
        try:
            for param_name, param_details in six.iteritems(service_details.get('parameters', {})):
                if param_name not in six.iterkeys(common_parameters):
                    parameters.append({'name': param_name,
                                       'desc': param_details['description'],
                                       'required': param_details['required']})
        except AttributeError:
            pass
        parameters = multikeysort(parameters, ['-required', 'name'])

        params = ', '.join([param['name'] for param in parameters])
        service_output.append('.. py:class:: meetup.api.Client')
        service_output.append('')
        service_output.append('    .. py:method:: {func_name}({params})'.format(func_name=service_name,
                                                                                params=params))
        service_output.append('\n    {0}'.format(service_details.get('summary')))
        if service_details.get('notes'):
            notes = service_details.get('notes')
            notes.replace('\n ', '\n')
            line_prefix = ' ' * 4
            in_pre_block = False
            for line in notes.split('\n'):
                if '<pre>' in line:
                    line = line_prefix + '.. code-block:: javascript\n'
                    in_pre_block = True
                elif '</pre>' in line:
                    line = ''
                    in_pre_block = False
                elif '####' in line:
                    line = line_prefix + '**' + line.strip('# ') + '**'
                else:
                    if in_pre_block:
                        line = line_prefix + line_prefix + line
                    else:
                        line = line_prefix + line.strip()
                service_output.append(line)

        service_output.append('\n    URI: {0}'.format(service_details.get('uri')))
        service_output.append('\n    API Version: {0}\n'.format(service_details.get('version')))
        for param in parameters:
            param_name = param.get('name')
            if param.get('name') in six.iterkeys(common_parameters):
                param_desc = common_parameters.get(param_name)
            else:
                param_desc = param.get('desc')

            service_output.append('    :param {name}: {desc}'.format(name=param_name, desc=param_desc))

            if param.get('required'):
                service_output.append('    :type {name}: required'.format(name=param_name))
        service_output.append('')
        output.append('\n'.join(service_output))
    return output


if __name__ == '__main__':
    services = {}
    for version, file_name in API_SERVICE_FILES:
        api_data = json.load(open(file_name))
        for service_name, service_details in six.iteritems(api_data['operations']):
            if service_name not in OMIT_SERVICE:
                services[service_name] = service_details
    api_method_docs = api_calls_to_rst(services)
    print("""
API Client
----------

The following are dynamically generated methods for the :py:class:`meetup.api.Client` class.

API Client Index
^^^^^^^^^^^^^^^^
.. hlist::
    :columns: 2
""")

    for service_name in sorted(six.iterkeys(services)):
        print('    - :py:meth:`{0}()<meetup.api.Client.{0}>`'.format(service_name))

    print("""
API Client Methods
^^^^^^^^^^^^^^^^^^
""")
    print('\n'.join(api_method_docs))
