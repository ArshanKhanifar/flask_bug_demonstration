# flask_bug_demonstration
Bug demonstration for Flask 1.1.0
This repo contains a pytest test case that tests the bug in this [issue](https://github.com/pallets/flask/issues/3287). 

# Setup
```
git clone https://github.com/ArshanKhanifar/flask_bug_demonstration.git
conda create -n bug_demo -y python=3
conda activate bug_demo
./pip_install.sh
```

# Running
```
export PYTHONPATH=src:$PYTHONPATH
pytest ./test  # This will fail with flask 1.1.0

pip install flask==1.0.3
pytest ./test  # This will pass.
```
