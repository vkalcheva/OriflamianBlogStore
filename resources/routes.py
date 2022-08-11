from resources.auth_blogger import RegisterBloggerResource, LoginBloggerResource
from resources.auth_admin import RegisterAdminResource, LoginAdminResource
from resources.category import CategoryResource
from resources.product import ProductResource, ProductResourceDetails

routes = (
    (RegisterBloggerResource, "/register"),
    (LoginBloggerResource, "/login"),
    (RegisterAdminResource, "/admins/create"),
    (LoginAdminResource, "/admins/login"),
    (CategoryResource, "/admin/category"),
    (ProductResource, "/admin/products"),
    (ProductResourceDetails, "/admin/product/<int:id_>"),
)