FROM continuumio/miniconda3
RUN conda update conda
RUN conda install -c conda-forge jupyterlab
RUN conda install -c conda-forge scikit-learn
RUN conda install -c conda-forge statsmodels
RUN conda install -c conda-forge matplotlib
RUN conda install -c conda-forge scipy
RUN conda install -c conda-forge cmocean
RUN conda install -c conda-forge altair vega_datasets
RUN conda install -c conda-forge geopandas
RUN conda install -c conda-forge xarray
RUN conda install -c conda-forge cartopy
RUN conda install -c conda-forge nodejs
RUN conda install -c conda-forge descartes
RUN conda install -c conda-forge dask
RUN conda install -c conda-forge gsw
RUN pip install regionmask
RUN pip install pygam
RUN jupyter labextension install jupyterlab_vim 
RUN conda install -c conda-forge timezonefinder
WORKDIR /opt/conda/lib/python3.7/site-packages/timezonefinder/ 
RUN wget https://github.com/evansiroky/timezone-boundary-builder/releases/download/2019b/timezones-with-oceans.geojson.zip
RUN apt-get update
RUN apt-get install unzip
RUN unzip timezones-with-oceans.geojson.zip
RUN rm timezones-with-oceans.geojson.zip
RUN mv dist/combined-with-oceans.json .
RUN rm -r dist
RUN mv combined-with-oceans.json combined.json
RUN cp file_converter.py file_converter_orig.py
RUN cp helpers.py helpers_orig.py
RUN sed --in-place '8,29d' file_converter.py
RUN sed --in-place '5,9d' helpers.py
RUN cat global_settings.py helpers.py file_converter.py > file_converter_new.py
RUN mv file_converter_new.py file_converter.py
RUN python file_converter.py
RUN pip install ephem
CMD jupyter lab --notebook-dir=/opt/acoustic-variability --ip='0.0.0.0' --port=8879 --no-browser --allow-root
