# -*- coding: utf-8 -*-
class CPU(object):
    def freeze(self):
        pass

    def jump(self, address):
        pass

    def execute(self):
        pass


class Memory(object):
    def load(self, position, data):
        pass


class HardDrive(object):
    def read(self, lba, size):
        pass


# Фасад
class Computer(object):
    BOOT_ADDRESS = 00000
    BOOT_SECTOR = 000000
    SECTOR_SIZE = 4 * 1024 * 1024

    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hardDrive = HardDrive()

    def start_computer(self):
        self._cpu.freeze()
        self._memory.load(
            self.BOOT_ADDRESS,
            self._hardDrive.read(self.BOOT_SECTOR, self.SECTOR_SIZE)
        )
        self._cpu.jump(self.BOOT_ADDRESS)
        self._cpu.execute()


facade = Computer()
facade.start_computer()