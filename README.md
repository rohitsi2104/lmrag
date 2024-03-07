
# lmrag Package Installation and Project Setup

1. Open your project in the terminal.
2. Run the following command to install the lmrag package using the .whl file:


```http
  pip install dist/lmrag-0.1-py3-none-any.whl
```

## Starting a New Project with default configuration

1. Decide on the directory where you want to create and launch your new project.

2. Run the following command to create a new project named project_name using the lmrag package:

```http
  lmrag createproject project_name
```

## Starting a New Project with user configuration

```http
  lmrag createproject project_name/your/path/to --secret-key "abc123"
```

After creating your project a web application will automatically launch and you are ready to promt your queries. 

## Happy Prompting......!


## Creating a .whl file and creating package 

```http
  python setup.py sdist bdist_wheel
```