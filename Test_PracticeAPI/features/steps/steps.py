from API_Automation.Test_PracticeAPI.test_API import *
from behave import *

@given('API url is provided for get')
def step_impl(context):
    context.message= 'API url is provided'
    print(context.message)

@when('User executes get method')
def step_impl(context):
    test_getMethod()
    context.msg = 'Get method is successfully executed'
    print(context.msg)

@then('User checks the response code for get')
def step_impl(context):
    print(context.msg)

@given('API url is provided for put')
def step_impl(context):
    context.message = 'API url is provided'
    print(context.message)

@when('User executes Put method')
def step_impl(context):
    test_putMethod()
    context.msg = 'Put method is successfully executed'

@then('User checks the response code for put')
def step_impl(context):
    context.msg = 'Response code is generated and Put method is executed'

@given('API url is provided for post')
def step_impl(context):
    context.message = 'API url is provided'
    print(context.message)

@when('User executes Post method')
def step_impl(context):
    test_postMethod()
    context.msg = 'Post method is successfully executed'

@then('User checks the response code for post')
def step_impl(context):
    context.msg = 'Response code is generared and post method is successfully executed'


@given('API url is provided for Delete')
def step_impl(context):
    context.message = 'API url is provided'
    print(context.message)


@when('User executes Delete method')
def step_impl(context):
    test_deleteMethod()
    context.msg = 'Delete method is successfully executed'


@then('User checks the response code for delete')
def step_impl(context):
    context.msg = 'Response code is generared and delete method is successfully executed'


