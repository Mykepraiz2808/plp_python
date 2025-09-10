# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")
    
    def charge(self, hours):
        self.battery_life += hours
        print(f"{self.brand} {self.model} charged for {hours} hours. Battery life is now {self.battery_life} hrs ⚡")


# Derived class: SmartphoneWithCamera (inherits Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        # Initialize parent class (Smartphone)
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels
    
    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo with {self.camera_megapixels}MP camera 📸")
    
    # Polymorphism: overriding charge method
    def charge(self, hours):
        self.battery_life += hours * 1.2  # faster charging for this model
        print(f"{self.brand} {self.model} (with camera) fast-charged for {hours} hrs. Battery life: {self.battery_life} hrs ⚡🚀")


# Creating objects
phone1 = Smartphone("Nokia", "3310", 24)
phone2 = SmartphoneWithCamera("Apple", "iPhone 15", 20, 48)

# Using methods
phone1.call("123-456-7890")
phone1.charge(2)

print("-" * 50)

phone2.call("987-654-3210")
phone2.take_photo()
phone2.charge(2)  # demonstrates polymorphism
