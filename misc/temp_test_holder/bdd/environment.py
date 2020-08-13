from behave import use_fixture
from my_django.behave_fixtures import django_test_runner, django_test_case
from  os import environ

environ["DJANGO_SETTINGS_MODULE"] = "stevebooks.settings"

def before_all(context):
    use_fixture(django_test_runner, context)

def before_scenario(context, scenario):
    use_fixture(django_test_case, context)
