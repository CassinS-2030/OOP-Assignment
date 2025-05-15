class Superhero:
    """Base class representing a generic superhero"""
    
    def __init__(self, name, secret_identity, powers, base_of_operations):
        """
        Initialize a superhero with:
        - name: Hero name (str)
        - secret_identity: Real name (str)
        - powers: List of superpowers (list)
        - base_of_operations: Where they operate from (str)
        """
        self.name = name
        self._secret_identity = secret_identity  # Encapsulated attribute
        self.powers = powers
        self.base_of_operations = base_of_operations
        self._health = 100  # Encapsulated attribute
    
    def introduce(self):
        """Introduce the superhero"""
        print(f"I am {self.name}! My powers include: {', '.join(self.powers)}.")
    
    def use_power(self, power_index):
        """Use one of the superhero's powers"""
        if 0 <= power_index < len(self.powers):
            print(f"{self.name} uses {self.powers[power_index]}!")
        else:
            print(f"{self.name} doesn't have that power!")
    
    def take_damage(self, amount):
        """Reduce the superhero's health (encapsulated)"""
        self._health -= amount
        if self._health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {amount} damage. Health: {self._health}")
    
    def heal(self, amount):
        """Restore the superhero's health (encapsulated)"""
        self._health = min(100, self._health + amount)
        print(f"{self.name} heals {amount}. Health: {self._health}")
    
    def reveal_secret_identity(self):
        """Reveal the secret identity (encapsulated method)"""
        print(f"{self.name}'s secret identity is {self._secret_identity}!")


class FlyingSuperhero(Superhero):
    """Subclass for superheroes with flight capability"""
    
    def __init__(self, name, secret_identity, powers, base_of_operations, max_altitude):
        """
        Initialize a flying superhero with:
        - max_altitude: Maximum flying height in feet (int)
        """
        super().__init__(name, secret_identity, powers + ['flight'], base_of_operations)
        self.max_altitude = max_altitude
        self._current_altitude = 0  # Encapsulated attribute
    
    def fly(self, altitude):
        """Fly to a specific altitude"""
        if altitude <= self.max_altitude:
            self._current_altitude = altitude
            print(f"{self.name} flies to {altitude} feet!")
        else:
            print(f"{self.name} can't fly that high! Max altitude is {self.max_altitude} feet.")
    
    def land(self):
        """Land from flight"""
        self._current_altitude = 0
        print(f"{self.name} lands safely.")
    
    def use_power(self, power_index):
        """Override power use to include flight check"""
        if power_index < len(self.powers) - 1:  # Don't include 'flight' in normal power use
            super().use_power(power_index)
        elif self.powers[power_index] == 'flight':
            print(f"{self.name} is already flying at {self._current_altitude} feet!")
        else:
            print(f"{self.name} doesn't have that power!")


class TechHero(Superhero):
    """Subclass for superheroes who rely on technology"""
    
    def __init__(self, name, secret_identity, powers, base_of_operations, gadgets):
        """
        Initialize a tech hero with:
        - gadgets: List of technological gadgets (list)
        """
        super().__init__(name, secret_identity, powers, base_of_operations)
        self.gadgets = gadgets
        self._battery_level = 100  # Encapsulated attribute
    
    def use_gadget(self, gadget_index):
        """Use one of the hero's gadgets"""
        if 0 <= gadget_index < len(self.gadgets):
            self._battery_level -= 10
            print(f"{self.name} uses {self.gadgets[gadget_index]}! Battery: {self._battery_level}%")
            if self._battery_level <= 0:
                print("Warning: Power depleted! Gadgets unavailable.")
        else:
            print(f"{self.name} doesn't have that gadget!")
    
    def recharge(self):
        """Recharge all tech"""
        self._battery_level = 100
        print(f"{self.name}'s tech has been fully recharged!")


# Example usage
if __name__ == "__main__":
    # Create some superheroes
    superman = FlyingSuperhero(
        "Superman", 
        "Clark Kent", 
        ["super strength", "heat vision", "freeze breath"], 
        "Fortress of Solitude", 
        50000
    )
    
    batman = TechHero(
        "Batman",
        "Bruce Wayne",
        ["martial arts", "detective skills"],
        "Batcave",
        ["batarang", "grappling gun", "smoke pellets"]
    )
    
    # Demonstrate polymorphism
    heroes = [superman, batman]
    
    for hero in heroes:
        hero.introduce()
        hero.use_power(0)
        hero.take_damage(30)
        print()  # Blank line
    
    # Flying superhero specific methods
    superman.fly(10000)
    superman.land()
    
    # Tech hero specific methods
    batman.use_gadget(0)
    batman.use_gadget(1)
    batman.recharge()
    
    # Encapsulation demonstration
    try:
        print(batman._secret_identity)  # This works but is discouraged
        print(batman.__battery_level)  # This will fail (name mangling)
    except AttributeError as e:
        print(f"Encapsulation protected this attribute: {e}")