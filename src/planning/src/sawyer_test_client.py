#!/usr/bin/env python
import numpy as np
import rospy
# from turtle_patrol.srv import Patrol  # Import service type
from planning.srv import enviro  # Service type
# from turtlesim.srv import TeleportAbsolute
from path_test import main #Link to Arm Movement
from geometry_msgs.msg import PoseStamped
toggle = False
def sawyer_client():
    global toggle
    # Initialize the client node
    rospy.init_node('sawyer_client')
    # Wait until patrol service is ready
    # rospy.wait_for_service('/turtle1/patrol')
    rospy.wait_for_service('/sawyer_parms/enviro')
    try:
        # Acquire service proxy
        sawyer_proxy = rospy.ServiceProxy(
            '/sawyer_parms/enviro', enviro)
        # vel = 2.0  # Linear velocity
        # omega = 1.0  # Angular velocity

        #Test Case 1
        obj_posx = np.array([2])
        obj_posy = np.array([2])
        obj_posz = np.array([2])
        obj_orientx = np.array([0.5])
        obj_orienty = np.array([0])
        obj_orientz = np.array([0])
        obj_orientw = np.array([0])
        sizex = np.array([0.5])
        sizey = np.array([0.5])
        sizez = np.array([0.5])
        name_obj = np.array(["Brick"])

        # goal = PoseStamped()
        # goal.pose.position.x = 0.502
        # goal.pose.position.y = -0.394
        # goal.pose.position.z = -0.133

        #Orientation as a quaternion
        # goal.pose.orientation.x = 0.0
        # goal.pose.orientation.y = -1.0
        # goal.pose.orientation.z = 0.0
        # goal.pose.orientation.w = 0.0

        #pos1
        pos1 = PoseStamped()
        pos1.pose.position.x = 0.803
        pos1.pose.position.y = 0.273
        pos1.pose.position.z = -0.099

        pos1.pose.orientation.x = 0.669
        pos1.pose.orientation.y = 0.742
        pos1.pose.orientation.z = 0.019
        pos1.pose.orientation.w = 0.04


        #pos2
        pos2 = PoseStamped()
        pos2.pose.position.x = 0.865
        pos2.pose.position.y = -0.214
        pos2.pose.position.z = -0.082

        pos2.pose.orientation.x = 0.684
        pos2.pose.orientation.y = 0.726
        pos2.pose.orientation.z = 0.022
        pos2.pose.orientation.w = 0.07

        


        rospy.loginfo('Moving Arm')
        # Call patrol service via the proxy

        input("press enter to move")
        toggle = not toggle
        goal = pos1 if toggle else pos2
        sawyer_proxy(obj_posx, obj_posy, obj_posz, obj_orientx, obj_orienty, obj_orientz, obj_orientw, sizex, sizey, sizez, name_obj, goal)
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s"%e)


if __name__ == '__main__':
    sawyer_client()

