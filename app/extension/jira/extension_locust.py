import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')

@jira_measure("locust_app_specific_action_matrix")
def app_specific_action_matrix(locust):
    logger.error(f"XXXXXXXXXXXXXXXXXXXXXXXXXX")
    r = locust.get('/rest/softcomply/rm/1.0/api/projects/RISK/matrix', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    token_pattern_example = '"token":"(.+?)"'
    id_pattern_example = '"id":"(.+?)"'
    token = re.findall(token_pattern_example, content)  # get TOKEN from response using regexp
    id = re.findall(id_pattern_example, content)    # get ID from response using regexp

    logger.locust_info(f'token: {token}, id: {id}')  # log information for debug when verbose is true in confluence.yml file
    if 'assertion string' not in content:
        logger.error(f"'assertion string' was not found in {content}")
    assert 'RISK' in content  # assert specific string in response content

    #body = {"id": id, "token": token}  # include parsed variables to POST request body
    #headers = {'content-type': 'application/json'}
    #r = locust.post('/app/post_endpoint', body, headers, catch_response=True)  # call app-specific POST endpoint
    #content = r.content.decode('utf-8')
    #if 'assertion string after successful POST request' not in content:
    #    logger.error(f"'assertion string after successful POST request' was not found in {content}")
    #assert 'assertion string after successful POST request' in content  # assertion after POST request

@jira_measure("locust_app_specific_action_table")
def app_specific_action_table(locust):
    logger.error(f"XXXXXXXXXXXXXYYYYXXXXXXXXXXXXX")
    r = locust.get('/rest/softcomply/rm/1.0/api/projects/RISK/table', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    token_pattern_example = '"token":"(.+?)"'
    id_pattern_example = '"id":"(.+?)"'
    token = re.findall(token_pattern_example, content)  # get TOKEN from response using regexp
    id = re.findall(id_pattern_example, content)    # get ID from response using regexp

    logger.locust_info(f'token: {token}, id: {id}')  # log information for debug when verbose is true in confluence.yml file
    if 'assertion string' not in content:
        logger.error(f"'assertion string' was not found in {content}")
    assert 'RISK' in content  # assert specific string in response content
