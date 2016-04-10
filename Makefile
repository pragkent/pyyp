bdist:
	python setup.py bdist_wheel

publish: bdist
	twine upload dist/*

clean:
	rm -rf pyyp.egg-info build dist
