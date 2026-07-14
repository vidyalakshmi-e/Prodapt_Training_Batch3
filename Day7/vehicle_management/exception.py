class VehicleError(Exception):
    """Base class for vehcile-related exceptions."""
    pass

class OwnerAlreadyExistsError(VehicleError):
    """Raised when trying to add an owner that already exists."""
    def __init__(self,owner_name):
        message=f"Owner '{owner_name}' already exists."
        super().__init__(message)

class InvalidBatteryCapacityError(VehicleError):
    """Raised when the battery capacity is invalid."""
    def __init__(self,capacity):
        message=f"Invalid battery capacity: {capacity}"
        super().__init__(message)