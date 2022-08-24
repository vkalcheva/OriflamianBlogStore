from resources.auth_admin import RegisterAdminResource, LoginAdminResource
from resources.auth_blogger import RegisterBloggerResource, LoginBloggerResource
from resources.category import CategoryResource
from resources.order import OrderResource, ApproveOrderResource, RejectOrderResource
from resources.post import PostResource
from resources.product import ProductResource
from resources.review import ReviewResource, ReviewResourceDetails

routes = (
    (RegisterBloggerResource, "/register"),
    (LoginBloggerResource, "/login"),
    (PostResource, "/post"),
    (ReviewResource, "/review"),
    (ReviewResourceDetails, "/blogger/review/<int:id_>"),
    (RegisterAdminResource, "/admins/create"),
    (LoginAdminResource, "/admins/login"),
    (CategoryResource, "/admin/category"),
    (ProductResource, "/admin/products"),
    (OrderResource, "/order"),
    (ApproveOrderResource, "/admin/order/<int:id_>/approve"),
    (RejectOrderResource, "/admin/order/<int:id_>/reject"),
)
