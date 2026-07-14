class Overloadingdemo:
    def show_details(self,*args):
        if len(args)==1:
            print(f"Car brand: {args[0]}")
        elif len(args)==2:
            print(f"Card Brand: {args[0]}, Model: {args[1]}")
        elif len(args)==3:
            print(f"Car Brand: {args[0]}, Model:{args[1]}, year:{args[2]}")
        else:
            print(f"Invalid no of arguments. provide 3 arguments")

def overloading_demo():
    demo=Overloadingdemo()
    demo.show_details("Toyota")
    demo.show_details("Honda","Civic")
    demo.show_details("Telsa","2000","12345678")
    demo.show_details("bmw","789","1234")


        