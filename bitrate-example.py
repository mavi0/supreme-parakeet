# Bytes and Life are from this json: /onos/v1/imr/imr/intentStats
# An example JSON path for bytes is: x.statistics[0].intents[0].00:00:00:00:00:03/None00:00:00:00:00:01/None[0].bytes
# An example JSON path for life is: x.statistics[0].intents[0].00:00:00:00:00:03/None00:00:00:00:00:01/None[0].life
# There's no documentation for what the bytes value is in the docs, but it seems to be bytes sent in that time interval
# The time interval is the interval taken between the json being updated - seems to be about 5 seconds
# The life interval is the number of seconds since the intent was created
#
# This method gets the bytes difference and time difference (intervals between reading the JSON), divides the 
# bytes by time and multiplies by 8 to get bits per second. (The 1.0 is just there to get python to cast to a float).
# There's also some safety so we don't try and divide by 0


def bitrate(old_bytes, current_bytes, old_life, current_life):
    delta_bytes = current_bytes - old_bytes
    delta_time = current_life - old_life
    
    if delta_time > 0 and delta_bytes >= 0
        return 8 * 1.0 * delta_bytes / delta_time  
    else 
        return None





