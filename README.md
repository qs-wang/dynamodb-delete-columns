Python cli to delete attributes of DynamoDB table
==========================

This is the simple tool I am using for deleting the attributes from DynamoDB


### Create a Virtual Environment

After cloning or downloading the repo, create a Python virtual environment with:

```
python -m venv .virtualenv
```

if the `pyvenv` command does not exist on your system.

### Activate the Virtual Environment

Now activate the virtual environment. on macOS, Linux and Unix systems, use:

```
source .virtualenv/bin/activate
```

On Windows:

```
.virtualenv\Scripts\activate.bat
```

### Install the Development Environment

Now run:

```
pip install -r requirements.txt
pip install -e .[dev]
```

This will install the packages the project depends on in production as well as packages needed during development.

### Run the command
drmps --profile dev --region ap-southeast-2 --table qs_table --properties '["key1","key2"]' --primary tableId
