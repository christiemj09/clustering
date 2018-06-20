"""
Install clustering.
"""

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Cluster identifiers deemed to be equivalent',
		'author': 'Matt Christie',
		'download_url': 'https://github.com/christiemj09/clustering.git',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		'py_modules': ['clustering'],  # just a single module
		'scripts': ['bin/clustering-demo'],
		'name': 'clustering'
	}

	setup(**config)	

if __name__ == '__main__':
	main()
