from resources.auth_blogger import RegisterBloggerResource, LoginBloggerResource
from resources.auth_admin import RegisterAdminResource, LoginAdminResource
from resources.category import CategoryResource
from resources.post import PostResource
from resources.product import ProductResource, ProductResourceDetails
from resources.review import ReviewResource

routes = (
    (RegisterBloggerResource, "/register"),
    (LoginBloggerResource, "/login"),
    (PostResource, "/post"),
    (ReviewResource, "/review"),
    (RegisterAdminResource, "/admins/create"),
    (LoginAdminResource, "/admins/login"),
    (CategoryResource, "/admin/category"),
    (ProductResource, "/admin/products"),
    (ProductResourceDetails, "/admin/product/<int:id_>"),
)