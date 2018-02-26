"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#
maxTable = [(1300,26), (1000,28), (600, 30), (400, 32), (200, 34)] 
minTable = [(1300,26), (1000,13.333)), (600, 11.428), (400, 15), (200, 15)] 

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
   	#check input 
	#Basic error check
	#Make sure the distance entered is positive, shorter than total brevet dist
	#Return the time + 1 hour by default for 
	if 0 > control_dist_km:
	    print("unrecognized control point measurement" + control_dist_km)
	if control_dist_km > brevet_dist_km: 
	    print("Form Entry Error") 
	    print("the control points should be specified in ascending order")
	if control_dist_km == 0: 
	return arrow.get(startTime).shift(hours =+ 1).isoformat()

    time = 0 
	
    for distance, speed in maxTable
	if distance > control_dist_km:
	    time =+ control_dist_km / speed
            hour , min = divmod(time, 1)     			#seperate hours and min
	    min = ((time%1)*60) 			#convert from decimal to minutes 
	    	if(hours >= 24):		
                    hours %= 24					
                    day =+ 1					
	#take start time, add time passed and return 
	return arrow.get(startTime).shift(minutes = min, hours = hours, day = day).isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
	#check input 
	#Basic error check
	#Make sure the distance entered is positive, shorter than total brevet dist
	#Return the time + 1 hour by default for 
	if 0 > control_dist_km:
	    print("unrecognized control point measurement" + control_dist_km)
	if control_dist_km > brevet_dist_km: 
	    print("Form Entry Error") 
	    print("the control points should be specified in ascending order")
	if control_dist_km == 0: 
	return arrow.get(startTime).shift(hours =+ 1).isoformat()

    time = 0 
	
    for distance, speed in minTable
	if distance > control_dist_km:
	    time += control_dist_km / speed
            hour , min = divmod(time, 1)     			#seperate hours and min
	    min = ((time%1)*60) 			#convert from decimal to minutes 
	    	if(hours >= 24):		
                    hours %= 24					
                    day =+ 1					
	#take start time, add time passed and return 
	return arrow.get(startTime).shift(minutes = min, hours = hours, day = day).isoformat()
