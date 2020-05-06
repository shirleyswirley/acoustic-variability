FROM continuumio/miniconda3
RUN conda update conda
RUN conda install -c conda-forge jupyterlab
RUN conda install -c conda-forge scikit-learn
RUN conda install -c conda-forge matplotlib
RUN conda install -c conda-forge scipy
RUN conda install -c conda-forge geopandas
RUN conda install -c conda-forge cartopy
RUN conda install -c conda-forge xarray
RUN conda update xarray
RUN conda install -c conda-forge scikit-image
RUN conda install -c conda-forge nodejs
RUN jupyter labextension install jupyterlab_vim 
CMD jupyter lab --notebook-dir=/opt/acoustic-variability --ip='0.0.0.0' --port=8879 --no-browser --allow-root
