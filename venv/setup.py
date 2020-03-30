from setuptools import setup, find_packages

with open('readme.md') as readme_file:
    README = readme_file.read()

with open('history.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='wangtools',
    version='0.1.2',
    description='Useful tools to work with text mining in Python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Xiaoou WANG',
    author_email='xiaoouwangfrance@gmail.com',
    keywords=['text mining', 'npl', 'corpus'],
    url='https://github.com/xiaoouwang/wangtools',
    download_url='https://pypi.org/project/wangtools/'
)

install_requires = [
    'string'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)