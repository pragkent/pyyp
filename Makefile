bdist:
	python setup.py bdist_wheel

publish: bdist
	twine upload dist/*

test:
	py.test tests/

clean:
	rm -rf pyyp.egg-info build dist
