from src.test_case import TestCase
from src.target import Target
import re

class UnixBench(TestCase):
    def __init__(self, command: str):
        super().__init__(command)

    def install(self, target: Target):
        dependencies = ['snap install unixbench']
        super().install(target, dependencies)


