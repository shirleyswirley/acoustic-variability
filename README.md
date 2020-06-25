# Using ADCP data to characterize zooplanktonic and micronektonic variability

The Python code here is discussed, referenced, and used to produce figures in Appendix A "Repurposing ADCP data: A case study on Tropical Pacific mid-trophic level prey" of the PhD thesis: "Particles, prey, and purse seines: A data-driven investigation into the impacts of climate on biological processes across the global ocean" by Shirley Leung at the University of Washington (here: forthcoming link). Please cite the thesis and the code itself (here: forthcoming link) if you use any of it.

This code was written using Python 3.7.3.

Steps to use this code to reproduce Appendix A "Repurposing ADCP data: A case study on Tropical Pacific mid-trophic level prey" figures are as follows:  
1. Download the python folder or clone this repo.
2. Obtain all desired JASADCP (Joint Archive for Shipboard Acoustic Doppler Current Profiler) netcdf files as described in Appendix A from https://uhslc.soest.hawaii.edu/sadcp/. Put these ncfiles into a folder called JASADCP.
3. Build a docker container with all the required python packages using Dockerfile inside the docker dir. (Or create a virtual environment with the packages listed in the Dockerfile.)
4. To recreate the figures from Appendix A, simply run adcp_main.ipynb in the python dir. Change dpath (dpath should point to the outer folder that <i>contains</i> the inner folder called JASADCP that you created in step 2; that is, dpath should point to one folder up from JASADCP) and figpath (path to dir where you want to save figures to) as needed at the beginning of bet_skj_sep_main.ipynb.

These steps/code provide a starting framework for how you can use this amazing JASADCP dataset. Tweak it and build off of it however you want!

To properly employ this code, however, each individual user should begin by verifying that it is working how they expect. Each individual user is also responsible for calculating the errors caused by any assumptions made in the code for their individual dataset and purpose.

6/24/20: To see the latest developments to this code base, head to the develop branch, which currently has (preliminary) code to calculate S_v from time and depth-resolved temperature and salinity profiles.
