old ?= "sample"
new ?= "sample"
# pyproject.tomlのnameを取得する
PACKAGE_NAME := $(shell grep name pyproject.toml | sed -e 's/name = "//g' -e 's/"//g')

init:
	rm -rf ./venv poetry.lock
	which poetry || pip3 install poetry
	./rename.sh $(old) $(new)
	poetry install

run:
	poetry run python -m ${PACKAGE_NAME}

docker:
	docker image build -t ${PACKAGE_NAME} .
	docker run --rm ${PACKAGE_NAME} python -m ${PACKAGE_NAME}
