__Data Classes in models:__

__Class Controller:__
  controllername
 
 __Class Project:__
  user =(foreignkey User)\
  controllers= (manytomany Controller)\
  __optional__
  measurements =(manytomany Timeseries)
  
  __optional__
  __Class Timeseries__
    ypoint (float)
    timepoint (float)
  
  __Class Measurement__
    name (char)
    ylabel  (char)
    xlabel (char)
    data = (manytomany Timeseries)
    
    
