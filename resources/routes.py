from resources.auth import RegisterBloggerResource, LoginBloggerResource

routes = (
    (RegisterBloggerResource, "/register"),
    (LoginBloggerResource, "/login"),
)