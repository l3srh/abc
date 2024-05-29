from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page, name="LOG_IN" ),                          # log in on -----> BASE Dir       
    path('register/',views.signup_page, name="SIGN_UP" ),               # url for new sign up registrations
    path('logout_page/',views.logout_page ,name="LOG_OUT"),

    path('userlist/',views.UsersList ,name="USER_LIST"), 
    path('shareslist/<int:id>',views.shareslist ,name="SHARE_LIST"),
    path('shareslist/<int:id>/<int:s_id>',views.shareslist ,name="SHARE_LIST"),

    path('editshare/<int:id>/<int:s_id>',views.edit_share,name="EDIT_SHARE"),
    path('deleshare/<int:id>/<int:s_id>',views.del_share,name="DEL_SHARE"),

    path('user_logs/<int:id>',views.user_logs,name="USER_LOGS")
]