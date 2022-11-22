import socket, traceback
import tf
import rospy

from datetime import datetime

from std_msgs.msg import Header
from sensor_msgs.msg import Imu


def data_imu_to_msg(LIST_DATA):
    global accelerometer_x, accelerometer_y, accelerometer_z,gyroscope_x, gyroscope_y, gyroscope_z,magnetic_x, magnetic_y, magnetic_z


    accelerometer_data = LIST_DATA[2:5]
    for idx, acc in enumerate(accelerometer_data):
        accelerometer_data[idx] = float(acc.strip()[:-1])
    accelerometer_x, accelerometer_y, accelerometer_z = accelerometer_data

    gyroscope_data = LIST_DATA[6:9]
    for idx, gyro in enumerate(gyroscope_data):
        gyroscope_data[idx] = float(gyro.strip()[:-1])
    gyroscope_x, gyroscope_y, gyroscope_z = gyroscope_data

    magnetic_data = LIST_DATA[10:13]
    for idx, magneto in enumerate(magnetic_data):
        magnetic_data[idx] = float(magneto.strip()[:-1])
    magnetic_x, magnetic_y, magnetic_z = magnetic_data
    # print(magnetic_x)




def convert_to_msg():
    print("rahul ka"+str(magnetic_x))

    q = tf.transformations.quaternion_from_euler()
        imu = Imu()
        imu.header.frame_id = imu_frame_id
        imu.header.stamp = rospy.Time.from_sec(float(timestamp.strftime("%s.%f")))
        imu.orientation.x = q[0]
        imu.orientation.y = q[1]
        imu.orientation.z = q[2]
        imu.orientation.w = q[3]
        imu.linear_acceleration.x = oxts.packet.af
        imu.linear_acceleration.y = oxts.packet.al
        imu.linear_acceleration.z = oxts.packet.au
        imu.angular_velocity.x = oxts.packet.wf
        imu.angular_velocity.y = oxts.packet.wl
        imu.angular_velocity.z = oxts.packet.wu
        bag.write(topic, imu, t=imu.header.stamp) 

    













host = '172.17.18.202 '
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
while 1:
    try:
        message, address = s.recvfrom(8192)
        # print (message)
        LIST_DATA = str(message).split(",")
        rcvd_length = len(LIST_DATA)
        # print(rcvd_length)
        if(rcvd_length>10):
            # print(LIST_DATA)
            data_imu_to_msg(LIST_DATA)
            # convert_to_msg()
            print(LIST_DATA[10:13])
            print(magnetic_x)
            print("\n\n\n\n")
        # except (KeyboardInterrupt, SystemExit):
        # raise
        # except:
        # traceback.print_exc()
    except:
        pass
