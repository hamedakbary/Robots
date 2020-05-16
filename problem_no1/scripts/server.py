#!/usr/bin/env python
import rospy
from problem_no1.srv import servicedata


def handle(req):
	rospy.loginfo("Request received")
	rospy.loginfo("Entered data:")
	rospy.loginfo(req)
	availibility = True
	xt = 5.4
	yt = 3
	ls = [availibility, xt, yt]
	return ls

if __name__ == '__main__':
	rospy.init_node("server")
	rospy.loginfo("Server started")
	coordinates = input("Enter x: ")
	service = rospy.Service("/data_request", servicedata, handle)	
	rospy.spin()
