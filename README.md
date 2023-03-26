# shalist
Since I haven't written scripts in a long time, this time I decided to get back to it. Therefore, I wrote a simple Python script that calculates the SHA256 checksum of files in a specified folder. Of course, to run it, I'll use Docker. However, this time I also provide the script. So, if you don't want to, you can run it using Python installed on your local system. The script is located in the Github repository. 

To download files from Github:
git clone https://github.com/kgodzisz/shalist.git

Create your own image in your local repository:
docker build -t shalist .

Run the tool:
docker run --rm -v /path/to/folder:/app/results shalist > /path/to/save/file/with/results.txt

The second way is to download the prepared file from the Docker Hub repository:
docker run --rm -v /path/to/folder:/app/results kgodzisz/shalist > /path/to/save/file/with/results.txt

Description of the options used in the commands: 
--rm - the container will be automatically removed after it exits; 
-v - path to the folder where the SHA256 checksum of files is to be calculated. host directory: container working directory. If you set a different working directory in the Dockerfile, you need to make changes both in the script and in the command above. 
shalist - the name of the created image we want to use; 
kgodzisz/shalist - the address of the image on the DockerHub platform;
/path/to/save/file/with/results.txt - specify the path where the results file will be saved in the host system.

