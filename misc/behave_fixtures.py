# -- FILE: my_django/behave_fixtures.py
from behave import fixture
import django
from os import close, unlink
import tempfile
from behave import fixture, use_fixture
# flaskr is the sample application we w
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
from flaskr import app, init_db
@fixture
def django_test_runner(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()
    yield
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()

@fixture
def django_test_case(context):
    context.test_case = LiveServerTestCase
    context.test_case.setUpClass()
    yield
    context.test_case.tearDownClass()
    del context.test_case

@fixture
def flaskr_client(context, *args, **kwargs):
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    app.testing = True
    context.client = app.test_client()
    with app.app_context():
        init_db()
    yield context.client
    # -- CLEANUP:
    close(context.db)
    unlink(app.config['DATABASE'])

def before_feature(context, feature):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(flaskr_client, context)
