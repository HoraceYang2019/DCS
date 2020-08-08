import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('hello_pub', String, queue_size=10)

    rospy.init_node('Hello_world_publisher',anonymous=True)
    pub = rospy.Publisher('hello_pub', String, queue_size=10)

    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = "Publish Time: %s"%rospy.get_time()
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
