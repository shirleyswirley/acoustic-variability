# Using ADCP data to characterize zooplanktonic and micronektonic variability

Code in clean_version is discussed, referenced, and used to produce figures in Chapter 6 of the PhD thesis: "Particles, prey, and purse seines: A data-driven investigation into the impacts of climate on biological processes across the global ocean" by Shirley Leung at the University of Washington. A link to the thesis is forthcoming.

Steps to use the code in clean_version to reproduce Chapter 6 figures are as follows:
0. Obtain all desired JASADCP (Joint Archive for Shipboard Acoustic Doppler Current Profiler) netcdf files as described in Chapter 6 from https://uhslc.soest.hawaii.edu/sadcp/.
1. Download the clean_version folder or clone this repo. 
2. If you prefer to use Docker + JupyterLab like me, run the following commands inside the clean_version dir. Then open the generated link in your browser as usual. (Of course, change ports and other options as you like.)

```
docker build -t <your_desired_docker_name>:<desired version tag> .
docker run --rm -i -t --mount type=bind,src=<path to clean_dir on your local machine>,dst=<preferred path to clean_dir in your docker environment> -p 8879:8879 <your_desired_docker_name>:<desired version tag>
```

3. Otherwise if you prefer virtualenvs, you can open the Dockerfile in the clean_version dir to see the required packages and create your own virtualenv with those packages.

4. Go into the clean_version/python dir, open run adcp_main.ipynb, and edit 1.) dpath (path where a folder called JASADCP is stored, which contains all of your downloaded JASADCP nc files; i.e., the path should point to the folder ABOVE or CONTAINING the JASADCP folder) and 2.) figpath (path where figures will save to) as needed. You should be able to run adcp_main.ipynb in its entirety now, which should reproduce all relevant figures!
