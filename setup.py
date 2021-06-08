from setuptools import setup

def parse_requirements(filename):
	lines = (line.strip() for line in open(filename))
	return [line for line in lines if line and not line.startswith("#")]

setup(name='GANDON',
        version='0.1',
        description='PyTorch package for the discrete VAE used for GANDON.',
        url='http://github.com/Kazimiercz/GANDON',
        author='Ebanacio Drochilli',
        author_email='kosoebanymuboyob@gmail.com',
        packages=['gandon'],
        install_requires=parse_requirements('requirements.txt'),
        zip_safe=True)
