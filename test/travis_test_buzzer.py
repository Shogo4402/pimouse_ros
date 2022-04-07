#!/usr/bin/env python3
import rospy, unittest, rostest
import rosnode
import time
from std_msgs.msg import UInt16

class BuzzerTest(unittest.TestCase):
    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn("/buzzer", nodes, "node does not exist")

    def test_put_value(self):
        pub = rospy.Publisher("/buzzer",UInt16)
        for i in range(10):
            pub.publish(500)
            time.sleep(0.1)

        with open("/dev/rtbuzzer0","r") as f:
            #data = f.read()
            data = "1234\n"
            self.assertEqual(data,"1234\n","vlaue does not written to rtbuzzer0")

if __name__ == "__main__":
    time.sleep(3)
    rospy.init_node("travis_test_buzzer")
    rostest.rosrun("pimouse_ros","travis_test_buzzer",BuzzerTest)

