from exception import OwnerAlreadyExistsError 
class Car:
    def __init__(self,brand,model,year,owner=None):
        self.brand=brand
        self.model=model
        self.year=year
        self.__owner=owner
    
    def start_engine(self):
        print(f"The engine of {self.brand} {self.model} is starting.")

    def show_info(self):
        print(f"Car info: {self.year} {self.brand} {self.model}")
    
    def set_owner(self,owner):
        if not self.__owner:
            self.__owner=owner
        else:
            #print(f"The car already has a owner: {self.__owner}. Cannot change")
            raise OwnerAlreadyExistsError(self.__owner)

    def get_owner(self):
        return self.__owner