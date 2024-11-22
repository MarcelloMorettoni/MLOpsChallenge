 ```
 1914  docker run -it -p 1880:1880 -v node_red_data:/data nodered/node-red
 1917  docker run -it -p 1880:1880 -v node_red_data:/data nodered/node-red
 1925  docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered -u node-red:dialout nodered/node-red
 1926  docker run -it -p 1880:1880 -v node_red_data:/data -u node-red:dialout nodered/node-red
 1935  npm install -g --unsafe-perm node-red
 1936  node-red
 ```