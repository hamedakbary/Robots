#!/usr/bin/env python
import rospy
from problem_no1.srv import servicedata
from std_msgs.msg import String


def handle(req):
    rospy.loginfo("Data Received:")
    rospy.loginfo(req)
    idnum = 01
    availibility = False
    ls = [idnum, availibility, xt, yt]
    return ls

if __name__ == '__main__':
    rospy.init_node("p5_server")
    service = rospy.Service("/data_exchange", servicedata, handle)
    pub = rospy.Publisher("/publish_request", String, queue_size = 10)
    rospy.loginfo("Server initiated")
    xt = input("Enter x: ")
    yt = input("Enter y: ")
    message = "New target appeared. Waiting for clients data."
    rospy.sleep(1)
    pub.publish(message)
    rospy.loginfo(message)
    rospy.spin()

rospy.loginfo("Server has been Stopped")
