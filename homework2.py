import rospy
from std_msgs.msg import Float32

def grid_callback(data):
    # Process grid data
    energy = data.energy

    # Publish grid energy data to ROS topic
    energy_pub.publish(energy)

if __name__ == '__main__':
    rospy.init_node('grid_node')

    # Subscribe to grid data topic
    rospy.Subscriber('grid_data', GridData, grid_callback)

    # Publish grid energy data topic
    energy_pub = rospy.Publisher('grid_energy', Float32, queue_size=10)

    rospy.spin()