# Containernet / ONOS Demo

1. SSH into my user on the scaleway vm (I have added your key) - ellie@51.158.171.12

2. This is going to need about 4 terminal sessions, so open tmux to make life eaiser. 

3. Start the onos server (this must be done in bash not zsh) - this will take about 5 mins so make sure you have tea.
```bash
cd ~/onos/
bash
sudo bazel run onos-local [-- [clean] [debug]]
```

4. When ONOS has finished loading, in another terminal enable the openflow and automatic forwarding module.
```bash
ssh onos
password: karaf
app activate org.onosproject.openflow  
app activate org.onosproject.fwd  
```
5. In another terminal, start containernet.
```bash
cd ~/containernet/pancake/
sudo python containernet.py
```
   This should have an output like this: 
   
   ![alt text](https://raw.githubusercontent.com/mavi0/supreme-parakeet/master/containernet-example.png "Sample output")

6. You should be able to ping between instances now. This doesn't pass much traffic however, so I made a quick docker image which also has iperf3 which means we can properly see some data passing through the network. To do this you're going to need to load up a couple more terminals. 

   In the first load up the iperf server:
```bash
sudo docker exec -it mn.d1 bash 
iperf3 -s
```

   In the second load up the iperf client:
```bash
sudo docker exec -it mn.d2 bash 
iperf3 -c 10.0.0.251
```
   Here's a sample output: 
   
   ![alt text](https://raw.githubusercontent.com/mavi0/supreme-parakeet/master/iperf-example.png "Sample output")

7. To access the REST API the url is [http://51.158.171.12:8181/onos/v1/flows](http://51.158.171.12:8181/onos/v1/flows) (onos/rocks)

8. To access the webGUI the url is [http://51.158.171.12:8181/onos/ui/login.html](http://51.158.171.12:8181/onos/ui/login.html) (onos/rocks)
