import rospy
import requests
from datetime import datetime

# import from files & fiware imports
from hri_dm.msg import Pose2D

# publishers
Artificial_PublicationPose2D = rospy.Publisher('Artificial_Pose2D', Pose2D, queue_size=100)

# callbacks
def send_msg1_pose2d():
    global Artificial_PublicationPose2D
    pose_task = Pose2D()
    pose_task.x = 5.0
    pose_task.y = 10.0
    pose_task.theta = 60.0
    my_date = datetime.utcnow()  # utc time, this is used in FELICE
    pose_task.timestamp = my_date.isoformat()
    rospy.loginfo(pose_task)
    Artificial_PublicationPose2D.publish(pose_task)

# location sender
def location_sender():
    rospy.loginfo('artificial sender node starts...')
    send_msg1_pose2d()
    rospy.Rate(0.5)  # t=1/f, where f = 0.5 <-- rospyRate

if __name__ == '__main__':
    # init the 1st publisher  or init the first pub-in
    rospy.init_node('pose2D', anonymous=True)
    print('________________________________')
    try:
        location_sender()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
