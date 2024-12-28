from abc import ABC, abstractmethod


class Workable(ABC):

    @abstractmethod
    def work(self):
        ...


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        ...


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")


class LazyPerson(Eatable):

    def eat(self):
        print("I only eat!")


class BaseManager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...


class WorkManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {Workable}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Eatable), f"`worker` must be of type {Eatable}"

        self.worker = worker

    def manage(self):
        self.worker.eat()


#before
#
#
# from abc import ABCMeta, abstractmethod
# import time
#
# class AbstractWorker:
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def work(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Worker(AbstractWorker):
#
#     def work(self):
#         print("I'm normal worker. I'm working.")
#
#     def eat(self):
#         print("Lunch break....(5 secs)")
#         time.sleep(5)
#
# class SuperWorker(AbstractWorker):
#
#     def work(self):
#         print("I'm super worker. I work very hard!")
#
#     def eat(self):
#         print("Lunch break....(3 secs)")
#         time.sleep(3)
#
#
# class Manager:
#
#     def __init__(self):
#         self.worker = None
#
#     def set_worker(self, worker):
#         assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)
#
#         self.worker = worker
#
#     def manage(self):
#         self.worker.work()
#
#     def lunch_break(self):
#         self.worker.eat()
#
# class Robot(AbstractWorker):
#
#     def work(self):
#         print("I'm a robot. I'm working....")
#
#     def eat(self):
#         print("I don't need to eat....")
#
#
# manager = Manager()
# manager.set_worker(Worker())
# manager.manage()
# manager.lunch_break()
#
# manager.set_worker(SuperWorker())
# manager.manage()
# manager.lunch_break()
#
# manager.set_worker(Robot())
# manager.manage()
# manager.lunch_break()