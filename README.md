# Project Overview

This project provides a Python example module that demonstrates how to use the SPARQLWrapper library to interact with an Eccence Corporate Memory instance. The module showcases basic SPARQL query execution and result parsing.
Prerequisites

Before running the example, ensure you have the following prerequisites installed:

    Python: A recent version of Python (3.10 or later).
    Poetry: A dependency management tool for Python projects.

# Local CO (Corporate Memory)

While the example can work with a running local CO instance, it's often more convenient to connect to a specific Eccence Corporate Memory instance. To do this, you'll need to set environment variables.
Environment Variables

The following environment variables are required to connect to a specific Eccence Corporate Memory instance:

    CMEM_BASE_URI: The base URI of your Eccence Corporate Memory instance (e.g., https://your-cmem-instance.com).
    OAUTH_GRANT_TYPE: The OAuth grant type used for authentication (e.g., client_credentials).
    OAUTH_CLIENT_ID: The client ID for your application (e.g., cmem-service-account).
    OAUTH_CLIENT_SECRET: The client secret for your application (Important: Replace CHANGE_ME with your actual client secret).

### Setting Environment Variables

The method for setting environment variables depends on your operating system and shell. Here are some common examples:

Linux/macOS:
```Bash
export CMEM_BASE_URI="https://plugin-testing.eccenca.dev"
export OAUTH_GRANT_TYPE="client_credentials"
export OAUTH_CLIENT_ID="cmem-service-account"
export OAUTH_CLIENT_SECRET="your_actual_client_secret"
```

### Clone the Repository:
```Bash
git clone https://github.com/msaipraneeth/example-sparqlwrapper.git
```

### Install Dependencies:


```bash
cd example-sparqlwrapper
poetry install
```
### Running the Example

Make sure the environment variables are set correctly before proceeding.

Execute the Example:
```bash
poetry run python example-sparqlwrapper/__init__.py
```
This will run the example module, which will connect to the specified Eccence Corporate Memory instance, execute a sample SPARQL query, and print the results to the console.

### Customization
SPARQL Query: Modify the SPARQL query within the module to match your specific data retrieval needs.