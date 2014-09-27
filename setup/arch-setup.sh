# INSTAL DEPENDENCIES
sudo pacman -Syy
sudo pacman -S --noconfirm base-devel blas lapack gcc-fortran glpk
sudo pacman -S --noconfirm python2 python2-pip python2-virtualenv

# FORCE PYTHON 2
sudo ln -sf /usr/bin/python2 /usr/bin/python
sudo ln -sf /usr/bin/pip2 /usr/bin/pip

# CREATE VIRTUAL ENV
virtualenv2 env
source env/bin/activate

# PYTHON PIP PACKAGES
mkdir ~/.pipcache
source env/bin/activate && pip install --download-cache ~/.pipcache numpy==1.9.0
source env/bin/activate && pip install --download-cache ~/.pipcache FuncDesigner==0.5402
source env/bin/activate && pip install --download-cache ~/.pipcache openopt==0.5402
source env/bin/activate && pip install --download-cache ~/.pipcache matplotlib==1.4.0
source env/bin/activate && pip install --download-cache ~/.pipcache inspyred==1.0
source env/bin/activate && export CVXOPT_BUILD_GLPK=1 && pip install --download-cache ~/.pipcache cvxopt==1.1.7
