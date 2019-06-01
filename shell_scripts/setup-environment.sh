cd ../
mkdir -p ./.virtualenvs/myproject_env 
python -m venv ./.virtualenvs/myproject_env 
./.virtualenvs/myproject_env/scripts/activate.bat
python -m pip install --upgrade pip
python -m pip install -r ./config/requirements.txt
