import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(rospy.get_caller_id()+ " Get: %s", msg.data)

def listener():
    rospy.init_node('Hello_world_subscriber',anonymous=True)
    rospy.Subscriber('hello_pub', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException: pass
