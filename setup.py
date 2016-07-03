from setuptools import setup

setup(name='basicapp',
      version='0.1',
      description='flask facade to scraper workers',
      long_description='TODO: more in depth here....!',
      classifiers=[
            'Development Status :: 3 - Beta',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Network :: <various>',
      ],
      keywords='funniest joke comedy flying circus',
      url='https://github.com/johnpappas/basicapp.git',
      author='John Pappas',
      author_email='john.steven.pappas@gmail.com',
      license='MIT',
      packages=['basicapp'],
      install_requires=[
            'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      scripts=['bin/german-joke'],
      entry_points={
            'console_scripts': ['icelandic-beer=basicapp.command_line:main'],
      },
      zip_safe=False)
