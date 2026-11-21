
# Create environment:

```
conda env create -f environment.yml
```

# Useful commands

| Action                  | Command                                       |
| ----------------------- | --------------------------------------------- |
| Activate environment    | `conda activate physics`                      |
| Deactivate environment  | `conda deactivate`                            |
| Update environment      | `conda env update -f environment.yml --prune` |
| Open JupyterLab         | `jupyter lab`                                 |
| Open JupyterLab without browser         | `jupyter lab --no-browser`                                 |
| List installed packages | `conda list`                                  |
| Show environemnts       | `conda env list`                              |


# Workflow

```
conda activate physics
jupyter lab --no-browser
```


# Fixing Pycharm

Pycharm managed server:

For an environment called physics

First create the kernelspec, in the Anaconda Prompt:
```
conda activate physics
conda install ipykernel
python -m ipykernel install --user --name physics --display-name "physics"
```
That creates `C:\Users\Marian\AppData\Roaming\jupyter\kernels\physics\kernel.json`. Add this env block to it:

```json
 "env": {
  "PATH": "C:\\Users\\Marian\\anaconda3\\envs\\physics;C:\\Users\\Marian\\anaconda3\\envs\\physics\\Library\\mingw-w64\\bin;C:\\Users\\Marian\\anaconda3\\envs\\physics\\Library\\usr\\bin;C:\\Users\\Marian\\anaconda3\\envs\\physics\\Library\\bin;C:\\Users\\Marian\\anaconda3\\envs\\physics\\Scripts;C:\\Windows\\system32;C:\\Windows",
  "CONDA_PREFIX": "C:\\Users\\Marian\\anaconda3\\envs\\physics",
  "CONDA_DEFAULT_ENV": "physics"
 }
```

Check paths, depends on user name, e.g. `maria` instead of `Marian`

For more detail see [here](https://claude.ai/chat/42c1d0d6-e526-4840-a1a2-bb096d7b4982).

