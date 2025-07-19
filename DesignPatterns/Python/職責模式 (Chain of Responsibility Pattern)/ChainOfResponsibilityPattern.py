__author__ = "ChiangWei"
__date__ = "2022/05/27"

from abc import ABCMeta, abstractmethod

# class Person:
#     def __init__(self, name, dayoff, reason):
#         self.__name = name
#         self.__dayoff = dayoff
#         self.__reason = reason
#         self.__leader = None

#     def getName(self):
#         return self.__name

#     def getDayOff(self):
#         return self.__dayoff

#     def getReason(self):
#         return self.__reason

#     def setLeader(self, leader):
#         self.__leader = leader

#     def reuqest(self):
#         print("%s 申請請假 %d 天。請假事由:%s" % (self.__name, self.__dayoff, self.__reason) )
#         if self.__leader is not None:
#             self.__leader.handleRequest(self)

# class Manager(metaclass=ABCMeta):
#     def __init__(self, name, title):
#         self.__name = name
#         self.__title = title
#         self._nextHandler = None

#     def getName(self):
#         return self.__name

#     def getTitle(self):
#         return self.__title

#     def setNextHandler(self, nextHandler):
#         self._nextHandler = nextHandler

#     @abstractmethod
#     def handleRequest(self, person):
#         pass

# class Supervisor(Manager):
#     def __init__(self, name, title):
#         super().__init__(name, title)

#     def handleRequest(self, person):
#         if(person.getDayOff() <= 2):
#             print("同意 %s 請假，簽字人:%s(%s)" % (person.getName(), self.getName(), self.getTitle()) )
#         if(self._nextHandler is not None):
#             self._nextHandler.handleRequest(person)

# class DepartmentManager(Manager):
#     def __init__(self, name, title):
#         super().__init__(name, title)

#     def handleRequest(self, person):
#         if(person.getDayOff() >2 and person.getDayOff() <= 5):
#             print("同意 %s 請假，簽字人:%s(%s)" % (person.getName(), self.getName(), self.getTitle()))
#         if(self._nextHandler is not None):
#             self._nextHandler.handleRequest(person)

# class CEO(Manager):
#     def __init__(self, name, title):
#         super().__init__(name, title)

#     def handleRequest(self, person):
#         if (person.getDayOff() > 5 and person.getDayOff() <= 22):
#             print("同意 %s 請假，簽字人:%s(%s)" % (person.getName(), self.getName(), self.getTitle()))

#         if (self._nextHandler is not None):
#             self._nextHandler.handleRequest(person)

# class Administrator(Manager):
#     def __init__(self, name, title):
#         super().__init__(name, title)

#     def handleRequest(self, person):
#         print("%s 的請假申請已審核，情況屬實！已備案處理。處理人:%s(%s)\n" % (person.getName(), self.getName(), self.getTitle()))

# def testAskForLeave():
#     directLeader = Supervisor("Eren", "客戶端研發部經理")
#     departmentLeader = DepartmentManager("Eric", "技術研發中心總監")
#     ceo = CEO("Helen", "創新文化公司CEO")
#     administrator = Administrator("Nina", "行政中心總監")
#     directLeader.setNextHandler(departmentLeader)
#     departmentLeader.setNextHandler(ceo)
#     ceo.setNextHandler(administrator)

#     sunny = Person("Sunny", 1, "參加MDCC大會。")
#     sunny.setLeader(directLeader)
#     sunny.reuqest()
#     tony = Person("Tony", 5, "家裡有緊急事情！")
#     tony.setLeader(directLeader)
#     tony.reuqest()
#     pony = Person("Pony", 22, "出國深造。")
#     pony.setLeader(directLeader)
#     pony.reuqest()

# testAskForLeave()

class Request:
    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def getName(self):
        return self.__name

    def getDayOff(self):
        return self.__dayoff

    def getReason(self):
        return self.__reason

class Responsible(metaclass=ABCMeta):
    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._nextHandler = None

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.__title

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    def getNextHandler(self):
        return self._nextHandler

    def handleRequest(self, request):
        self._handleRequestImpl(request)
        
        if (self._nextHandler is not None):
            self._nextHandler.handleRequest(request)

    @abstractmethod
    def _handleRequestImpl(self, request):
        pass

class Person:
    def __init__(self, name):
        self.__name = name
        self.__leader = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setLeader(self, leader):
        self.__leader = leader

    def getLeader(self):
        return self.__leader

    def sendReuqest(self, request):
        print("%s 申請請假 %d 天。請假事由:%s" % (self.__name, request.getDayOff(), request.getReason()))
        if (self.__leader is not None):
            self.__leader.handleRequest(request)

class Supervisor(Responsible):
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() <= 2):
            print("同意 %s 請假，簽字人:%s(%s)" % (request.getName(), self.getName(), self.getTitle()))

class DepartmentManager(Responsible):
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 2 and request.getDayOff() <= 5):
            print("同意 %s 請假，簽字人:%s(%s)" % (request.getName(), self.getName(), self.getTitle()))

class CEO(Responsible):
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 5 and request.getDayOff() <= 22):
            print("同意 %s 請假，簽字人:%s(%s)" % (request.getName(), self.getName(), self.getTitle()))

class Administrator(Responsible):
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        print("%s 的請假申請已審核，情況屬實！已備案處理。處理人:%s(%s)\n" % (request.getName(), self.getName(), self.getTitle()))

def testChainOfResponsibility():
    directLeader = Supervisor("Eren", "客戶端研發部經理")
    departmentLeader = DepartmentManager("Eric", "技術研發中心總監")
    ceo = CEO("Helen", "創新文化公司CEO")
    administrator = Administrator("Nina", "行政中心總監")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    sunny = Person("Sunny")
    sunny.setLeader(directLeader)
    sunny.sendReuqest(Request(sunny.getName(), 1, "參加MDCC大會。"))
    tony = Person("Tony")
    tony.setLeader(directLeader)
    tony.sendReuqest(Request(tony.getName(), 5, "家裡有緊急事情！"))
    pony = Person("Pony")
    pony.setLeader(directLeader)
    pony.sendReuqest(Request(pony.getName(), 15, "出國深造。"))

testChainOfResponsibility()
