# CX Knowledgebase : channelSessionState

Object Name| channelSessionState  
---|---  
Description| This object contains properties related to the state of the channel session.  
  
  


Parameter| Type| Description  
---|---|---  
`name REQUIRED`| String| The channel session can assume the following states:

  1. `STARTED`
  2. `ENDED`
  3. `CLOSED`.

  
`reasonCode` `REQUIRED`| ReasonCodeEnum| For the session state, following are the possible reasons:

  1. `CUSTOMER`
  2. `INACTIVITY`
  3. `NETWORK`
  4. `AGENT`
  5. `FORCE_CLOSED`


