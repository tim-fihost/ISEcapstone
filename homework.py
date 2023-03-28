#!/usr/bin/env python
import rospy 
from std_msgs.msg import Float32

def solar_panel_callback(data):
    # Process solar panel data
    voltage = data.voltage
    current = data.current
    power = voltage * current

    # Publish solar panel power data to ROS topic
    power_pub.publish(power)

if __name__ == '__main__':
    rospy.init_node('solar_panel_node')

    # Subscribe to solar panel data topic
    rospy.Subscriber('solar_panel_data', SolarPanelData, solar_panel_callback)

    # Publish solar panel power data topic
    power_pub = rospy.Publisher('solar_panel_power', Float32, queue_size=10)

    rospy.spin()
