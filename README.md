# Using ADCP data to characterize zooplanktonic/micronektonic distribution variability

Code in clean_version is discussed and referenced in Chapter 6 of the PhD thesis: "Particles, prey, and purse seines: A data-driven investigation into the impacts of climate on biological processes across the global ocean" by Shirley Leung at the University of Washington.

Link to thesis is forthcoming.

Steps to use the code in clean_version are as follows:
1. If you prefer to use Docker, download Dockerfile. Inside the clean_version dir, run the command:

docker build -t docker_cleanversion_adcp:v1 .
docker run --rm -i -t --mount type=bind,src=/home/shirlleu/acoustic-variability,dst=/opt/acoustic-variability -p 8879:8879 docker_miniconda_adcp:v5