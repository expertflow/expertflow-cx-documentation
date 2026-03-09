# CX Knowledgebase : SIPrec-based recording using a drachtio server, and FreeSWITCH as the media server

This document provides a comprehensive guide to setting up SIPREC-based call recording based on Drachtio and using FreeSWITCH as the backend recording system. Drachtio, an open-source SIP server framework, enhances the implementation of SIPREC by providing a flexible, scalable, and programmable environment to handle SIP signaling. It acts as a bridge between the SIPREC clients and recording servers like FreeSWITCH. 

## Requirements

### Software Requirements

Item| Recommended  
---|---  
Operating system| Debian 10  
CPUs| 4  
RAM| 8 GB  
Storage| 100 GB  
Backend-recording system| [FreeSWITCh](https://expertflow-docs.atlassian.net/wiki/spaces/VRS/pages/78905374/14.2+FreeSWITCH+installation)  
Runtime-environment| Node JS  
  
### Port Utilization Requirements

The following ports must be open on the server.

Type| Application| Description| Port  
---|---|---|---  
TCP| FreeSwitch | ESL port| 8021  
TCP| FreeSwitch | Websocket port| 7443  
TCP & UDP| FreeSwitch | Internal SIP UAS| 5065  
TCP & UDP| FreeSwitch| External SIP UAS| 5080  
TCP| FreeSwitch| Used for webRTC| 5066  
TCP & UDP| FreeSwitch| For NAT profile| 5070  
UDP| FreeSwitch| H.323 gatekeeper RAS| 1719  
TCP| FreeSwitch| H.323 call signaling| 1720  
TCP| FreeSwitch| MSRP(used for calls with messaging)| 2855-2856  
UDP| FreeSwitch| STUN service, for NAT traversal| 3478-3479  
TCP| FreeSwitch| MLP protocol server| 5002  
UDP| FreeSwitch| Neighborhood service| 5003  
UDP| FreeSwitch| RTP/ RTCP multimedia streaming| 16384-32768  
TCP & UDP| Drachtio| For incoming SIPrec| 5060  
  
The ports can be opened as follows:

  * Run the following command and replace **PORT** with each of the required ports listed above:

    * 
[code]sudo iptables -A INPUT -p tcp -m tcp --dport PORT-j ACCEPT
[/code]

    * Example: 
[code] sudo iptables -A INPUT -p tcp -m tcp --dport 8021 -j ACCEPT
[/code]

  * Save this port configuration with the command:

    * 
[code]sudo iptables-save
[/code]




## Setting up the drachtio server 

Drachtio-server is a [_SIP_](http://www.ietf.org/rfc/rfc3261.txt) server that is built on the [_Sofia SIP stack_](https://github.com/davehorton/sofia-sip). It provides a high-performance SIP engine that can be controlled by client applications written in pure Javascript running on [_node.js_](https://nodejs.org/).

The node.js module that will be used to create applications controlling the server is called [_drachtio-srf_](https://github.com/davehorton/drachtio-srf). Install the following dependencies
[code] 
    sudo apt install libcurl4-openssl-dev
[/code]

After installing libcurl, do as follows:
[code] 
    git clone --depth=50 --branch=main https://github.com/drachtio/drachtio-server.git && cd drachtio-server
    git submodule update --init --recursive
    ./autogen.sh
    mkdir build && cd $_
    ../configure CPPFLAGS='-DNDEBUG'
    make
    sudo make install
[/code]

After the successful installation move the drachtio.conf.xml file to /etc 
[code] 
    mv drachtio-server/drachtio.conf.xml /etc/
[/code]

Open this file 
[code] 
    nano /etc/drachtio.conf.xml
[/code]

Replace 127.0.0.1 with the IP of your server. It’ll look like this
[code] 
    <admin port="9022" secret="cymru">192.168.1.90</admin>
[/code]

To run the drachtio server do 
[code] 
    sudo drachtio --config /etc/drachtio.conf.xml
[/code]

Now make a service for the drachtio server 
[code] 
    sudo nano /etc/systemd/system/drachtio.service
[/code]

Insert the following line in this file 
[code] 
    [Unit]
    Description=Drachtio Server
    After=network.target
    
    [Service]
    Type=simple
    ExecStart=/usr/local/bin/drachtio
    Restart=always
    
    [Install]
    WantedBy=multi-user.target
[/code]

To start drachtio as a service 
[code] 
    sudo systemctl daemon-reload
    sudo systemctl enable drachtio
    sudo systemctl start drachtio
[/code]

## Redis set up 

Redis is used in this application to store the SIPrec invite and generate SDP for legB. 

Install and start Redis. 
[code] 
    sudo apt install redis
    sudo systemctl start redis.service
    sudo systemctl status redis.service
[/code]

## Freeswitch configuration 

Configure freeswitch to record the calls coming from SBC/CUBE. 

  * Make sure that the internal SIP profile is listening on 5065 as the 5060 port is used by drachtio for listening SIPrec from CUBE.




Now open public dialplan 
[code] 
    nano /etc/freeswitch/dialplan/public.xml 
[/code]

Add the following dialpan to it 
[code] 
      <extension name="hairpin_and_record">
        <condition field="${sip_h_X-Return-Token}" expression="^(.+)$">
          <action application="export" data="sip_h_X-Return-Token=${sip_h_X-Return-Token}" />
          <action application="export" data="_nolocal_jitterbuffer_msec=100"/>
          <action application="set" data="RECORD_STEREO=true"/>
          <action application="set" data="call_id=${strftime(%Y%m%d_%H%M%S)}_${sip_from_tag}"/>
          <action application="set" data="outfile=$${base_dir}/recordings/${call_id}.wav"/> 
          <action application="record_session" data="${outfile}"/>
          <action application="set" data="hangup_after_bridge=true"/> 
          <action application="bridge" data="sofia/external/${destination_number}@${network_addr}"/>
        </condition>
      </extension>
[/code]

  * Create directory recordings in your base directory.




## Node.js application set up

This application requires a [_drachtio SIP server_](https://github.com/drachtio/drachtio-server) to be installed in your network.

Now clone this application 
[code] 
    git clone  https://github.com/drachtio/drachtio-siprec-recording-server.git
[/code]

Now enter the cloned directory and do
[code] 
    cp config/default.json.example-freeswitch config/local.json
[/code]

Make config directory if node available.

Now open local.json and provide drachtio host (server IP), drachtio port (9022), freeswitch (server IP:5065), redis host(123.0.0.1), and redis port (6379). 

We need to update the javascript code. 

Open the lib/freeswitch-call-handler.js file and replace the createSdpForResponse() function with this 
[code] 
    async function createSdpForResponse(opts, sdp, res) {
      try {
        await client.connect(); // Ensure the client is connected
    
        const result = await client.get(opts.sessionId);
    
        const combinedPayload = payloadCombiner(sdp, result, opts.sdp1, opts.sdp2);
        console.log('----------------------------- Created SDP for response.')
        return combinedPayload; // Resolve the promise with the combined payload
      } catch (err) {
        console.error('---------------Error in createSdpForResponse:', err);
        throw err; // Reject the promise with the error
      } finally {
        await client.quit(); // Ensure the client is properly closed
      }
    }
[/code]

Replace the storeUnusedSdp() function with this 
[code] 
    async function storeUnusedSdp(opts) {
      try {
        debug(`sessionId: ${opts.sessionId}: sdp ${opts.sdp2}`);
        await client.connect();  // Ensure the client is connected
    
        // Using the promise-based version of set
        const reply = await client.set(opts.sessionId, opts.sdp2, 'EX', 10);
        
        console.log('Store the unused SDP in redis     -----------------------  ' + reply);
    
        return opts;  // Resolving the promise with opts
      } catch (err) {
        console.error('Could not store the unused SDP in redis:', err);
        throw err;  // Rejecting the promise with the error
      } finally {
        await client.quit();  // Ensure the client is properly closed
      }
    }
[/code]

Replace the exchangeSdp() function with this 
[code] 
    async function exchangeSdp(sessionId, sdp) {
      try {
        await client.connect(); // Ensure the client is connected
    
        const replies = await client.multi()
          .get(sessionId)
          .set(sessionId, sdp)
          .exec();
    
        return replies[0]; // Resolve the promise with the result of the GET command
      } catch (err) {
        console.error('----------------- Error in exchangeSdp:', err);
        throw err; // Reject the promise with the error
      } finally {
        await client.quit(); // Ensure the client is properly closed
      }
    }
[/code]

Now save this file and run the following commands in drachtio-siprec-recording-server directory to run app.js 
[code] 
    npm install drachtio
    npm install redis config
    npm init
    npm cache clean --force
    npm install -g npm@latest
    npm install -g npm@10.8.1
    node app.js 
[/code]

## Testing

The tests done and their results are as below,

**Test**| **Result**  
---|---  
Normal call| Working  
Consult call | Not working, Just the audio of the first session (A1 <\--> C) before consulting is recorded, no audio recording (silent recording) for the second session (A1 <\--> A2), and when the consult call is retrieved the voice (A1 <\--> C) starts getting recording again.  
Consult-Transfer call| Not working, Just the audio of the first session (A1 <\--> C) before consulting is recorded, no audio recording (silent recording) for the second session (A1 <\--> A2), and when the consult call is transferred the voice (A2 <\--> C) still doesn’t,t get recorded.  
Direct-Transfer call| Working, The audio of the first session (A1 <\--> C) before consulting is recorded, and audio recording continues when the call is direct-transferred (C <\-->A2)n.  
Hold- Unhold call| The MOH is also recorded in the audio file  
Pause-Resume call recording| This feature is working for SIPrec recording ( Performing it by hardcoding the recording file name)  
  
## Optional: Freeswitch configuration for pause-resume recording.

To add pause-resume recording update the dialplan inserted earlier with this 
[code] 
    <extension name="hairpin_and_record">
        <condition field="${sip_h_X-Return-Token}" expression="^(.+)$">
          <action application="export" data="sip_h_X-Return-Token=${sip_h_X-Return-$      
          <action application="export" data="_nolocal_jitterbuffer_msec=100"/>
          <action application="set" data="RECORD_STEREO=true"/>
          <action application="record_session" data="/tmp/mytestingfile.wav"/>
          <action application="bind_meta_app" data="2 ab s lua::prtask_pause.lua"/>
          <action application="bind_meta_app" data="3 ab s lua::prtask_resume.lua"/>
          <action application="bridge" data="sofia/external/${destination_number}@$$
        </condition>
      </extension>
[/code]

Save this is add lua scripts at /usr/share/freeswitch/scripts/ .

Make a script prtask_pause.lua and add the following script to it 
[code] 
    local filename = "/tmp/mytestingfile.wav";
    freeswitch.consoleLog("INFO", "==============================================Pa$
    session:execute("record_session_pause", filename)
[/code]

Save this and make another script prtask_reume.lua and add the following script to it 
[code] 
    local filename = "/tmp/mytestingfile.wav";
    freeswitch.consoleLog("INFO", "==============================================Pa$
    session:execute("record_session_resume", filename)
[/code]

Save this. Now run reloadxml in fs_cli. Pause the call recording by pressing *2 and resume call recording by pressing *3 from any end side. 
