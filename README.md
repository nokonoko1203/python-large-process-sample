# app

## usage

- If you want to create a new package, please execute the following command
- Please replace `< your_new_package_name >` with the name of the new package

```bash
% make init new=< your_new_package_name >
```

- You can do the following

```bash
% make run
```

## jupyter

- If you use jupyter notebook, please execute the following command

```bash
poetry add --group dev ipykernel
```

- Also install the `ms-toolsai.jupyter` extension

## docker

- If you use docker, please execute the following command
- By default, it creates and runs an image with the same name as the package name. Modify the Makefile as necessary

```bash
make docker
```
