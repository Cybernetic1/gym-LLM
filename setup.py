from setuptools import setup, find_packages

setup(name='gym_LLM',
      version='0.0.1',
      description='LLM (Large Language Model) OpenAi Gym environment',
      url='https://github.com/Cybernetic1/gym-LLM',
      author='YKY',
      author_email='generic.intelligence@gmail.com',
      license='MIT License',
      packages=find_packages(),
      package_data={},
      zip_safe=False,
      install_requires=['gym>=0.2.3'],
      dependency_links=[]
      )
