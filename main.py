class Part:
    def __init__(self, name, stock=0):
        self.name = name
        self.stock = stock  
        self.sub_parts = [] 

    def add_sub_part(self, part, quantity):
        
        self.sub_parts.append((part, quantity))

    def max_buildable(self):
       
        if not self.sub_parts:   
            return self.stock

        max_count = float('inf')  
        for sub_part, quantity_needed in self.sub_parts:
            max_count = min(max_count, sub_part.max_buildable() // quantity_needed)

        return max_count



seat = Part("Seat", stock=50)
pedal = Part("Pedal", stock=60)
frame = Part("Frame", stock=60)
tube = Part("Tube", stock=35)


wheel = Part("Wheel")
wheel.add_sub_part(frame, 1)
wheel.add_sub_part(tube, 1)


bike = Part("Bike")
bike.add_sub_part(seat, 1)
bike.add_sub_part(pedal, 2)
bike.add_sub_part(wheel, 2)


print(f"Maximum bikes buildable: {bike.max_buildable()}")
