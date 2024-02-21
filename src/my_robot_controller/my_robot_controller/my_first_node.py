#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __ini__(self):
        super().__init__("ichi_node")
        self.get_logger().info("Hello from sarthak")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.shudown()

if __name__ =="main":
    main()
