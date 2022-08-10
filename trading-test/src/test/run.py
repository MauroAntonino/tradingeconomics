from test.test_get_callbackurl import suite
from test.test_get_token import suite as suite_2
from test.test_authorize_params import suite as suite_3
from unittest import TextTestRunner

runner = TextTestRunner()
runner.run(suite())
runner.run(suite_2())
runner.run(suite_3())