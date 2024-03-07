from setuptools import setup, find_packages

setup(
    name='lmrag',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'pyyaml',
        'langchain',
        'openai',
        'python-dotenv',
        'streamlit',
        'subprocess'
        
    ],
    entry_points={
        'console_scripts': [
            'lmrag = lmrag.cli:cli',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
