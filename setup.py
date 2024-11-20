from setuptools import setup, find_packages

setup(
    name='Appointment Manager',
    version='0.1.0',
    author='Nícolas, Reginaldo e Vitor',
    author_email='_@fatec.sp.gov.br',  # Seu email
    description='Projeto de um gerenciador de agendamentos genérico',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    url='https://github.com/regisboliver/AppointmentManager',
    packages=find_packages(),    # Encontra automaticamente os pacotes
    classifiers=[                # Classificadores para o PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',    # Requisitos da versão do Python
    install_requires=[           # Dependências do seu projeto
        'mysql-connector-python',
        'prettytable',
        'pyodbc'
    ],
)
