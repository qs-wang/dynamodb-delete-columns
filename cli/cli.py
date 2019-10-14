# -*- coding: utf-8 -*-
r"""This module is used to use the Boto3 SDK to manipulate the Jobs DB.

Example:
    ::
        $ pip install -e .
        $ drmps --profile dev --region ap-southeast-2 --table qs_table --properties '["key1","key2"]'


.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

"""
import os
import re
import sys

import click
import ast
import cli.dynamodb as dynamodb

class PythonLiteralOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)

@click.command()
@click.option(
    "--profile",
    envvar="AWS_PROFILE",
    required=True,
    help="AWS profile",
)
@click.option(
    "--region",
    envvar="AWS_REGION",
    required=True, help="AWS region"
)
@click.option(
    "--table",
    required=True,
    help="The Dynamo DB name.",
)
@click.option(
    "--properties",
    cls=PythonLiteralOption,
    default=[],
    required=True,
    help="The properties to be removed."
)

@click.option(
    "--primary",
    required=True,
    help="The primary."
)
def cli(profile, region, table, properties,primary):
    """DynamoDB properties removal Tool."""
    count = dynamodb.scan_table_and_remove(profile, region, table, properties,primary)
    print("{} records updated".format(count))
