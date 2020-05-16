#!/usr/bin/env python
import rospy
from problem_no1.srv import servicedata


id = 49
type = "turtle"
availibility = False
xr = 4.1
yr = 5.2

if __name__ == '__main__':
	rospy.init_node("client")
	rospy.wait_for_service("/data_request")


try:
	
	request_data = rospy.ServiceProxy("/data_request", servicedata)
	response = request_data(id, type, availibility , round(xr,2), round(yr,2))
	rospy.loginfo("Response data: ")
	rospy.loginfo(response)
except rospy.ServiceException as e:
		rospy.logwarn("Service Failed" , str(e))
	
