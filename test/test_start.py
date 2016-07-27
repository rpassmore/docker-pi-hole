
# coding=utf-8
"""docker-pi-hole feature tests."""

import pytest
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers,
)

scenarios('.')

@given('docker <images>')
def docker_images(images):
    """docker <images>."""


@given(parsers.parse('{env_name} environment is provided'))
def an_environment_is_provided(env_name):
    """an environment is provided."""


@when('I run the docker image')
def i_run_the_docker_image():
    """I run the docker image."""


@then(parsers.parse('the container prints: {message}'))
def the_container_errors_saying(message):
    """the container prints"""

@then(parsers.parse('the container started {process}'))
def the_container_errors_saying(process):
    """the container started process"""

@then('the container exits')
def the_container_exits():
    """the container exits."""
