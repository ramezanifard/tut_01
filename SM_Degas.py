from __future__ import annotations
from abc import ABC, abstractmethod
import time

# the context class contains a _state that references the concrete state and setState method to change between states.
last_state= 'S0'

class Context:

    _state = None


    def __init__(self, state: State) -> None:
        self.setState(state)

    def setState(self, state: State):

        # print(f"Context: Transitioning to {type(state).__name__}")
        print(" \tstate transition  {} ---> {}".format(type(self._state).__name__, type(state).__name__))
        # print(type(self._state).__name__)
        self._state = state
        self._state.context = self

    def doSomething(self):
        self._state.doSomething()
        return type(self._state).__name__






class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def doSomething(self) -> None:
        pass






class State_0(State):
    def doSomething(self) -> None:
        print("Current state: State_0.")
        print("\t Initialization started ....")
        time.sleep(3) # Sleep for 3 seconds
        print("\t----- system is initialized ------")
        
        self.context.setState(State_1())


class State_1(State):
    def doSomething(self) -> None:
        global last_state
        print("Current state: State_1.")

        # wait for an event
        x=''
        while (x!='0' and x!='1' and x!='2' and x!='3' and x!='4' ):
            x = input('\tEnter the event number (0, 1, 2, 3, 4):')

        #an event happend. Take an action based on the envent number
        if (x == '0'):            
            print("\tE0 happend  --> action1_0 is executed  --> Transitioning to  S2")
            self.context.setState(State_2())
        elif (x=='1'):
            print("\tE1 happend  --> action1_0 is executed  --> :. Staying in S1")
            self.context.setState(State_1())
        elif (x=='2'):
            print("\tE2 happend:. Staying in S1")
            self.context.setState(State_1())
        elif (x=='3'):
            print("\tE3 happend:. System Pasued. Go to  S6")
            last_state = 'S1'
            self.context.setState(State_6())
        elif (x=='4'):
            print("\tE4 happend:. Error happened. Go to  S7")            
            self.context.setState(State_7())
        else:
            print("\tinvalid event. Staying in S1")
            self.context.setState(State_1())
            


class State_2(State):
    def doSomething(self) -> None:
        print("Current state: State_2.")
        
        self.context.setState(State_3())

class State_3(State):
    def doSomething(self) -> None:
        print("Current state: State_3.")
        
        self.context.setState(State_4())

class State_4(State):
    def doSomething(self) -> None:
        print("Current state: State_4.")
        
        self.context.setState(State_5())

class State_5(State):
    def doSomething(self) -> None:
        print("Current state: State_5.")
        
        self.context.setState(State_8())

class State_6(State):
    def doSomething(self) -> None:
        global last_state
        print("Current state: State_6.")
        
        if (last_state == 'S1'):
            x = ''
            while True:
                # print("Enter 'C' to continue:")
                x = input("\tEnter 'C' to continue:")
                # print('x:',x)
                if (x=='c' or x=='C'):
                    # print('wait...')
                    break

            print("\tback to state 1.")
            self.context.setState(State_1())
        else:
            self.context.setState(State_8())

class State_7(State):
    def doSomething(self) -> None:
        print("Current state: ERROR STATE (state_7). Terminating the execution.")
        
        self.context.setState(State_8())

class State_8(State):
    def doSomething(self) -> None:
        print("Current state: State_8.")        
        print("This is the end of process ...............")
        #self.context.setState(State_0())


if __name__ == "__main__":
    # sample application
    app = Context(State_0())
    print('')

    while(True):
        current_state = app.doSomething()    # this method is executed as in state 2
        print('')
        if (current_state == 'State_8'):
            break