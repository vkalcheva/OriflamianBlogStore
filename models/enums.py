from enum import Enum


class UserRole(Enum):
    blogger = "blogger"
    admin = "admin"


class State(Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"


class CategoryType(Enum):
    skin_care = "skin care"
    makeup = "makeup"
    fragrance = "fragrance"
    body = "body"
    hair = "hair"
    accessory = "accessory"
    wellness = "wellness"
    other = "other"
