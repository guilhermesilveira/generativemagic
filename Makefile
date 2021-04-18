build:
	git stash
    python -m pip install --upgrade build
    python -m build
    pip install bumpversion twine
    python setup.py sdist bdist_wheel
    tar tzf dist/generativemagic-0.8.0.tar.gz
    read
    twine check dist/*
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
