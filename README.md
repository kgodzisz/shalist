# shalist
Since I haven't written scripts in a long time, this time I decided to get back to it. Therefore, I wrote a simple Python script that calculates the SHA256 checksum of files in a specified folder. Of course, to run it, I'll use Docker. However, this time I also provide the script. So, if you don't want to, you can run it using Python installed on your local system. The script is located in the Github repository.</br></br> 

<strong>To download files from Github:</strong></br>
<code>git clone https://github.com/kgodzisz/shalist.git</code></br></br>

<strong>Create your own image in your local repository:</strong></br>
<code>docker build -t shalist .</code></br></br>

<strong>Run the tool:</strong></br>
<code>docker run --rm -v /path/to/folder:/app/results shalist > /path/to/save/file/with/results.txt</code></br></br>

<strong>The second way is to download the prepared file from the Docker Hub repository:</strong></br>
<code>docker run --rm -v /path/to/folder:/app/results kgodzisz/shalist > /path/to/save/file/with/results.txt</code></br></br>

<strong>Description of the options used in the commands: </strong></br>
<code>--rm</code> - the container will be automatically removed after it exits; </br>
<code>-v</code> - path to the folder where the SHA256 checksum of files is to be calculated. host directory: container working directory. If you set a different working directory in the Dockerfile, you need to make changes both in the script and in the command above;</br>
<code>shalist</code> - the name of the created image we want to use; </br>
<code>kgodzisz/shalist</code> - the address of the image on the DockerHub platform;</br>
<code>/path/to/save/file/with/results.txt</code> - specify the path where the results file will be saved in the host system.</br>
