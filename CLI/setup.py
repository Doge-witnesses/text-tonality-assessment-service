from setuptools import setup

setup(
    name='text_tonality_application',
    version='0.1.0',
    py_modules=['processing_text_cli', 'processing_formatted_text_cli', 'processing_logPart_text_cli, help_cli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'processing_text=processing_text_cli:processing',
            'processing_formatted_text=processing_formatted_text_cli:processing',
            'processing_logPart_text=processing_logPart_text_cli:processing',
            'help=help_cli:help',
        ],
    },
)