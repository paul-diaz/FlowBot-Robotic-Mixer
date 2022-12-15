#!/usr/bin/env python
"""
Path Planning Script for Lab 7
Author: Valmik Prabhu
"""
import sys
from intera_interface import Limb
import rospy
import numpy as np
import traceback

from moveit_msgs.msg import OrientationConstraint
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose

from path_planner import PathPlanner
from planning.srv import enviro  # Service type

from forward_kinematics_server import map_keyboard
# from set_angles import set_joint_angles

try:
    from controller import Controller
except ImportError:
    pass
    
def main(obj_arr = [], end_goal = None, orien_const = None):
    """
    Main Script
    """

    # Make sure that you've looked at and understand path_planner.py before starting

    planner = PathPlanner("right_arm")
    


    Kp = 2 * np.array([0.4, 2, 1.7, 1.5, 2, 2, 3])
    # Kp = 0 * Kp
    Kd = 0.01 * np.array([2, 1, 2, 0.5, 0.8, 0.8, 0.8])
    # Kd = 0* Kd
    Ki = 0.01 * np.array([1.4, 1.4, 1.4, 1, 0.6, 0.6, 0.6])
    # Ki = 0 * np.array([1.4, 1.4, 1.4, 1, 0.6, 0.6, 0.6])
    Kw = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9])
    L = Limb("right")
    controller = Controller(Kp, Ki, Kd, Kw, L)


    # # 
    # # Add the obstacle to the planning scene here
    # #

    #TABLE OBSTACLE
    size = np.array([0.40, 1.20, 0.10])
    name = "basic_box"
    pos = PoseStamped()
    pos.header.frame_id = "base"
    pos.pose.position.x = 0.55
    pos.pose.position.y = 0
    pos.pose.position.z = -0.21
    pos.pose.orientation.x = 0
    pos.pose.orientation.y = 0
    pos.pose.orientation.z = 0
    pos.pose.orientation.w = 1
    planner.add_box_obstacle(size, name, pos)
    # for obstacle in obj_arr:
    #     planner.add_box_obstacle(obstacle[0], obstacle[1], obstacle[2])

    #Create a path constraint for the arm
    #UNCOMMENT FOR THE ORIENTATION CONSTRAINTS PART
    # if orien_const is not None:
    #     orien_const = OrientationConstraint()
    #     orien_const.link_name = "right_gripper_tip";
    #     orien_const.header.frame_id = "base";
    #     orien_const.orientation = planner.get_current_poses().orientation
    #     orien_const.absolute_x_axis_tolerance = 0.2;
    #     orien_const.absolute_y_axis_tolerance = 0.2;
    #     orien_const.absolute_z_axis_tolerance = 0.2;
    #     orien_const.weight = 1.0;

    # orien_const = OrientationConstraint()
    # orien_const.link_name = "right_gripper";
    # orien_const.header.frame_id = "base";
    # orien_const.orientation.z = -1.0;
    # orien_const.absolute_x_axis_tolerance = 0.1;
    # orien_const.absolute_y_axis_tolerance = 0.1;
    # orien_const.absolute_z_axis_tolerance = 0.1;
    # orien_const.weight = 1.0;

    #Waypoints Planning
    # print("Planning waypoints")
    # waypoints = []

    # # start with the current pose
    # start = planner.get_current_poses()
    # waypoints.append(start)

    # #Difference between start and end goal
    # dx = start.pose.position.x - end_goal.pose.position.x
    # dy = start.pose.position.y - end_goal.pose.position.y
    # dz = start.pose.position.z - end_goal.pose.position.z

    # #Iterate n number of waypoint positions between start and end
    # n = 10
    # i = 0

    # while i < n:

    #     i++

    # first orient gripper and move forward (+x)
    # wpose = geometry_msgs.msg.Pose()
    # wpose.orientation.w = 1.0
    # wpose.position.x = waypoints[0].position.x + 0.1
    # wpose.position.y = waypoints[0].position.y
    # wpose.position.z = waypoints[0].position.z
    # waypoints.append(copy.deepcopy(wpose))

    # # second move down
    # wpose.position.z -= 0.10
    # waypoints.append(copy.deepcopy(wpose))

    # # third move to the side
    # wpose.position.y += 0.05
    # waypoints.append(copy.deepcopy(wpose))


    # orien_const = OrientationConstraint()
    # orien_const.link_name = "right_gripper_tip";
    # orien_const.header.frame_id = "base";
    # orien_const.orientation.x = 1.0;
    # orien_const.orientation.y = 0.0;
    # orien_const.orientation.z = 0.0;
    # orien_const.absolute_x_axis_tolerance = 0.2;
    # orien_const.absolute_y_axis_tolerance = 0.2;
    # orien_const.absolute_z_axis_tolerance = 0.2;
    # orien_const.weight = 1.0;

    # orien_const_2 = PositionConstraint()
    # orien_const_2.link_name = "right_gripper_tip";
    # orien_const_2.header.frame_id = "base";
    # orien_const_2.target_point_offset.x = 0.6;
    # orien_const_2.target_point_offset.y = -0.3;
    # orien_const_2.target_point_offset.z = 0.0;
    # orien_const_2.weight = 1.0;



    print("Got to pose move loop in path_test")

    while not rospy.is_shutdown():
        try:
            # x, y, z = 0.8, 0.05, 0.07
            # goal_1 = PoseStamped()
            # goal_1.header.frame_id = "base"

            # #x, y, and z position
            # goal_1.pose.position.x = x
            # goal_1.pose.position.y = y
            # goal_1.pose.position.z = z

            # #Orientation as a quaternion
            # goal_1.pose.orientation.x = 0.0
            # goal_1.pose.orientation.y = -1.0
            # goal_1.pose.orientation.z = 0.0
            # goal_1.pose.orientation.w = 0.0

            goal_1 = end_goal

            # Might have to edit this . . . 
            # plan = planner.plan_to_pose(goal_1, [orien_const])
            print('moving to x: ' + str(goal_1.pose.position.x))
            print('moving to y: ' + str(goal_1.pose.position.y))
            print('moving to z: ' + str(goal_1.pose.position.z))
            # put_orient_const = [orien_const] if orien_const is not None else []
            put_orient_const = []
            repeat = True

            #Code block to choose most efficient path out of n paths cycled through
            # i = 0
            # n = 100
            # plan = planner.plan_to_pose(goal_1, put_orient_const)
            # while i < n:
            #     new_plan = planner.plan_to_pose(goal_1, put_orient_const)
            #     if (len(new_plan[1].joint_trajectory.points) < len(plan[1].joint_trajectory.points)):
            #         plan = new_plan
            #     i = i + 1
            
            #Code block to cycle through plans on rviz
            if (not orien_const):
                print("Number of joint trajectory points:")
                while(repeat):
                    i = 0
                    n = 50
                    plan = planner.plan_to_pose(goal_1, put_orient_const)
                    while i < n:
                        new_plan = planner.plan_to_pose(goal_1, put_orient_const)
                        num_joint_trajectory_points = len(new_plan[1].joint_trajectory.points)
                        print(num_joint_trajectory_points)
                        # print("%d"%len(new_plan[1].joint_trajectory.points))
                        if(len(new_plan[1].joint_trajectory.points) == 0):
                            pass
                        elif (len(new_plan[1].joint_trajectory.points) < len(plan[1].joint_trajectory.points)):
                            plan = new_plan
                        i = i + 1
                    # print(plan)
                    # answer = input("y if go, n if no, abort if pro\n")
                    # print("your answer: %s"%answer)
                    # if "abort" in answer:
                    #     return "mission abort"
                    # repeat = "y"  not in answer
                    repeat = False
                    # print(repeat)
                # input("Press <Enter> to move the right arm to goal pose 1: ")
                print("OG PLAN", plan, '\n\n\n')
                # print(plan[1])
                # if not planner.execute_plan(plan[1]): 
                # if not planner.execute_plan(plan[1]):
                #     raise Exception("Execution failed")
                if not controller.execute_plan(plan[1]):
                    raise Exception("Execution failed")
                planner.get_group().set_start_state_to_current_state()

            # Do FK
            else:
                # curr_state = planner.get_current_joint_values()
                # print("curr_state")
                # print()
                # print(curr_state)
                # angles = curr_state.positions
                seven_angles = {
                    'joints0': 0.35,
                    'joints1': -0.72,
                    'joints2': -0.53,
                    'joints3': 1.65,
                    'joints4': 0.14,
                    'joints5': -1,
                    'joints6': 2.1,
                }
                thing = map_keyboard('right')
                
                set_joint_angles(seven_angles)

            break
        except Exception as e:
            print(e)
            traceback.print_exc()
            break


    # while not rospy.is_shutdown():
    #     try:
    #         goal_3 = PoseStamped()
    #         goal_3.header.frame_id = "base"

    #         #x, y, and z position
    #         goal_3.pose.position.x = 0.6
    #         goal_3.pose.position.y = -0.3
    #         goal_3.pose.position.z = 0.0

    #         #Orientation as a quaternion
    #         goal_3.pose.orientation.x = 0.909
    #         goal_3.pose.orientation.y = -0.007
    #         goal_3.pose.orientation.z = 0.132
    #         goal_3.pose.orientation.w = -0.278
    #         plan = planner.plan_to_pose(goal_3, [], [])
    #         input("Press <Enter> to move the right arm to goal pose 3: ")
    #         if not controller.execute_plan(plan[1]):
    #             raise Exception("Execution failed")
    #         else:
    #             break
    #     except Exception as e:
    #         print(e)

    # while not rospy.is_shutdown():
    #     try:
    #         goal_3 = PoseStamped()
    #         goal_3.header.frame_id = "base  
    #         #x, y, and z position
    #         goal_3.pose.position.x = 0.6
    #         goal_3.pose.position.y = -0.3
    #         goal_3.pose.position.z = 0. 
    #         #Orientation as a quaternion
    #         goal_3.pose.orientation.x = 0.909
    #         goal_3.pose.orientation.y = -0.007
    #         goal_3.pose.orientation.z = 0.132
    #         goal_3.pose.orientation.w = -0.27   
    #         plan = planner.plan_to_pose(goal_3, [], [orien_const_2] 
    #         input("Press <Enter> to move the right arm to goal pose 4: ")
    #         if not controller.execute_plan(plan[1]):
    #             raise Exception("Execution failed")
    #     except Exception as e:
    #         print(e)
    #     else:
    #         break

    # while not rospy.is_shutdown():
    #     try:
    #         goal_3 = PoseStamped()
    #         goal_3.header.frame_id = "base"
    #         #x, y, and z position
    #         goal_3.pose.position.x = 0.6
    #         goal_3.pose.position.y = -0.3
    #         goal_3.pose.position.z = 0.0
    #         #Orientation as a quaternion
    #         goal_3.pose.orientation.x = -0.789
    #         goal_3.pose.orientation.y = 0.131
    #         goal_3.pose.orientation.z = -0.137
    #         goal_3.pose.orientation.w = 0.584
    #         plan = planner.plan_to_pose(goal_3, [], [orien_const_2])
    #         input("Press <Enter> to move the right arm to goal pose 5: ")
    #         if not controller.execute_plan(plan[1]):
    #             raise Exception("Execution failed")
    #     except Exception as e:
    #         print(e)
    #     else:
    #         break
    # while not rospy.is_shutdown():
    #     try:
    #         x, y, z = 0.770, -0.197, -0.1
    #         goal_1 = PoseStamped()
    #         goal_1.header.frame_id = "base"
    #         #x, y, and z position
    #         goal_1.pose.position.x = x
    #         goal_1.pose.position.y = y
    #         goal_1.pose.position.z = z
    #         #Orientation as a quaternion
    #         goal_1.pose.orientation.x = 1.0
    #         goal_1.pose.orientation.y = 0.0
    #         goal_1.pose.orientation.z = 0.0
    #         goal_1.pose.orientation.w = 0.0
    #         # Might have to edit this . . . 
    #         plan = planner.plan_to_pose(goal_1, [orien_const], [])
    #         input("Press <Enter> to move the right arm to goal pose 6: ")
    #         if not controller.execute_plan(plan[1]):
    #             raise Exception("Execution failed")
    #         print('opening')
    #         gripper.open()
    #         rospy.sleep(1.0)
    #         print('opened')
    #     except Exception as e:
    #         print(e)
    #         traceback.print_exc()
    #     else:
    #         break

if __name__ == '__main__':
    rospy.init_node('moveit_node')
    main()
