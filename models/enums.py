from enum import Enum


class UserRole(Enum):
    blogger = "blogger"
    admin = "admin"


class State(Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
