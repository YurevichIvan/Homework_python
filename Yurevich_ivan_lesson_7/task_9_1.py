from pprint import pprint
class TrafficLight:

    def __init__(self, color = 'красный'):
        self.__color = color

    def running(self):
        switch = ['красный 4 сек', 'желтый 2 сек', 'зеленый 3 сек']
        if self.__color == 'красный':
            for i in range(3):
                print(switch[i])
        elif self.__color == 'желтый':
            switch = switch[1:] + switch[0::]
            for i in range(3):
                print(switch[i])
        elif self.__color == 'зеленый':
            switch = switch[::-1]
            for i in range(3):
                print(switch[i])


if __name__ == '__main__':
    traffic = TrafficLight('зеленый')
    #pprint(traflight)
    traffic.running()